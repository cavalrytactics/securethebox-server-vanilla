from mongoengine import connect
from bson import ObjectId
from app_schema.course import schema
from app_models.graphql.models import (
    Application,
    Configuration,
    Credential,
    Category,
    Competency,
    Course,
    Question,
    Report,
    Scope,
    Service,
    Solution,
    Subscription,
    Topic,
    User,
)
import os
from gql import gql, Client
from graphene.test import Client as TestClient
from gql.transport.requests import RequestsHTTPTransport
import sys
import json 

class GraphqlMongodbController():
    def __init__(self):
        self.mongodbConnection = False
        self.graphqlConnection = False
        self.schema = object
        self.gqlclient = object
        self.mongodbclient = object

    def setEnvironmentVariable(self, environmentVariable):
        try:
            if os.getenv(environmentVariable) is not None:
                setattr(self, environmentVariable,
                        os.getenv(environmentVariable))
            else:
                print(f"{environmentVariable} is not set")
                return False
            return True
        except:
            return False

    def setMongodbClient(self):
        try:
            self.mongodbclient = connect("production_securethebox", host="mongodb+srv://"+os.environ["MONGODB_USER"]+":"+os.environ["MONGODB_PASSWORD"]+"@"+os.environ["MONGODB_CLUSTER"], alias="default")
            self.mongodbConnection = True
            return True
        except:
            return False

    def setSchema(self):
        try:
            self.schema = schema
            return True
        except:
            return False
    
    def setGraphqlClient(self):
        try:
            if "pytest" in sys.modules:
                self.gqlclient = TestClient(self.schema)
                self.graphqlConnection = True
                return True
            else:
                self.gqlclient = Client(transport=RequestsHTTPTransport(url='http://localhost:5000/graphql'), schema=self.schema)
                self.graphqlConnection = True
                return True
        except:
            return False

    def getCategoryByValue(self,value):
        try:
            query = gql('''
            query ($value: String!) {
                allCategories (value: $value) {
                    edges {
                        node {
                            id,
                            value,
                            label
                        }
                    }
                }
            }
            ''')
            variables = {"value":value}
            if "pytest" in sys.modules:
                output = self.gqlclient.execute(query,variables=variables)
                print(output)
            else:
                output = self.gqlclient.execute(query,variable_values=json.dumps(variables))
                print(output
            return True, output["data"]["allCategories"]["edges"]
        except:
            return False

    def getServiceByValue(self,value):
        try:
            query = gql('''
            query ($value: String!) {
                allServices (value: $value) {
                    edges {
                        node {
                            id,
                            value,
                            label
                        }
                    }
                }
            }
            ''')
            variables = {"value":value}
            if "pytest" in sys.modules:
                output = self.gqlclient.execute(query,variables=variables)
            else:
                output = self.gqlclient.execute(query,variable_values=json.dumps(variables))
            return True, output["data"]["allServices"]["edges"]
        except:
            return False

    def getApplicationByValue(self,value):
        try:
            query = gql('''
            query ($value: String!) {
                allApplications (value: $value) {
                    edges {
                        node {
                            id,
                            value,
                            label
                        }
                    }
                }
            }
            ''')
            variables = {"value":value}
            if "pytest" in sys.modules:
                output = self.gqlclient.execute(query,variables=variables)
            else:
                output = self.gqlclient.execute(query,variable_values=json.dumps(variables))
            return True, output["data"]["allApplications"]["edges"]
        except:
            return False

    def mutate(self):
        try:
            query = gql('''
            mutation CreateCourse($title: String!, $activeStep: Int!, $description: String!, $length: Int!, $slug: String!, $totalSteps: Int!) {
                createCourse(title: $title, activeStep: $activeStep, description: $description, length: $length, slug: $slug, totalSteps: $totalSteps) {
                    course {
                        title
                        activeStep
                        description
                        length
                        slug
                        totalSteps
                    }
                }
            }
            ''')
            variables = {
                "title": "Blue Team - Security Engineer IC1",
                "activeStep": 0,
                "description": "This challenge is hard!",
                "length": 50,
                "slug": "this-is-slug",
                "totalSteps": 0
            }
        except:
            return False