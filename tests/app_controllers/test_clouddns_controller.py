from app_controllers.clouddns_controller import CloudDnsController
import json
import os
import pytest

pytest.globalData = []

c = CloudDnsController()

def test_loadGlobalData():
    with open(str(os.getcwd())+"/tests/globalData.json", "r") as f:
        pytest.globalData = json.load(f)

# def test_deleteParentDNSManagedZone():
#     assert c.deleteParentDNSManagedZone() == True

# def test_createParentDNSManagedZone():
#     assert c.createParentDNSManagedZone() == True

def test_deleteChildExternalDNSManagedZones():
    assert c.deleteChildExternalDNSManagedZones() == True

def test_createChildExternalDNSManagedZones():
    assert c.createChildExternalDNSManagedZones() == True