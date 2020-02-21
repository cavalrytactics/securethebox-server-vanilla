import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
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
from app_types.types import (
    ApplicationType,
    ConfigurationType,
    CredentialType,
    CategoryType,
    CompetencyType,
    CourseType,
    QuestionType,
    ReportType,
    ScopeType,
    ServiceType,
    SolutionType,
    SubscriptionType,
    TopicType,
    UserType,
)

from app_mutations.applications.mutations import (
    CreateApplicationMutation,
    UpdateApplicationMutation,
    DeleteApplicationMutation,
)
from app_mutations.categories.mutations import (
    CreateCategoryMutation,
    UpdateCategoryMutation,
    DeleteCategoryMutation,
)
from app_mutations.categories.mutations import (
    CreateCategoryMutation,
    UpdateCategoryMutation,
    DeleteCategoryMutation,
)
from app_mutations.competencies.mutations import (
    CreateCompetencyMutation,
    UpdateCompetencyMutation,
    DeleteCompetencyMutation,
)
from app_mutations.configurations.mutations import (
    CreateConfigurationMutation,
    UpdateConfigurationMutation,
    DeleteConfigurationMutation,
)
from app_mutations.courses.mutations import (
    CreateCourseMutation,
    UpdateCourseMutation,
    DeleteCourseMutation,
)
from app_mutations.credentials.mutations import (
    CreateCredentialMutation,
    UpdateCredentialMutation,
    DeleteCredentialMutation,
)
from app_mutations.questions.mutations import (
    CreateQuestionMutation,
    UpdateQuestionMutation,
    DeleteQuestionMutation,
)
from app_mutations.reports.mutations import (
    CreateReportMutation,
    UpdateReportMutation,
    DeleteReportMutation,
)
from app_mutations.scopes.mutations import (
    CreateScopeMutation,
    UpdateScopeMutation,
    DeleteScopeMutation,
)
from app_mutations.services.mutations import (
    CreateServiceMutation, 
    UpdateServiceMutation,
    DeleteServiceMutation,
    UpdateServiceAddApplicationMutation,
    UpdateServiceDeleteApplicationMutation
)
from app_mutations.solutions.mutations import (
    CreateSolutionMutation,
    UpdateSolutionMutation,
    DeleteSolutionMutation,
)
from app_mutations.subscriptions.mutations import (
    CreateSubscriptionMutation,
    UpdateSubscriptionMutation,
    DeleteSubscriptionMutation,
)
from app_mutations.topics.mutations import (
    CreateTopicMutation,
    UpdateTopicMutation,
    DeleteTopicMutation,
)
from app_mutations.users.mutations import (
    CreateUserMutation,
    UpdateUserMutation,
    DeleteUserMutation,
)

class Mutations(graphene.ObjectType):
    create_application = CreateApplicationMutation.Field()
    update_application = UpdateApplicationMutation.Field()
    delete_application = DeleteApplicationMutation.Field()
    create_category = CreateCategoryMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()
    create_competency = CreateCompetencyMutation.Field()
    update_competency = UpdateCompetencyMutation.Field()
    delete_competency = DeleteCompetencyMutation.Field()
    create_configuration = CreateConfigurationMutation.Field()
    update_configuration = UpdateConfigurationMutation.Field()
    delete_configuration = DeleteConfigurationMutation.Field()
    create_course = CreateCourseMutation.Field()
    update_course = UpdateCourseMutation.Field()
    delete_course = DeleteCourseMutation.Field()
    create_credential = CreateCredentialMutation.Field()
    update_credential = UpdateCredentialMutation.Field()
    delete_credential = DeleteCredentialMutation.Field()
    create_question = CreateQuestionMutation.Field()
    update_question = UpdateQuestionMutation.Field()
    delete_question = DeleteQuestionMutation.Field()
    create_report = CreateReportMutation.Field()
    update_report = UpdateReportMutation.Field()
    delete_report = DeleteReportMutation.Field()
    create_scope = CreateScopeMutation.Field()
    update_scope = UpdateScopeMutation.Field()
    delete_scope = DeleteScopeMutation.Field()
    create_service= CreateServiceMutation.Field()
    update_service = UpdateServiceMutation.Field()
    delete_service = DeleteServiceMutation.Field()
    update_service_add_application = UpdateServiceAddApplicationMutation.Field()
    update_service_delete_application = UpdateServiceDeleteApplicationMutation.Field()
    create_solution = CreateSolutionMutation.Field()
    update_solution = UpdateSolutionMutation.Field()
    delete_solution = DeleteSolutionMutation.Field()
    create_subscription = CreateSubscriptionMutation.Field()
    update_subscription = UpdateSubscriptionMutation.Field()
    delete_subscription = DeleteSubscriptionMutation.Field()
    create_topic = CreateTopicMutation.Field()
    update_topic = UpdateTopicMutation.Field()
    delete_topic = DeleteTopicMutation.Field()
    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()
    delete_user = DeleteUserMutation.Field()

