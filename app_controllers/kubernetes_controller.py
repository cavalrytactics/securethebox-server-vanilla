import subprocess
import json
import os
from subprocess import check_output
from os import path
import yaml
from kubernetes import client, config
import re
import shutil

class KubernetesController():
    def __init__(self):
        self.podId = ""
        self.currentDirectory = ""
        self.serviceName = ""
        self.userName = ""
        self.kubectlAction = ""
        self.fileName = ""
        self.kubernetesDeploymentImage = ""
        self.kubernetesDeploymentName = ""
        self.kubernetesHost = ""
        self.googleProjectId = ""
        self.googleCredentials = ""
        self.googleKubernetesComputeZone = ""
        self.googleKubernetesComputeCluster = ""
        self.googleKubernetesComputeRegion = ""
        self.googleKubernetesClusterOperationInfo = ""
        self.googleServiceAccountEmail = ""
        self.challengeId = "0000"
        self.challengeGroupId = "1234"
        self.kubernetesPodId = ""

    def setFileName(self, fileName):
        try:
            self.fileName = fileName
            return True
        except:
            return False

    def setCurrentDirectory(self):
        try:
            self.currentDirectory = os.getcwd()
            return True
        except:
            return False

    def setClusterName(self, clusterName):
        try:
            self.googleKubernetesComputeCluster = clusterName
            return True
        except:
            return False

    def setServiceName(self, serviceName):
        try:
            self.serviceName = serviceName
            return True
        except:
            return False

    def setUserName(self, userName):
        try:
            self.userName = userName
            return True
        except:
            return False

    def setEmailAddress(self, emailAddress):
        try:
            self.emailAddress = emailAddress
            return True
        except:
            return False

    def setEnvironmentVariable(self, environmentVariable):
        try:
            if os.getenv(environmentVariable) is not None:
                setattr(self, environmentVariable,
                        os.getenv(environmentVariable))
            else:
                print(f"{environmentVariable} is not set")
                return False
            return True
        except:
            return False

    def setKubernetesDeploymentName(self, kubernetesDeploymentName):
        self.kubernetesDeploymentName = kubernetesDeploymentName

    def setKubernetesDeploymentImage(self, kubernetesDeploymentImage):
        self.kubernetesDeploymentImage = kubernetesDeploymentImage

    def setKubernetesPodId(self, kubernetesPodId):
        try:
            self.kubernetesPodId = kubernetesPodId
            return True
        except:
            return False

    def setKubectlAction(self, kubectlAction):
        try:
            self.kubectlAction = kubectlAction
            return True
        except:
            return False

    def generateIngressYamlFiles(self):
        try:
            fileList = ["01_permissions", "02_cluster-role",
                        "03_config", "04_deployment", "05_service", "06_ingress"]
            for file in fileList:
                fullFilePath = f"{self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/ingress/{self.serviceName}/{file}"
                subprocess.Popen(
                    [f"python3.7 {fullFilePath}.py {self.googleKubernetesComputeCluster} {self.serviceName} {self.emailAddress}"], shell=True).wait()
                fileCreated = path.exists(
                    f"{fullFilePath}-{self.googleKubernetesComputeCluster}-{self.serviceName}.yml")
                if fileCreated == False:
                    return False
            return True
        except:
            return False

    def generateServiceYamlFiles(self):
        try:
            fileList = ["01_deployment", "02_service", "03_ingress"]
            for file in fileList:
                fullFilePath = f"{self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/services/{self.serviceName}/{file}"
                subprocess.Popen(
                    [f"python3.7 {fullFilePath}.py {self.googleKubernetesComputeCluster} {self.serviceName} {self.userName}"], shell=True).wait()
                fileCreated = path.exists(
                    f"{fullFilePath}-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml")
                if fileCreated == False:
                    return False
            return True
        except:
            return False

    def generateAuthenticationYamlFiles(self):
        try:
            fileList = ["01_deployment", "02_service", "03_ingress"]
            for file in fileList:
                fullFilePath = f"{self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/authentication/{self.serviceName}/{file}"
                subprocess.Popen(
                    [f"python3.7 {fullFilePath}.py {self.googleKubernetesComputeCluster} {self.serviceName} {self.userName} {self.emailAddress} {self.GOOGLE_CLIENT_ID} {self.GOOGLE_CLIENT_SECRET}"], shell=True).wait()
                fileCreated = path.exists(
                    f"{fullFilePath}-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml")
                if fileCreated == False:
                    return False
            return True
        except:
            return False

    def generateStorageYamlFiles(self):
        try:
            fileList = ["01_persistent-volume", "02_persistent-volume-claim"]
            for file in fileList:
                fullFilePath = f"{self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/storage/challenges/{file}"
                subprocess.Popen(
                    [f"python3.7 {fullFilePath}.py {self.googleKubernetesComputeCluster} {self.userName} {self.challengeId} {self.challengeGroupId}"], shell=True).wait()
                fileCreated = path.exists(
                    f"{fullFilePath}-{self.userName}.yml")
                if fileCreated == False:
                    return False
            return True
        except:
            return False

    def generateDnsYamlFiles(self):
        try:
            fileList = ["01_cluster-role", "02_deployment"]
            for file in fileList:
                fullFilePath = f"{self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/dns/external-dns/{file}"
                subprocess.Popen(
                    [f"python3.7 {fullFilePath}.py {self.googleKubernetesComputeCluster} {self.userName}"], shell=True).wait()
                fileCreated = path.exists(
                    f"{fullFilePath}-external-dns-{self.userName}.yml")
                if fileCreated == False:
                    return False
            return True
        except:
            return False

    def deleteIngressYamlFiles(self):
        try:
            fileList = ["01_permissions", "02_cluster-role",
                        "03_config", "04_deployment", "05_service", "06_ingress"]
            for file in fileList:
                fullFilePath = f"{self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/ingress/{self.serviceName}/{file}"
                try:
                    subprocess.Popen(
                        [f"rm -rf {fullFilePath}-{self.googleKubernetesComputeCluster}-{self.serviceName}.yml"], shell=True).wait()
                except:
                    continue
                fileCreated = path.exists(
                    f"{fullFilePath}-{self.googleKubernetesComputeCluster}-{self.serviceName}.yml")
                if fileCreated == True:
                    return False
            return True
        except:
            return False

    def deleteServiceYamlFiles(self):
        try:
            fileList = ["01_deployment", "02_service", "03_ingress"]
            for file in fileList:
                fullFilePath = f"{self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/services/{self.serviceName}/{file}"
                try:
                    subprocess.Popen(
                        [f"rm -rf {fullFilePath}-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml"], shell=True).wait()
                except:
                    continue
                fileCreated = path.exists(
                    f"{fullFilePath}-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml")
                if fileCreated == True:
                    return False
            return True
        except:
            return False

    def deleteAuthenticationYamlFiles(self):
        try:
            fileList = ["01_deployment", "02_service", "03_ingress"]
            currentDirectory = self.currentDirectory
            for file in fileList:
                fullFilePath = f"{self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/authentication/{self.serviceName}/{file}"
                try:
                    subprocess.Popen(
                        [f"rm -rf {fullFilePath}-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml"], shell=True).wait()
                except:
                    continue
                fileCreated = path.exists(
                    f"{fullFilePath}-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml")
                if fileCreated == True:
                    return False
            return True
        except:
            return False

    def deleteDnsYamlFiles(self):
        try:
            fileList = ["01_cluster-role", "02_deployment"]
            for file in fileList:
                fullFilePath = f"{self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/dns/external-dns/{file}"
                try:
                    subprocess.Popen(
                        [f"rm -rf {fullFilePath}-external-dns-{self.userName}.yml"], shell=True).wait()
                except:
                    continue
                fileCreated = path.exists(
                    f"{fullFilePath}-external-dns-{self.userName}.yml")
                if fileCreated == True:
                    return False
            return True
        except:
            return False

    def deleteStorageYamlFiles(self):
        try:
            fileList = ["01_persistent-volume", "02_persistent-volume-claim"]
            for file in fileList:
                fullFilePath = f"{self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/storage/challenges/{file}"
                try:
                    subprocess.Popen(
                        [f"rm -rf {fullFilePath}-{self.userName}.yml"], shell=True).wait()
                except:
                    continue
                fileCreated = path.exists(
                    f"{fullFilePath}-{self.userName}.yml")
                if fileCreated == True:
                    return False
            return True
        except:
            return False

    def setGoogleProjectId(self, googleProjectId):
        try:
            self.googleProjectId = googleProjectId
            return True
        except:
            return False

    def setGoogleKubernetesComputeZone(self, googleKubernetesComputeZone):
        try:
            self.googleKubernetesComputeZone = googleKubernetesComputeZone
            return True
        except:
            return False

    def setGoogleKubernetesComputeCluster(self, googleKubernetesComputeCluster):
        try:
            self.googleKubernetesComputeCluster = googleKubernetesComputeCluster
            return True
        except:
            return False

    def setGoogleKubernetesComputeRegion(self, googleKubernetesComputeRegion):
        try:
            self.googleKubernetesComputeRegion = googleKubernetesComputeRegion
            return True
        except:
            return False

    def setGoogleServiceAccountEmail(self, googleServiceAccountEmail):
        try:
            self.googleServiceAccountEmail = googleServiceAccountEmail
            return True
        except:
            return False

    def loadGoogleKubernetesServiceAccount(self):
        try:
            subprocess.Popen(
                [f"gcloud auth activate-service-account --key-file {self.currentDirectory}/secrets/{self.fileName} >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"gcloud config set account {self.googleServiceAccountEmail} >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False
    
    def setGoogleKubernetesProject(self):
        try:
            subprocess.Popen(
                [f"gcloud config set project {self.googleProjectId} >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False

    def createGoogleKubernetesCluster(self):
        try:
            subprocess.Popen(
                [f"gcloud auth activate-service-account --key-file {self.currentDirectory}/secrets/{self.fileName} >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"gcloud config set account {self.googleServiceAccountEmail} >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"gcloud container \
                --project \"{self.googleProjectId}\" clusters create \"{self.googleKubernetesComputeCluster}\" \
                --zone \"{self.googleKubernetesComputeZone}\" \
                --no-enable-basic-auth \
                --cluster-version \"1.14.8-gke.33\" \
                --machine-type \"n1-standard-1\" \
                --image-type \"COS\" \
                --disk-type \"pd-standard\" \
                --disk-size \"30\" \
                --scopes \"https://www.googleapis.com/auth/devstorage.read_only\",\"https://www.googleapis.com/auth/logging.write\",\"https://www.googleapis.com/auth/monitoring\",\"https://www.googleapis.com/auth/servicecontrol\",\"https://www.googleapis.com/auth/service.management.readonly\",\"https://www.googleapis.com/auth/trace.append\" \
                --num-nodes \"3\" \
                --enable-ip-alias \
                --enable-stackdriver-kubernetes \
                --addons \"HorizontalPodAutoscaling\",\"HttpLoadBalancing\",\"CloudRun\" \
                --network \"projects/{self.googleProjectId}/global/networks/default\" \
                --subnetwork \"projects/{self.googleProjectId}/regions/{self.googleKubernetesComputeRegion}/subnetworks/default\" \
                --default-max-pods-per-node \"8\""], shell=True).wait()
            return True
        except:
            return False

    def getGoogleKubernetesClusterCredentials(self):
        try:
            subprocess.Popen(
                [f"gcloud auth activate-service-account --key-file {self.currentDirectory}/secrets/{self.fileName} >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"gcloud config set account {self.googleServiceAccountEmail} >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"gcloud container clusters get-credentials {self.googleKubernetesComputeCluster} --project {self.googleProjectId} --zone {self.googleKubernetesComputeZone} >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False

    def deleteGoogleKubernetesCluster(self):
        try:
            subprocess.Popen(
                [f"gcloud auth activate-service-account --key-file {self.currentDirectory}/secrets/{self.fileName} >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"gcloud config set account {self.googleServiceAccountEmail} >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"echo \"y\" | gcloud container clusters delete {self.googleKubernetesComputeCluster} --project {self.googleProjectId} --zone {self.googleKubernetesComputeZone}"], stdout=subprocess.PIPE, shell=True).wait()
            return True
        except:
            return False

    def selectGoogleKubernetesClusterContext(self):
        try:
            contexts, active_context = config.list_kube_config_contexts()
            if not contexts:
                print("Cannot find any context in kube-config file.")
                return False
            else:
                context = f"gke_{self.googleProjectId}_{self.googleKubernetesComputeZone}_{self.googleKubernetesComputeCluster}"
                config.load_kube_config(context=context)
                subprocess.Popen([f"kubectl config use-context {context}"], stdout=subprocess.PIPE, shell=True).wait()
                return True
        except:
            return False

    def manageKubernetesIngressPod(self):
        try:
            subprocess.Popen(
                [f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/ingress/{self.serviceName}/01_permissions-{self.googleKubernetesComputeCluster}-{self.serviceName}.yml >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/ingress/{self.serviceName}/02_cluster-role-{self.googleKubernetesComputeCluster}-{self.serviceName}.yml >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/ingress/{self.serviceName}/03_config-{self.googleKubernetesComputeCluster}-{self.serviceName}.yml >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/ingress/{self.serviceName}/04_deployment-{self.googleKubernetesComputeCluster}-{self.serviceName}.yml >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/ingress/{self.serviceName}/05_service-{self.googleKubernetesComputeCluster}-{self.serviceName}.yml >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen(
                [f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/ingress/{self.serviceName}/06_ingress-{self.googleKubernetesComputeCluster}-{self.serviceName}.yml >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False

    def manageKubernetesStoragePod(self):
        try:
            if self.kubectlAction == "apply":
                subprocess.Popen(
                    [f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/storage/challenges/01_persistent-volume-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
                subprocess.Popen(
                    [f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/storage/challenges/02_persistent-volume-claim-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
                return True
            elif self.kubectlAction == "delete":
                subprocess.Popen(
                    [f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/storage/challenges/02_persistent-volume-claim-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
                subprocess.Popen(
                    [f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/storage/challenges/01_persistent-volume-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
                return True
        except:
            return False

    def manageKubernetesServicePod(self):
        try:
            subprocess.Popen([f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/services/{self.serviceName}/01_deployment-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/services/{self.serviceName}/02_service-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/services/{self.serviceName}/03_ingress-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False
    
    def manageKubernetesAuthenticationPod(self):
        try:
            subprocess.Popen([f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/authentication/{self.serviceName}/01_deployment-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/authentication/{self.serviceName}/02_service-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/authentication/{self.serviceName}/03_ingress-{self.googleKubernetesComputeCluster}-{self.serviceName}-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False

    def manageKubernetesDnsPod(self):
        try:
            subprocess.Popen([f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/dns/external-dns/01_cluster-role-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
            subprocess.Popen([f"kubectl {self.kubectlAction} -f {self.currentDirectory}/app_controllers/infrastructure/kubernetes-deployments/dns/external-dns/02_deployment-{self.userName}.yml >> /dev/null 2>&1"], shell=True).wait()
            return True
        except:
            return False

    def getKubernetesPodId(self):
        command = ["kubectl", "get", "pods", "-o", "go-template", "--template",
                   "'{{range .items}}{{.metadata.name}}{{\"\\n\"}}{{end}}'"]
        out = check_output(command)
        pod_list = out.decode("utf-8").replace('\'', '').splitlines()
        pod_id = ''
        findPod = True
        while findPod:
            for i in pod_list:
                if f'{self.serviceName}' in str(i) and f'{self.userName}' in str(i):
                    pod_id = str(i)
                    findPod = False
                    self.kubernetesPodId = pod_id
                    print("POD ID:",str(pod_id))
                    return True, str(pod_id)
            return False, "0"

    def getkubernetesPodStatus(self):
        command = ["kubectl", "get", "pod", self.kubernetesPodId, "-o", "json"]
        command_output = check_output(command)
        parsedJSON = json.loads(command_output)
        currentState = parsedJSON["status"]["containerStatuses"][0]["state"]
        for i in currentState:
            if i == "running":
                return True, i
            else:
                return True, i
        return False, "unknown"

    def deployImage(self):
        try:
            subprocess.Popen([f"gcloud config set run/region us-central1"],shell=True).wait()
            subprocess.Popen([f"gcloud config set run/platform gke"],shell=True).wait()
            subprocess.Popen([f"gcloud auth activate-service-account --key-file ./secrets/stb-kubernetes-engine-sa.json"],shell=True).wait()
            subprocess.Popen([f"gcloud config set project securethebox-server"],shell=True).wait()
            subprocess.Popen([f"gcloud config set account stb-kubernetes-engine-sa@securethebox-server.iam.gserviceaccount.com"],shell=True).wait()
            subprocess.Popen([f"docker build . --tag gcr.io/securethebox-server/securethebox-server"],shell=True).wait()
            subprocess.Popen([f"docker push gcr.io/securethebox-server/securethebox-server"],shell=True).wait()
            subprocess.Popen([f"gcloud run deploy securethebox-server --image gcr.io/securethebox-server/securethebox-server --cluster testclusternamelower --cluster-location us-central1-a"],shell=True).wait()
            return True
        except:
            return False

    def deleteImage(self):
        try:
            subprocess.Popen([f"echo 'y' | gcloud run services delete securethebox-server --cluster testclusternamelower --cluster-location us-central1-a"],shell=True).wait()
            return True
        except:
            return False


""" ############################################################################################################################## """

def kubernetesGeneratePodsYaml(clusterName, serviceName, userName):
    print("Generating Pod Yaml", clusterName, serviceName, userName)
    subprocess.Popen(
        [f"python3.7 ./app_controllers/infrastructure/kubernetes-deployments/pods/{serviceName}/01_deployment.py {clusterName} {serviceName} {userName}"], shell=True).wait()

def kubernetesManagePods(clusterName, serviceName, userName, action):
    subprocess.Popen(
        [f"kubectl {action} -f ./app_controllers/infrastructure/kubernetes-deployments/pods/{serviceName}/01_{clusterName}-{serviceName}-{userName}-deployment.yml"], shell=True).wait()
