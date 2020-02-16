from app_controllers.graphql_mongodb_controller import GraphqlMongodbController
import json
import os
import pytest

pytest.globalData = []

c = GraphqlMongodbController()

def test_loadGlobalData():
    with open(str(os.getcwd())+"/tests/globalData.json", "r") as f:
        pytest.globalData = json.load(f)

def test_setEnvironmentVariables():
    for var in pytest.globalData["environmentVariablesList"]:
        assert c.setEnvironmentVariable(var) == True

def test_setMongodbClient():
    for var in pytest.globalData["environmentVariablesList"]:
        c.setEnvironmentVariable(var)
    assert c.setMongodbClient() == True

def test_setSchema():
    assert c.setSchema() == True

def test_setGraphqlClient():
    c.setSchema()
    assert c.setGraphqlClient() == True

def test_getAllCategories():
    c.setSchema()
    c.setGraphqlClient()
    status, output = c.getAllCategories()
    assert status == True

def test_getCategoryByValue():
    c.setSchema()
    c.setGraphqlClient()
    status, output = c.getCategoryByValue("red_team")
    assert status == True

def test_addCategory():
    c.setSchema()
    c.setGraphqlClient()
    category_payload = {
        "value": "web",
        "label": "WEB",
        "color": "#2196f3"
    }
    status, output = c.addCategory(category_payload)
    assert status == True

# def test_getCourseBySlug():
#     c.setSchema()
#     c.setGraphqlClient()
#     status, output = c.getCourseBySlug("red-team-this-is-slug")
#     print(output)

# def test_addCourse():
#     status, output = c.addCourse("tet",0,"test",10,"red-team-this-is-slug",7)
#     assert status == True

# def test_getAllCourses():
#     status, output = c.getAllCourses()
#     assert status == True

# def test_getCategory():
#     status, output c.getCategory("Blue Team")
#     assert status == True

# def test_deleteCategory():
#     assert c.deleteCategory("Blue Team") == True

# def test_addOneDocumentInsert():
#     for var in pytest.globalData["environmentVariablesList"]:
#         c.setEnvironmentVariable(var)
#     c.setClient()
#     c.setNamespace("production_securethebox")
#     c.setCollection("courses")
#     _object = {"key1":"value1"}
#     status, output = c.addOneDocumentInsert(_object)
#     assert status == True

# def test_addOneDocumentUpdateUpsert():
#     for var in pytest.globalData["environmentVariablesList"]:
#         c.setEnvironmentVariable(var)
#     c.setClient()
#     c.setNamespace("production_securethebox")
#     c.setCollection("courses")
#     _object = {"keyUnique":"valueUnique"}
#     assert c.addOneDocumenUpdateUpsert(_object) == True

# def test_getDocumentById():
#     for var in pytest.globalData["environmentVariablesList"]:
#         c.setEnvironmentVariable(var)
#     c.setClient()
#     c.setNamespace("production_securethebox")
#     c.setCollection("courses")
#     _object = {"key2":"value2"}
#     _, objectId = c.addOneDocumentInsert(_object)
#     status, output = c.getDocumentById(objectId)
#     assert status == True

# def test_addManyDocuments():
#     for var in pytest.globalData["environmentVariablesList"]:
#         c.setEnvironmentVariable(var)
#     c.setClient()
#     c.setNamespace("production_securethebox")
#     c.setCollection("courses")
#     _objects = [{"key3":"value3"},{"key4":"value4"}]
#     status, output = c.addManyDocuments(_objects)
#     assert status == True

# def test_getDocumentsCount():
#     status, output = c.getDocumentsCount()
#     assert status == True

# def test_getDocumentCountFilter():
#     status, output = c.getDocumentCountFilter({"key1":"value1"})
#     assert status == True

# def test_deleteOneDocumentsByKeyValue():
#     assert c.deleteOneDocumentsByKeyValue({"key1":"value1"}) == True

# def test_deleteManyDocumentsByKeyValue():
#     assert c.deleteManyDocumentsByKeyValue({"key1":"value1"}) == True

# def test_deleteAllDocuments():
#     assert c.deleteAllDocuments() == True