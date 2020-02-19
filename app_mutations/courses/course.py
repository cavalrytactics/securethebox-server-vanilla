import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from app_models.graphql.course import Course as CourseModel
from app_models.graphql.category import Category as CategoryModel
from app_models.graphql.application import Application as ApplicationModel
from app_models.graphql.service import Service as ServiceModel
# from app_models.graphql.step import Step as StepModel

class Course(MongoengineObjectType):
    class Meta:
        model = CourseModel
        interfaces = (Node,)

class Category(MongoengineObjectType):
    class Meta:
        model = CategoryModel
        interfaces = (Node,)

class Application(MongoengineObjectType):
    class Meta:
        model = ApplicationModel
        interfaces = (Node,)

class Service(MongoengineObjectType):
    class Meta:
        model = ServiceModel
        interfaces = (Node,)

# class Step(MongoengineObjectType):
#     class Meta:
#         model = StepModel
#         interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    all_courses = MongoengineConnectionField(Course)
    all_categories = MongoengineConnectionField(Category)
    all_applications = MongoengineConnectionField(Application)
    all_services = MongoengineConnectionField(Service)
    # course = graphene.Field(Course)
    # category = graphene.Field(Category)
    # course = graphene.Field(Course)

schema = graphene.Schema(query=Query)

# class Role(MongoengineObjectType):
#     class Meta:
#         model = RoleModel
#         interfaces = (Node,)

# class Topic(MongoengineObjectType):
#     class Meta:
#         model = TopicModel
#         interfaces = (Node,)



# class CreateCourse(graphene.Mutation):
#     class Arguments:
#         title = graphene.String()
#         activeStep = graphene.Int()
#         description = graphene.String()
#         length = graphene.Int()
#         slug = graphene.String()
#         # steps = graphene.List()
#         totalSteps = graphene.Int()
#     course = graphene.Field(lambda: Course)

#     def mutate(root, info, title, activeStep, description, length, slug, totalSteps): 
#         course = Course(title=title, activeStep=activeStep, description=description, length=length, slug=slug, totalSteps=totalSteps)
#         return CreateCourse(course=course)

# # Mutation Class
# class CCourse(graphene.ObjectType):
#     title = graphene.String()
#     activeStep = graphene.Int()
#     description = graphene.String()
#     length = graphene.Int()
#     slug = graphene.String()
#     # steps = ListField(EmbeddedDocumentField(Step))
#     totalSteps = graphene.Int()

# class CourseMutations(graphene.ObjectType):
#     create_course = CreateCourse.Field()


# schema = graphene.Schema(query=Query, types=[Category, Course])
