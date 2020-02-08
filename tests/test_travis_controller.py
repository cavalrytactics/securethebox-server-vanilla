from app_controllers.travis_controller import TravisController
import os
import json
import pytest

tc = TravisController()
pytest.globalData = []

def test_loadGlobalData():
    with open(str(os.getcwd())+"/tests/globalData.json", "r") as f:
        pytest.globalData = json.load(f)

def test_setTravisEncryptUncryptFiles():
    tc.setCurrentDirectory()
    tc.setFileName("secrets.tar")
    assert tc.tarSecretFiles(pytest.globalData["unencryptedFileNames"]) == True
    assert tc.setTravisEncryptFile() == True
    assert tc.setTravisUnencryptFile() == True