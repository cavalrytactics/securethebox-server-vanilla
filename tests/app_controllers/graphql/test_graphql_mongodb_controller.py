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

def test_addCategory1():
    c.setSchema()
    c.setGraphqlClient()
    payload = {
        "value": "application_security",
        "label": "Application security",
        "color": "#2196f3"
    }
    status, output = c.addCategory(payload)
    assert status == True

def test_addCategory2():
    c.setSchema()
    c.setGraphqlClient()
    payload = {
        "value": "infrastructure_security",
        "label": "Infrastructure security",
        "color": "#2196f3"
    }
    status, output = c.addCategory(payload)
    assert status == True

def test_addCategory3():
    c.setSchema()
    c.setGraphqlClient()
    payload = {
        "value": "cloud_security",
        "label": "Cloud security",
        "color": "#2196f3"
    }
    status, output = c.addCategory(payload)
    assert status == True

def test_addService1():
    c.setSchema()
    c.setGraphqlClient()
    payload = {
        "value": "load_balancer",
    }
    status, output = c.addService(payload)
    assert status == True

def test_addService2():
    c.setSchema()
    c.setGraphqlClient()
    payload = {
        "value": "http_server",
    }
    status, output = c.addService(payload)
    assert status == True

def test_addService3():
    c.setSchema()
    c.setGraphqlClient()
    payload = {
        "value": "git_repository",
    }
    status, output = c.addService(payload)
    assert status == True

# def test_addService4():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "database",
#         "label": "Database",
#         "subvalue": "mysql",
#         "sublabel": "Mysql"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService5():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "security_incident_event_management",
#         "label": "Security incident event management",
#         "subvalue": "ELK",
#         "sublabel": "ELK"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService6():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "intrusion_detection_system",
#         "label": "Instrustion detection system",
#         "subvalue": "Snort",
#         "sublabel": "Snort"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService7():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "instrastructure_as_code",
#         "label": "Infrastructure as code",
#         "subvalue": "terraform",
#         "sublabel": "Terraform"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService8():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "configuration_management",
#         "label": "Configuration Management",
#         "subvalue": "puppet",
#         "sublabel": "Puppet"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService9():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "http_proxy",
#         "label": "HTTP proxy",
#         "subvalue": "squid",
#         "sublabel": "Squid"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService9():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "virtual_private_network",
#         "label": "Virtual Private Network",
#         "subvalue": "pritunl",
#         "sublabel": "Pritunl"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService10():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "secrets_management",
#         "label": "Secrets management",
#         "subvalue": "vault",
#         "sublabel": "Vault"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService11():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "continuous_integration_continuous_delivery",
#         "label": "Continuous integration continuous delivery",
#         "subvalue": "jenkins",
#         "sublabel": "Jenkins"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService12():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "centralized_logging",
#         "label": "Centralized logging",
#         "subvalue": "logstash",
#         "sublabel": "Logstash"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService13():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "web_application_firewall",
#         "label": "Web application firewall",
#         "subvalue": "modsecurity",
#         "sublabel": "Modsecurity"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService14():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "endpoint_security",
#         "label": "Endpoint security",
#         "subvalue": "wazuh",
#         "sublabel": "Wazuh"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService15():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "domain_name_service",
#         "label": "Domain name service",
#         "subvalue": "bind",
#         "sublabel": "Bind"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService16():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "instrastructure",
#         "label": "Infrastructure",
#         "subvalue": "kubernetes",
#         "sublabel": "Kubernetes"
#     }
#     status, output = c.addService(payload)
#     assert status == True

# def test_addService17():
#     c.setSchema()
#     c.setGraphqlClient()
#     payload = {
#         "value": "nodejs_application",
#         "label": "Nodejs application",
#         "subvalue": "juiceshop",
#         "sublabel": "Juiceshop"
#     }
#     status, output = c.addService(payload)
#     assert status == True
