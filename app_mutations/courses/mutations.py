import graphene
from app_models.graphql.models import Course
from app_types.types import CourseType

class CourseInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    report = graphene.ID()
    category = graphene.ID()
    cluster = graphene.ID()
    status = graphene.String()
    activeStep = graphene.Int()
    length = graphene.Int()
    totalSteps = graphene.Int()
    slug = graphene.String()

class CreateCourseMutation(graphene.Mutation):
    course = graphene.Field(CourseType)
    class Arguments:
        course_data = CourseInput(required=True)
    def mutate(self, info, course_data=None):
        course = Course(
            title=course_data.title,
            description=course_data.description,
            steps=course_data.steps,
            report=course_data.report,
            category=course_data.category,
            status=course_data.status,
            cluster=course_data.cluster,
            activeStep=course_data.activeStep,
            length=course_data.length,
            totalSteps=course_data.totalSteps,
            slug=course_data.slug,
        )
        course.save()
        return CreateCourseMutation(course=course)

class UpdateCourseMutation(graphene.Mutation):
    course = graphene.Field(CourseType)
    class Arguments:
        course_data = CourseInput(required=True)
    @staticmethod
    def get_object(id):
        return Course.objects.get(pk=id)
    def mutate(self, info, course_data=None):
        course = UpdateCourseMutation.get_object(course_data.id)
        if course_data.title:
            course.title = course_data.title
        if course_data.description:
            course.description = course_data.description
        if course_data.report:
            course.report = course_data.report
        if course_data.category:
            course.category = course_data.category
        if course_data.status:
            course.status = course_data.status
        if course_data.cluster:
            course.cluster = course_data.cluster
        if course_data.activeStep:
            course.activeStep = course_data.activeStep
        if course_data.length:
            course.length = course_data.length
        if course_data.totalSteps:
            course.totalSteps = course_data.totalSteps
        if course_data.slug:
            course.slug = course_data.slug
        course.save()
        return UpdateCourseMutation(course=course)

class DeleteCourseMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    success = graphene.Boolean()
    def mutate(self, info, id):
        try:
            Course.objects.get(pk=id).delete()
            success = True
        except:
            success = False
        return DeleteCourseMutation(success=success)