from app_controllers.kubernetes_controller import KubernetesController
import json
import os
import pytest
import time

pytest.globalData = []

c = KubernetesController()

def test_loadGlobalData():
    with open(str(os.getcwd())+"/tests/globalData.json", "r") as f:
        pytest.globalData = json.load(f)

def test_setEnvironmentVariables():
    for var in pytest.globalData["environmentVariablesList"]:
        assert c.setEnvironmentVariable(var) == True

def test_setCurrentDirectory():
    assert c.setCurrentDirectory() == True

def test_setFileName():
    for file in pytest.globalData["unencryptedFileNames"]:
        assert c.setFileName(file) == True

def test_setGoogleKubernetesComputeCluster():
    assert c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"]) == True

def test_setServiceName():
    assert c.setServiceName(pytest.globalData["serviceName_service"]) == True

def test_setUserName():
    assert c.setUserName(pytest.globalData["userName"]) == True

def test_setEmailAddress():
    assert c.setEmailAddress(pytest.globalData["emailAddress"]) == True

def test_setKubernetesPodId():
    assert c.setKubernetesPodId(pytest.globalData["kubernetesPodId"]) == True

def test_setKubectlAction():
    assert c.setKubectlAction(pytest.globalData["kubectlAction_apply"]) == True
    assert c.setKubectlAction(pytest.globalData["kubectlAction_delete"]) == True

def test_generateIngressYamlFiles():
    c.setCurrentDirectory()
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setServiceName(pytest.globalData["serviceName_ingress"])
    c.setUserName(pytest.globalData["userName"])
    c.setEmailAddress(pytest.globalData["emailAddress"])
    assert c.generateIngressYamlFiles() == True

def test_generateServiceYamlFiles():
    c.setCurrentDirectory()
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setServiceName(pytest.globalData["serviceName_service"])
    c.setUserName(pytest.globalData["userName"])
    assert c.generateServiceYamlFiles() == True

def test_generateAuthenticationYamlFiles():
    c.setCurrentDirectory()
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setServiceName(pytest.globalData["serviceName_authentication"])
    c.setUserName(pytest.globalData["userName"])
    c.setEmailAddress(pytest.globalData["emailAddress"])
    for var in pytest.globalData["environmentVariablesList"]:
        assert c.setEnvironmentVariable(var) == True
    assert c.generateAuthenticationYamlFiles() == True

def test_generateDnsYamlFiles():
    c.setCurrentDirectory()
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setServiceName(pytest.globalData["serviceName_dns"])
    c.setUserName(pytest.globalData["userName"])
    c.setEmailAddress(pytest.globalData["emailAddress"])
    for var in pytest.globalData["environmentVariablesList"]:
        assert c.setEnvironmentVariable(var) == True
    assert c.generateDnsYamlFiles() == True

