import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from app_models.graphql.services.models import Service, Application, Configuration, Credential
from app_types.services.types import ServiceType, ApplicationType, ConfigurationType, CredentialType
from app_mutations.services.mutations import (
    CreateApplicationMutation,
    UpdateApplicationMutation,
    DeleteApplicationMutation, 
    CreateServiceMutation, 
    UpdateServiceMutation,
    UpdateServiceAddApplicationMutation,
    UpdateServiceDeleteApplicationMutation,
    DeleteServiceMutation)

class Mutations(graphene.ObjectType):
    create_service = CreateServiceMutation.Field()
    update_service = UpdateServiceMutation.Field()
    delete_service = DeleteServiceMutation.Field()
    update_service_add_application = UpdateServiceAddApplicationMutation.Field()
    update_service_delete_application = UpdateServiceDeleteApplicationMutation.Field()
    create_application = CreateApplicationMutation.Field()
    update_application = UpdateApplicationMutation.Field()
    delete_application = DeleteApplicationMutation.Field()

class Query(graphene.ObjectType):
    node = Node.Field()
    services = MongoengineConnectionField(ServiceType)
    applications = MongoengineConnectionField(ApplicationType)
    configurations = MongoengineConnectionField(ConfigurationType)
    credentials = MongoengineConnectionField(CredentialType)
    service_list = graphene.List(ServiceType)
    application_list = graphene.List(ApplicationType)
    configuration_list = graphene.List(ConfigurationType)
    credential_list = graphene.List(CredentialType)
    def resolve_service_list(self, info):
        return Service.objects.all()
    def resolve_application_list(self, info):
        return Application.objects.all()
    def resolve_configuration_list(self, info):
        return Configuration.objects.all()
    def resolve_credential_list(self, info):
        return Credential.objects.all()

schema = graphene.Schema(
    query=Query, 
    mutation=Mutations, 
    types=[
        ServiceType, 
        ApplicationType, 
        ConfigurationType, 
        CredentialType
        ]
    )