from app_controllers.mongodb_controller import MongodbController
import json
import os
import pytest

pytest.globalData = []

c = MongodbController()

def test_loadGlobalData():
    with open(str(os.getcwd())+"/tests/globalData.json", "r") as f:
        pytest.globalData = json.load(f)

def test_setEnvironmentVariables():
    for var in pytest.globalData["environmentVariablesList"]:
        assert c.setEnvironmentVariable(var) == True

def test_setClient():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    assert c.setClient() == True

def test_setNamespace():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setClient()
    assert c.setNamespace("production_securethebox") == True

def test_setCollection():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setClient()
    c.setNamespace("production_securethebox")
    assert c.setCollection("course") == True

def test_addOneDocumentInsert():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    c.setClient()
    c.setNamespace("production_securethebox")
    c.setCollection("course")
    _object = {"key1":"value1"}
    status, output = c.addOneDocumentInsert(_object)
    assert status == True

# def test_addOneDocumentUpdateUpsert():
#     for var in pytest.globalData["environmentVariablesList"]:
#         c.setEnvironmentVariable(var)
#     c.setClient()
#     c.setNamespace("production_securethebox")
#     c.setCollection("course")
#     _object = {"keyUnique":"valueUnique"}
#     assert c.addOneDocumenUpdateUpsert(_object) == True

# def test_getDocumentById():
#     for var in pytest.globalData["environmentVariablesList"]:
#         c.setEnvironmentVariable(var)
#     c.setClient()
#     c.setNamespace("production_securethebox")
#     c.setCollection("course")
#     _object = {"key2":"value2"}
#     _, objectId = c.addOneDocumentInsert(_object)
#     status, output = c.getDocumentById(objectId)
#     assert status == True

# def test_addManyDocuments():
#     for var in pytest.globalData["environmentVariablesList"]:
#         c.setEnvironmentVariable(var)
#     c.setClient()
#     c.setNamespace("production_securethebox")
#     c.setCollection("course")
#     _objects = [{"key3":"value3"},{"key4":"value4"}]
#     status, output = c.addManyDocuments(_objects)
#     assert status == True

def test_getDocumentsCount():
    status, output = c.getDocumentsCount()
    assert status == True

def test_getDocumentCountFilter():
    status, output = c.getDocumentCountFilter({"key1":"value1"})
    assert status == True

def test_deleteOneDocumentsByKeyValue():
    assert c.deleteOneDocumentsByKeyValue({"key1":"value1"}) == True

def test_deleteManyDocumentsByKeyValue():
    assert c.deleteManyDocumentsByKeyValue({"key1":"value1"}) == True

def test_deleteAllDocuments():
    assert c.deleteAllDocuments() == True