def test_generateStorageYamlFiles():
    c.setCurrentDirectory()
    c.setUserName(pytest.globalData["userName"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    assert c.generateStorageYamlFiles() == True

def test_setGoogleProjectId():
    assert c.setGoogleProjectId(pytest.globalData["googleProjectId"]) == True

def test_setGoogleKubernetesComputeZone():
    assert c.setGoogleKubernetesComputeZone(pytest.globalData["googleKubernetesComputeZone"]) == True

def test_setGoogleKubernetesComputeCluster():
    assert c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"]) == True

def test_setGoogleKubernetesComputeRegion():
    assert c.setGoogleKubernetesComputeRegion(pytest.globalData["googleKubernetesComputeRegion"]) == True

def test_setGoogleServiceAccountEmail():
    assert c.setGoogleServiceAccountEmail(pytest.globalData["googleKubernetesEngineServiceAccountEmail"]) == True

def test_loadGoogleKubernetesServiceAccount():
    c.setCurrentDirectory()
    c.setFileName(pytest.globalData["googleKubernetesEngineServiceAccountFile"])
    c.setGoogleServiceAccountEmail(pytest.globalData["googleKubernetesEngineServiceAccountEmail"])
    assert c.loadGoogleKubernetesServiceAccount() == True

def test_setGoogleKubernetesProject():
    assert c.setGoogleProjectId(pytest.globalData["googleProjectId"])
    assert c.setGoogleKubernetesProject() == True

def test_createGoogleKubernetesCluster():
    c.setCurrentDirectory()
    c.setFileName(pytest.globalData["googleKubernetesEngineServiceAccountFile"])
    c.setGoogleKubernetesComputeRegion(pytest.globalData["googleKubernetesComputeRegion"])
    c.setGoogleKubernetesComputeZone(pytest.globalData["googleKubernetesComputeZone"])
    c.setGoogleProjectId(pytest.globalData["googleProjectId"])
    c.setGoogleServiceAccountEmail(pytest.globalData["googleKubernetesEngineServiceAccountEmail"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    assert c.createGoogleKubernetesCluster() == True

def test_getGoogleKubernetesClusterCredentials():
    c.setCurrentDirectory()
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setFileName(pytest.globalData["googleKubernetesEngineServiceAccountFile"])
    c.setGoogleServiceAccountEmail(pytest.globalData["googleKubernetesEngineServiceAccountEmail"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setGoogleKubernetesComputeZone(pytest.globalData["googleKubernetesComputeZone"])
    c.setGoogleKubernetesComputeRegion(pytest.globalData["googleKubernetesComputeRegion"])
    assert c.getGoogleKubernetesClusterCredentials() == True

def test_createExternalDNSManagedZones():
    c.setCurrentDirectory()
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setFileName(pytest.globalData["googleKubernetesEngineServiceAccountFile"])
    c.setGoogleServiceAccountEmail(pytest.globalData["googleKubernetesEngineServiceAccountEmail"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setGoogleKubernetesComputeZone(pytest.globalData["googleKubernetesComputeZone"])
    c.setGoogleKubernetesComputeRegion(pytest.globalData["googleKubernetesComputeRegion"])
    c.getGoogleKubernetesClusterCredentials()
    assert c.createExternalDNSManagedZones() == True

def test_deleteExternalDNSManagedZones():
    c.setCurrentDirectory()
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setFileName(pytest.globalData["googleKubernetesEngineServiceAccountFile"])
    c.setGoogleServiceAccountEmail(pytest.globalData["googleKubernetesEngineServiceAccountEmail"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setGoogleKubernetesComputeZone(pytest.globalData["googleKubernetesComputeZone"])
    c.setGoogleKubernetesComputeRegion(pytest.globalData["googleKubernetesComputeRegion"])
    c.getGoogleKubernetesClusterCredentials()
    assert c.deleteExternalDNSManagedZones() == True

def test_manageKubernetesIngressPod_apply():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setCurrentDirectory()
    c.setServiceName(pytest.globalData["serviceName_ingress"])
    c.setKubectlAction(pytest.globalData["kubectlAction_apply"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.selectGoogleKubernetesClusterContext()
    assert c.manageKubernetesIngressPod() == True

def test_manageKubernetesStoragePod_apply():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setCurrentDirectory()
    c.setUserName(pytest.globalData["userName"])
    c.setKubectlAction(pytest.globalData["kubectlAction_apply"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    assert c.manageKubernetesStoragePod() == True

def test_manageKubernetesAuthenticationPod_apply():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setCurrentDirectory()
    c.setServiceName(pytest.globalData["serviceName_service"])
    c.setUserName(pytest.globalData["userName"])
    c.setKubectlAction(pytest.globalData["kubectlAction_apply"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    assert c.manageKubernetesAuthenticationPod() == True

def test_manageKubernetesDnsPod_apply():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setCurrentDirectory()
    c.setServiceName(pytest.globalData["serviceName_dns"])
    c.setUserName(pytest.globalData["userName"])
    c.setKubectlAction(pytest.globalData["kubectlAction_apply"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    assert c.manageKubernetesDnsPod() == True

def test_manageKubernetesServicePod_apply():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setCurrentDirectory()
    c.setServiceName(pytest.globalData["serviceName_service"])
    c.setUserName(pytest.globalData["userName"])
    c.setKubectlAction(pytest.globalData["kubectlAction_apply"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    assert c.manageKubernetesServicePod() == True

def test_getKubernetesPodId():
    for x in range(30):
        time.sleep(1)
        print(x)
    c.setUserName(pytest.globalData["userName"])
    c.setServiceName(pytest.globalData["serviceName_service"])
    value, podId = c.getKubernetesPodId()
    assert value == True
    assert podId != "0"

def test_getKubernetesPodStatus():
    c.setUserName(pytest.globalData["userName"])
    c.setServiceName(pytest.globalData["serviceName_service"])
    value, podId = c.getKubernetesPodId()
    c.setKubernetesPodId(podId)
    value, podStatus = c.getkubernetesPodStatus()
    assert value == True

def test_manageKubernetesServicePod_delete():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setCurrentDirectory()
    c.setServiceName(pytest.globalData["serviceName_service"])
    c.setUserName(pytest.globalData["userName"])
    c.setKubectlAction(pytest.globalData["kubectlAction_delete"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    assert c.manageKubernetesServicePod() == True

def test_manageKubernetesAuthenticationPod_delete():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setCurrentDirectory()
    c.setServiceName(pytest.globalData["serviceName_service"])
    c.setUserName(pytest.globalData["userName"])
    c.setKubectlAction(pytest.globalData["kubectlAction_delete"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    assert c.manageKubernetesAuthenticationPod() == True

def test_manageKubernetesDnsPod_delete():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setCurrentDirectory()
    c.setServiceName(pytest.globalData["serviceName_dns"])
    c.setUserName(pytest.globalData["userName"])
    c.setKubectlAction(pytest.globalData["kubectlAction_delete"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    assert c.manageKubernetesDnsPod() == True

def test_manageKubernetesStoragePod_delete():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setCurrentDirectory()
    c.setUserName(pytest.globalData["userName"])
    c.setKubectlAction(pytest.globalData["kubectlAction_delete"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    assert c.manageKubernetesStoragePod() == True

def test_manageKubernetesIngressPod_delete():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setCurrentDirectory()
    c.setServiceName(pytest.globalData["serviceName_ingress"])
    c.setKubectlAction(pytest.globalData["kubectlAction_delete"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.selectGoogleKubernetesClusterContext()
    assert c.manageKubernetesIngressPod() == True

def test_deleteGoogleKubernetesCluster():
    c.setCurrentDirectory()
    c.setFileName(pytest.globalData["googleKubernetesEngineServiceAccountFile"])
    c.setGoogleKubernetesComputeRegion(pytest.globalData["googleKubernetesComputeRegion"])
    c.setGoogleKubernetesComputeZone(pytest.globalData["googleKubernetesComputeZone"])
    c.setGoogleProjectId(pytest.globalData["googleProjectId"])
    c.setGoogleServiceAccountEmail(pytest.globalData["googleKubernetesEngineServiceAccountEmail"])
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.selectGoogleKubernetesClusterContext()
    assert c.deleteGoogleKubernetesCluster() == True

def test_deleteIngressYamlFiles():
    c.setCurrentDirectory()
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setServiceName(pytest.globalData["serviceName_ingress"])
    c.setUserName(pytest.globalData["userName"])
    assert c.deleteIngressYamlFiles() == True

def test_deleteServiceYamlFiles():
    c.setCurrentDirectory()
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setServiceName(pytest.globalData["serviceName_service"])
    c.setUserName(pytest.globalData["userName"])
    assert c.deleteServiceYamlFiles() == True

def test_deleteAuthenticationYamlFiles():
    c.setCurrentDirectory()
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setServiceName(pytest.globalData["serviceName_authentication"])
    c.setUserName(pytest.globalData["userName"])
    assert c.deleteAuthenticationYamlFiles() == True
    
def test_deleteDnsYamlFiles():
    c.setCurrentDirectory()
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setServiceName(pytest.globalData["serviceName_dns"])
    c.setUserName(pytest.globalData["userName"])
    assert c.deleteDnsYamlFiles() == True

def test_deleteStorageYamlFiles():
    c.setCurrentDirectory()
    c.setGoogleKubernetesComputeCluster(pytest.globalData["googleKubernetesComputeCluster"])
    c.setUserName(pytest.globalData["userName"])
    assert c.deleteStorageYamlFiles() == True