from graphene import relay
from graphene_mongo import MongoengineObjectType
from app_models.graphql.services.models import Service, Application, Configuration, Credential

class ServiceType(MongoengineObjectType):
    class Meta:
        model = Service
        interfaces = (relay.Node,)

class ApplicationType(MongoengineObjectType):
    class Meta:
        model = Application
        interfaces = (relay.Node,)

class ConfigurationType(MongoengineObjectType):
    class Meta:
        model = Configuration
        interfaces = (relay.Node,)

class CredentialType(MongoengineObjectType):
    class Meta:
        model = Credential
        interfaces = (relay.Node,)