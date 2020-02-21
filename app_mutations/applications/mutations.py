import graphene
from app_models.graphql.models import Application
from app_types.types import ApplicationType

class ApplicationInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    value = graphene.String()

class CreateApplicationMutation(graphene.Mutation):
    application = graphene.Field(ApplicationType)
    class Arguments:
        application_data = ApplicationInput(required=True)
    def mutate(self, info, application_data=None):
        application = Application(
            value=application_data.value
        )
        application.save()
        return CreateApplicationMutation(application=application)

class UpdateApplicationMutation(graphene.Mutation):
    application = graphene.Field(ApplicationType)
    class Arguments:
        application_data = ApplicationInput(required=True)
    @staticmethod
    def get_object(id):
        return Application.objects.get(pk=id)
    def mutate(self, info, application_data=None):
        application = UpdateApplicationMutation.get_object(application_data.id)
        if application_data.value:
            application.value = application_data.value
        application.save()
        return UpdateApplicationMutation(application=application)

class DeleteApplicationMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    success = graphene.Boolean()
    def mutate(self, info, id):
        try:
            Application.objects.get(pk=id).delete()
            success = True
        except:
            success = False
        return DeleteApplicationMutation(success=success)