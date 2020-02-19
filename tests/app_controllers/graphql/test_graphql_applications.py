from app_controllers.graphql_mongodb_controller import GraphqlMongodbController
import json
import os
import pytest
from graphene.test import Client
from app_schema.applications.schema import schema
from tests.fixtures_applications import fixtures_data

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

def test_applications_first_item_query(fixtures_data):
    query = """
               {
               applications(first: 1){
                   edges {
                   node {
                       value
                       }
                   }
               }
           }"""

    expected = {
        "data": {
            "applications": {
                "edges": [
                    {
                        "node": {
                            "value": "load_balancer",
                        }
                    }
                ]
            }
        }
    }

    client = Client(schema)
    result = client.execute(query)
    assert result == expected


def test_applications_filter_by_type_item_query(fixtures_data):
    query = """
               {
               applications(first: 1, value: "load_balancer"){
                   edges {
                   node {
                       value
                       }
                   }
               }
           }"""

    expected = {
        "data": {
            "applications": {
                "edges": [
                    {
                        "node": {
                            "value": "load_balancer"
                        }
                    }
                ]
            }
        }
    }

    client = Client(schema)
    result = client.execute(query)
    assert result == expected


def test_create_application_mutation():
    query = """
            mutation {
                createApplication(applicationData:{
                        value:"git_repository"
                        }) {
                    application {
                        value
                    }
                }
            }
            """

    expected = {
        "data": {
            "createApplication": {
                "application": {
                    "value": "git_repository"
                }
            }
        }
    }

    client = Client(schema)
    result = client.execute(query)
    assert result == expected

def test_update_application_mutation():
    query = """
            mutation {
                updateApplication(applicationData:{
                        id: "5e4b28e7fae1c6e30caccb66"
                        value: "intrusion_detection_system"
                        }) {
                    application {
                        value
                    }
                }
            }
            """

    expected = {
        "data": {
            "updateApplication": {
                "application": {
                    "value": "intrusion_detection_system"
                }
            }
        }
    }

    client = Client(schema)
    result = client.execute(query)
    assert result == expected

def test_delete_application_mutation():
    query = """
            mutation {
                deleteApplication(id: "5e4b28e7fae1c6e30caccb66") {
                        success
                }
            }
            """

    expected = {"data": {"deleteApplication": {"success": True}}}

    client = Client(schema)
    result = client.execute(query)
    assert result == expected