import graphene
from app_models.graphql.models import Service, Application
from app_types.types import ServiceType, ApplicationType
from app_mutations.applications.mutations import ApplicationInput

class ServiceInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    value = graphene.String()

class CreateServiceMutation(graphene.Mutation):
    service = graphene.Field(ServiceType)
    application = graphene.Field(ApplicationType)
    class Arguments:
        service_data = ServiceInput(required=True)
        application_data = ApplicationInput(required=False)
    def mutate(self, info, service_data=None, application_data=None):
        application = Application(
                value=application_data.value
        )
        application.save()
        service = Service(
            value=service_data.value,
            applications=[application]
        )
        
        service.save()
        return CreateServiceMutation(service=service)

class UpdateServiceMutation(graphene.Mutation):
    service = graphene.Field(ServiceType)
    application = graphene.Field(ApplicationType)
    class Arguments:
        service_data = ServiceInput(required=True)
        application_data = ApplicationInput(required=False)
    @staticmethod
    def get_service_object(id):
        return Service.objects.get(pk=id)
    def mutate(self, info, service_data=None, application_data=None):
        service = UpdateServiceMutation.get_service_object(service_data.id)
        if service_data.value:
            service.value = service_data.value
        service.save()
        return UpdateServiceMutation(service=service)

class UpdateServiceAddApplicationMutation(graphene.Mutation):
    service = graphene.Field(ServiceType)
    application = graphene.Field(ApplicationType)
    class Arguments:
        service_data = ServiceInput(required=True)
        application_data = ApplicationInput(required=False)
    @staticmethod
    def get_service_object(id):
        return Service.objects.get(pk=id)
    def get_application_object(id):
        return Application.objects.get(pk=id)
    def mutate(self, info, service_data=None, application_data=None):
        service = UpdateServiceAddApplicationMutation.get_service_object(service_data.id)
        application = UpdateServiceAddApplicationMutation.get_application_object(application_data.id)
        if service_data.value:
            service.value = service_data.value
        if application_data.value:
            if application not in service.applications:
                service.applications.append(application)
        service.save()
        return UpdateServiceAddApplicationMutation(service=service)

class UpdateServiceDeleteApplicationMutation(graphene.Mutation):
    service = graphene.Field(ServiceType)
    application = graphene.Field(ApplicationType)
    class Arguments:
        service_data = ServiceInput(required=True)
        application_data = ApplicationInput(required=False)
    @staticmethod
    def get_service_object(id):
        return Service.objects.get(pk=id)
    def get_application_object(id):
        return Application.objects.get(pk=id)
    def mutate(self, info, service_data=None, application_data=None):
        service = UpdateServiceDeleteApplicationMutation.get_service_object(service_data.id)
        application = UpdateServiceDeleteApplicationMutation.get_application_object(application_data.id)
        if service_data.value:
            service.value = service_data.value
        if application_data.value:
            if application in service.applications:
                service.applications.remove(application)
        service.save()
        return UpdateServiceAddApplicationMutation(service=service)

class DeleteServiceMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    success = graphene.Boolean()
    def mutate(self, info, id):
        try:
            Service.objects.get(pk=id).delete()
            success = True
        except:
            success = False
        return DeleteServiceMutation(success=success)