from app_controllers.cloudrun_controller import CloudRunController
import os
import json
import pytest

crc = CloudRunController()
pytest.globalData = []

def test_loadGlobalData():
    with open(str(os.getcwd())+"/tests/globalData.json", "r") as f:
        pytest.globalData = json.load(f)

def test_setCurrentDirectory():
    assert crc.setCurrentDirectory() == True

def test_setFileName():
    assert crc.setFileName(pytest.globalData["googleCloudRunServiceAccountFile"]) == True

def test_setServiceAccountEmailAddress():
    assert crc.setServiceAccountEmailAddress(pytest.globalData["googleCloudRunServiceAccountEmail"]) == True

def test_setProjectId():
    assert crc.setProjectId(pytest.globalData["googleCloudRunProjectId"]) == True

def test_setImageName():
    assert crc.setImageName(pytest.globalData["googleCloudRunImageName"]) == True

def test_setRegion():
    assert crc.setRegion(pytest.globalData["googleCloudRunRegion"]) == True

def test_setPlatform():
    assert crc.setPlatform(pytest.globalData["googleCloudRunPlatform"]) == True

def test_setDockerSources():
    assert crc.setDockerSources() == True

def test_setAccount():
    crc.setCurrentDirectory()
    crc.setProjectId(pytest.globalData["googleCloudRunProjectId"])
    crc.setServiceAccountEmailAddress(pytest.globalData["googleCloudRunServiceAccountEmail"])
    assert crc.setAccount() == True

def test_buildImage():
    crc.setProjectId(pytest.globalData["googleCloudRunProjectId"])
    crc.setImageName(pytest.globalData["googleCloudRunImageName"])
    assert crc.buildImage() == True

def test_pushImage():
    crc.setProjectId(pytest.globalData["googleCloudRunProjectId"])
    crc.setImageName(pytest.globalData["googleCloudRunImageName"])
    assert crc.pushImage() == True

def test_deployImage():
    crc.setProjectId(pytest.globalData["googleCloudRunProjectId"])
    crc.setImageName(pytest.globalData["googleCloudRunImageName"])
    crc.setRegion(pytest.globalData["googleCloudRunRegion"])
    assert crc.deployImage() == True