class Query(graphene.ObjectType):
    node = Node.Field()

    applications = MongoengineConnectionField(ApplicationType)
    configurations = MongoengineConnectionField(ConfigurationType)
    credentials = MongoengineConnectionField(CredentialType)
    categories = MongoengineConnectionField(CategoryType)
    competencies = MongoengineConnectionField(CompetencyType)
    courses = MongoengineConnectionField(CourseType)
    questions = MongoengineConnectionField(QuestionType)
    reports = MongoengineConnectionField(ReportType)
    scopes = MongoengineConnectionField(ScopeType)
    services = MongoengineConnectionField(ServiceType)
    solutions = MongoengineConnectionField(SolutionType)
    subscriptions = MongoengineConnectionField(SubscriptionType)
    topics = MongoengineConnectionField(TopicType)
    users = MongoengineConnectionField(UserType)

    applications_list = graphene.List(ApplicationType)
    configurations_list = graphene.List(ConfigurationType)
    credentials_list = graphene.List(CredentialType)
    categories_list = graphene.List(CategoryType)
    competencies_list = graphene.List(CompetencyType)
    courses_list = graphene.List(CourseType)
    questions_list = graphene.List(QuestionType)
    reports_list = graphene.List(ReportType)
    scopes_list = graphene.List(ScopeType)
    services_list = graphene.List(ServiceType)
    solutions_list = graphene.List(SolutionType)
    subscriptions_list = graphene.List(SubscriptionType)
    topics_list = graphene.List(TopicType)
    users_list = graphene.List(UserType)
    
    def resolve_applications_list(self, info):
        return Applications.objects.all()
    def resolve_configurations_list(self, info):
        return Configurations.objects.all()
    def resolve_credentials_list(self, info):
        return Credentials.objects.all()
    def resolve_categories_list(self, info):
        return Categories.objects.all()
    def resolve_competencies_list(self, info):
        return Competencies.objects.all()
    def resolve_courses_list(self, info):
        return Courses.objects.all()
    def resolve_questions_list(self, info):
        return Questions.objects.all()
    def resolve_reports_list(self, info):
        return Reports.objects.all()
    def resolve_scopes_list(self, info):
        return Scopes.objects.all()
    def resolve_services_list(self, info):
        return Services.objects.all()
    def resolve_solutions_list(self, info):
        return Solutions.objects.all()
    def resolve_subscriptions_list(self, info):
        return Subscriptions.objects.all()
    def resolve_topics_list(self, info):
        return Topics.objects.all()
    def resolve_users_list(self, info):
        return Users.objects.all()

schema = graphene.Schema(
    query=Query, 
    mutation=Mutations, 
    types=[
        ApplicationType,
        ConfigurationType,
        CredentialType,
        CategoryType,
        CompetencyType,
        CourseType,
        QuestionType,
        ReportType,
        ScopeType,
        ServiceType,
        SolutionType,
        SubscriptionType,
        TopicType,
        UserType,
        ]
    )