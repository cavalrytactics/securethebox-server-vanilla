from graphene import relay
from graphene_mongo import MongoengineObjectType
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
    User)

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
class CategoryType(MongoengineObjectType):
	class Meta:
		model = Category
		interfaces = (relay.Node,)
class CompetencyType(MongoengineObjectType):
	class Meta:
		model = Competency
		interfaces = (relay.Node,)
class CourseType(MongoengineObjectType):
	class Meta:
		model = Course
		interfaces = (relay.Node,)
class QuestionType(MongoengineObjectType):
	class Meta:
		model = Question
		interfaces = (relay.Node,)
class ReportType(MongoengineObjectType):
	class Meta:
		model = Report
		interfaces = (relay.Node,)
class ScopeType(MongoengineObjectType):
	class Meta:
		model = Scope
		interfaces = (relay.Node,)
class ServiceType(MongoengineObjectType):
	class Meta:
		model = Service
		interfaces = (relay.Node,)
class SolutionType(MongoengineObjectType):
	class Meta:
		model = Solution
		interfaces = (relay.Node,)
class SubscriptionType(MongoengineObjectType):
	class Meta:
		model = Subscription
		interfaces = (relay.Node,)
class TopicType(MongoengineObjectType):
	class Meta:
		model = Topic
		interfaces = (relay.Node,)
class UserType(MongoengineObjectType):
	class Meta:
		model = User
		interfaces = (relay.Node,)