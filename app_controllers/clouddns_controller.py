import subprocess
import json
import os
from subprocess import check_output
from os import path
import yaml
from kubernetes import client, config
import re
import shutil
import time

class CloudDnsController():
    def __init__(self):
        self.parentDomain = "securethebox.us"
        self.subDomainPrefix = "us-central1-a"
        self.parentManagedZone = "securethebox-us"
        self.subManagedZonePrefix = "us-central1-a"
        self.firebaseSiteName = "thebox-client"
        self.firebasePrimaryIP = "151.101.1.195"
        self.firebaseSecondaryIP = "151.101.65.195"

    def setParentDomain(self,parentDomain):
        try:
            self.parentDomain = parentDomain
            return True
        except:
            return False

    def setSubDomainPrefix(self,subDomainPrefix):
        try:
            self.subDomainPrefix = subDomainPrefix
            return True
        except:
            return False
    
    def setParentManagedZone(self,parentManagedZone):
        try:
            self.parentManagedZone = parentManagedZone
            return True
        except:
            return False

    def setSubManagedZonePrefix(self,subManagedZonePrefix):
        try:
            self.subManagedZonePrefix = subManagedZonePrefix
            return True
        except:
            return False

    # This is used for parent root domains only. ie. {self.parentDomain}.
    def createParentDNSManagedZone(self):
        try:
            subprocess.Popen([f"gcloud dns managed-zones create \"{self.parentManagedZone}\" --dns-name \"{self.parentDomain}.\" --description \"Managed by clouddns_controller.py\" >> /dev/null 2>&1"], shell=True).wait()
            command = ["gcloud","dns","record-sets","list","--zone",f"{self.parentManagedZone}","--name",f"{self.parentDomain}.","--type","NS"]
            whileLoop = True
            while whileLoop:                
                out = check_output(command)
                dnsRecord = out.decode("utf-8").splitlines()[1]
                if "ns-cloud-d1" in dnsRecord:
                    whileLoop = False
                else:
                    subprocess.Popen([f"gcloud dns managed-zones delete {self.parentManagedZone}"], shell=True).wait()
                    subprocess.Popen([f"gcloud dns managed-zones create \"{self.parentManagedZone}\" --dns-name \"{self.parentDomain}.\" --description \"Managed by clouddns_controller.py\" >> /dev/null 2>&1"], shell=True).wait()
            
            subprocess.Popen([f"gcloud dns record-sets transaction start --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
            command2 = ["gcloud","dns","record-sets","list","--zone",f"{self.subManagedZonePrefix}-{self.parentManagedZone}","--name",f"{self.subManagedZonePrefix}.{self.parentDomain}.","--type","NS"]
            out2 = check_output(command2)
            dnsRecord = out2.decode("utf-8").splitlines()[1]
            options = ["ns-cloud-a", "ns-cloud-b", "ns-cloud-c", "ns-cloud-d", "ns-cloud-e", "ns-cloud-f"]
            for x in options:
                if x in dnsRecord:
                    subprocess.Popen([f"gcloud dns record-sets transaction add {x}{{1..4}}.googledomains.com. --name \"{self.subManagedZonePrefix}.{self.parentDomain}.\" --ttl 300 --type NS --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()            
                    subprocess.Popen([f"gcloud dns record-sets transaction add {self.firebasePrimaryIP} {self.firebaseSecondaryIP} --name \"{self.parentDomain}.\" --ttl 300 --type A --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
                    subprocess.Popen([f"gcloud dns record-sets transaction add {self.firebasePrimaryIP} {self.firebaseSecondaryIP} --name \"www.{self.parentDomain}.\" --ttl 300 --type A --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
                    subprocess.Popen([f"gcloud dns record-sets transaction add \"v=spf1 include:_spf.firebasemail.com ~all\" \"firebase={self.firebaseSiteName}\" --name \"{self.parentDomain}.\" --ttl 300 --type TXT --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
                    subprocess.Popen([f"gcloud dns record-sets transaction add \"mail-{self.parentManagedZone}.dkim1._domainkey.firebasemail.com.\" --name \"firebase1._domainkey.{self.parentDomain}\" --ttl 300 --type CNAME --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
                    subprocess.Popen([f"gcloud dns record-sets transaction add \"mail-{self.parentManagedZone}.dkim2._domainkey.firebasemail.com.\" --name \"firebase2._domainkey.{self.parentDomain}\" --ttl 300 --type CNAME --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
                    subprocess.Popen([f"gcloud dns record-sets transaction execute --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False

    # This is used for parent root domains only. ie. {self.parentDomain}.
    def deleteParentDNSManagedZone(self):
        try:
            subprocess.Popen([f"gcloud dns record-sets transaction abort --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction start --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets import --zone \"{self.parentManagedZone}\" --delete-all-existing /dev/null >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction execute --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud dns managed-zones delete {self.parentManagedZone} >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False

    def addChildInParentDNSManagedZone(self):
        subprocess.Popen([f"gcloud dns record-sets transaction start --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
        command = ["gcloud","dns","record-sets","list","--zone",f"{self.subManagedZonePrefix}-{self.parentManagedZone}","--name",f"{self.subManagedZonePrefix}.{self.parentDomain}.","--type","NS"]
        out = check_output(command2)
        dnsRecord = out.decode("utf-8").splitlines()[1]
        options = ["ns-cloud-a", "ns-cloud-b", "ns-cloud-c", "ns-cloud-d", "ns-cloud-e", "ns-cloud-f"]
        for x in options:
            if x in dnsRecord:
                subprocess.Popen([f"gcloud dns record-sets transaction add {x}{{1..4}}.googledomains.com. --name \"{self.subManagedZonePrefix}.{self.parentDomain}.\" --ttl 300 --type NS --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()            
                subprocess.Popen([f"gcloud dns record-sets transaction execute --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()

    def removeChildInParentDNSManagedZone(self):
        subprocess.Popen([f"gcloud dns record-sets transaction start --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
        command = ["gcloud","dns","record-sets","list","--zone",f"{self.subManagedZonePrefix}-{self.parentManagedZone}","--name",f"{self.subManagedZonePrefix}.{self.parentDomain}.","--type","NS"]
        out = check_output(command2)
        dnsRecord = out.decode("utf-8").splitlines()[1]
        options = ["ns-cloud-a", "ns-cloud-b", "ns-cloud-c", "ns-cloud-d", "ns-cloud-e", "ns-cloud-f"]
        for x in options:
            if x in dnsRecord:
                subprocess.Popen([f"gcloud dns record-sets transaction remove {x}{{1..4}}.googledomains.com. --name \"{self.subManagedZonePrefix}.{self.parentDomain}.\" --ttl 300 --type NS --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()            
                subprocess.Popen([f"gcloud dns record-sets transaction execute --zone \"{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()

    def createChildExternalDNSManagedZones(self):
        try:
            subprocess.Popen([f"gcloud dns managed-zones create \"{self.subManagedZonePrefix}-{self.parentManagedZone}\" --dns-name \"{self.subManagedZonePrefix}.{self.parentDomain}.\" --description \"Automatically managed zone by kubernetes.io/external-dns\" >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False

    def deleteChildExternalDNSManagedZones(self):
        try:
            subprocess.Popen([f"gcloud dns record-sets transaction abort --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction start --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets import --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\" --delete-all-existing /dev/null >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction execute --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\" >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud dns managed-zones delete {self.subManagedZonePrefix}-{self.parentManagedZone} >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False