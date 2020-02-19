import graphene
from app_models.graphql.services.models import Service
from app_types.services.types import ServiceType

class ServiceInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    value = graphene.String()

class CreateServiceMutation(graphene.Mutation):
    service = graphene.Field(ServiceType)
    class Arguments:
        service_data = ServiceInput(required=True)
    def mutate(self, info, service_data=None):
        service = Service(
            name=service_data.name,
            value=service_data.value
        )
        service.save()
        return CreateServiceMutation(service=service)

class UpdateServiceMutation(graphene.Mutation):
    service = graphene.Field(ServiceType)
    class Arguments:
        service_data = ServiceInput(required=True)
    @staticmethod
    def get_object(id):
        return Service.objects.get(pk=id)
    def mutate(self, info, service_data=None):
        service = UpdateServiceMutation.get_object(service_data.id)
        if service_data.name:
            service.name = service_data.name
        if service_data.value:
            service.value = service_data.value
        service.save()
        return UpdateServiceMutation(service=service)

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