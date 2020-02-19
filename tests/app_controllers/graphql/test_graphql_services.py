from app_controllers.graphql_mongodb_controller import GraphqlMongodbController
import json
import os
import pytest
from graphene.test import Client
from app_schema.services.schema import schema

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

def test_create_service_mutation():
    query = """
            mutation {
                createService(serviceData:{
                        name:"Git repository",
                        value:"git_repository"
                        }) {
                    service {
                        name
                        value
                    }
                }
            }
            """

    expected = {
        "data": {
            "createService": {
                "service": {
                    "name":"Git repository",
                    "value": "git_repository"
                }
            }
        }
    }

    client = Client(schema)
    result = client.execute(query)
    assert result == expected

def test_update_service_mutation():
    query = """
            mutation {
                updateService(serviceData:{
                        id: "U2VydmljZVR5cGU6NWU0YjNhODkxMTY5NDNlYmExZmNhNjgw,
                        name: "Intrusion detection system",
                        value: "intrusion_detection_system"
                        }) {
                    service {
                        value
                        name
                    }
                }
            }
            """

    expected = {
        "data": {
            "updateService": {
                "service": {
                    "name" : "Intrusion detection system",
                    "value": "intrusion_detection_system"
                }
            }
        }
    }

    client = Client(schema)
    result = client.execute(query)
    assert result == expected

def test_delete_service_mutation():
    query = """
            mutation {
                deleteService(id: "5e4b28e7fae1c6e30caccb66") {
                        success
                }
            }
            """

    expected = {"data": {"deleteService": {"success": True}}}

    client = Client(schema)
    result = client.execute(query)
    assert result == expected

def test_create_application_mutation():
    query = """
            mutation {
                createApplication(applicationData:{
                        id: "5e4b28e7fae1c6e30caccb55,
                        name:"Nginx",
                        value:"nginx"
                        }) {
                    service {
                        name
                        value
                    }
                }
            }
            """

    expected = {
        "data": {
            "createApplication": {
                "service": {
                    "name":"Nginx",
                    "value": "nginx"
                }
            }
        }
    }

    client = Client(schema)
    result = client.execute(query)
    assert result == expected

def test_update_Application_mutation():
    query = """
            mutation {
                updateApplication(applicationData:{
                        id: "5e4b28e7fae1c6e30caccb55"
                        name: "Haproxy",
                        value: "haproxy"
                        }) {
                    service {
                        value
                        name
                    }
                }
            }
            """

    expected = {
        "data": {
            "updateService": {
                "service": {
                    "name" : "Haproxy",
                    "value": "haproxy"
                }
            }
        }
    }

    client = Client(schema)
    result = client.execute(query)
    assert result == expected

def test_delete_service_mutation():
    query = """
            mutation {
                deleteService(id: "5e4b28e7fae1c6e30caccb55") {
                        success
                }
            }
            """

    expected = {"data": {"deleteService": {"success": True}}}

    client = Client(schema)
    result = client.execute(query)
    assert result == expected