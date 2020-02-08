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
    for file in pytest.globalData["unencryptedFileNames"]:
        tc.setCurrentDirectory()
        tc.setFileName(file)
        assert tc.setTravisEncryptFile() == True
        assert tc.setTravisUnencryptFile() == True