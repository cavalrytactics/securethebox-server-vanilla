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

    # This is used for parent root domains only. ie. {self.parentDomain}.
    def createParentDNSManagedZone(self):
        try:
            subprocess.Popen([f"gcloud dns managed-zones create \"{self.parentManagedZone}\" --dns-name \"{self.parentDomain}.\" --description \"Managed by clouddns_controller.py\" >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction start --zone \"{self.parentManagedZone}\""], shell=True).wait()
            command = ["gcloud","dns","record-sets","list","--zone",f"{self.parentManagedZone}","--name",f"{self.parentDomain}.","--type","NS"]
            out = check_output(command)
            dnsRecord = out.decode("utf-8").splitlines()[1]
            possible = ["ns-cloud-a1","ns-cloud-b1","ns-cloud-c1","ns-cloud-d1","ns-cloud-e1","ns-cloud-f1"]
            nsRecords = []
            for x in possible:
                if x in dnsRecord:
                    for i in range(1,5):
                        nsRecords.append("\""+x[:-1]+str(i)+".googledomains.com.\"")
            joinedNsRecords = " ".join(nsRecords)
            subprocess.Popen([f"gcloud dns record-sets transaction remove {joinedNsRecords} --name \"{self.parentDomain}.\" --ttl 21600 --type NS --zone \"{self.parentManagedZone}\""], shell=True).wait()        
            subprocess.Popen([f"gcloud dns record-sets transaction add ns-cloud-d{{1..4}}.googledomains.com. --name \"{self.parentDomain}.\" --ttl 300 --type NS --zone \"{self.parentManagedZone}\""], shell=True).wait()        
            subprocess.Popen([f"gcloud dns record-sets transaction add ns-cloud-d{{1..4}}.googledomains.com. --name \"{self.subManagedZonePrefix}.{self.parentDomain}.\" --ttl 300 --type NS --zone \"{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction add \"ns-cloud-d1.googledomains.com. cloud-dns-hostmaster.google.com. 1 21600 3600 259200 300\" --name \"{self.parentDomain}.\" --ttl 300 --type SOA --zone \"{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction add {self.firebasePrimaryIP} {self.firebaseSecondaryIP} --name \"{self.parentDomain}.\" --ttl 300 --type A --zone \"{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction add {self.firebasePrimaryIP} {self.firebaseSecondaryIP} --name \"www.{self.parentDomain}.\" --ttl 300 --type A --zone \"{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction add \"v=spf1 include:_spf.firebasemail.com ~all\" \"firebase={self.firebaseSiteName}\" --name \"{self.parentDomain}.\" --ttl 300 --type TXT --zone \"{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction add \"mail-{self.parentManagedZone}.dkim1._domainkey.firebasemail.com.\" --name \"firebase1._domainkey.{self.parentDomain}\" --ttl 300 --type CNAME --zone \"{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction add \"mail-{self.parentManagedZone}.dkim2._domainkey.firebasemail.com.\" --name \"firebase2._domainkey.{self.parentDomain}\" --ttl 300 --type CNAME --zone \"{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction execute --zone \"{self.parentManagedZone}\""], shell=True).wait()
            return True
        except:
            return False

    # This is used for parent root domains only. ie. {self.parentDomain}.
    def deleteParentDNSManagedZone(self):
        try:
            subprocess.Popen([f"gcloud dns record-sets transaction abort --zone \"{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction start --zone \"{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets import --zone \"{self.parentManagedZone}\" --delete-all-existing /dev/null"], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction execute --zone \"{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns managed-zones delete {self.parentManagedZone}"], shell=True).wait()
            return True
        except:
            return False


    def createChildExternalDNSManagedZones(self):
        try:
            subprocess.Popen([f"gcloud dns managed-zones create \"{self.subManagedZonePrefix}-{self.parentManagedZone}\" --dns-name \"{self.subManagedZonePrefix}.{self.parentDomain}.\" --description \"Automatically managed zone by kubernetes.io/external-dns\" >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction start --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\""], shell=True).wait()
            command = ["gcloud","dns","record-sets","list","--zone",f"{self.subManagedZonePrefix}-{self.parentManagedZone}","--name",f"{self.subDomainPrefix}.{self.parentDomain}.","--type","NS"]
            out = check_output(command)
            dnsRecord = out.decode("utf-8").splitlines()[1]
            possible = ["ns-cloud-a1","ns-cloud-b1","ns-cloud-c1","ns-cloud-d1","ns-cloud-e1","ns-cloud-f1"]
            nsRecords = []
            for x in possible:
                if x in dnsRecord:
                    for i in range(1,5):
                        nsRecords.append("\""+x[:-1]+str(i)+".googledomains.com.\"")
            joinedNsRecords = " ".join(nsRecords)
            print(joinedNsRecords)
            subprocess.Popen([f"gcloud dns record-sets transaction remove {joinedNsRecords} --name \"{self.subDomainPrefix}.{self.parentDomain}.\" --ttl 21600 --type NS --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction add ns-cloud-d{{1..4}}.googledomains.com. --name \"{self.subDomainPrefix}.{self.parentDomain}.\" --ttl 300 --type NS --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\""], shell=True).wait()        
            subprocess.Popen([f"gcloud dns record-sets transaction add \"ns-cloud-d1.googledomains.com. cloud-dns-hostmaster.google.com. 1 21600 3600 259200 300\" --name \"{self.subDomainPrefix}.{self.parentDomain}.\" --ttl 300 --type SOA --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction execute --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\""], shell=True).wait()
            return True
        except:
            return False

    def deleteChildExternalDNSManagedZones(self):
        try:
            subprocess.Popen([f"gcloud dns record-sets transaction abort --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction start --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets import --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\" --delete-all-existing /dev/null"], shell=True).wait()
            subprocess.Popen([f"gcloud dns record-sets transaction execute --zone \"{self.subManagedZonePrefix}-{self.parentManagedZone}\""], shell=True).wait()
            subprocess.Popen([f"gcloud dns managed-zones delete {self.subManagedZonePrefix}-{self.parentManagedZone}"], shell=True).wait()
            return True
        except:
            return False

    