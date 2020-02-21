from mongoengine import Document
from mongoengine.fields import (
    FloatField,
    StringField,
    ListField,
    URLField,
    ObjectIdField,
    ReferenceField,
    BooleanField,
    EmailField,
    IntField,
    DateTimeField,
    FloatField,
)

class Subscription(Document):
    meta = {"collection": "subscriptions"}
    stripeCustomerPlan = StringField()
    stripeCustomerId = StringField()
    stripeCustomerSubscriptionId = StringField()
    active = BooleanField()

class Job(Document):
    meta = {"collection": "jobs"}
    description = StringField()
    minimumRank = IntField()
    responsibilities = StringField()
    qualifications = StringField()
    applyLink = URLField()
    applyEmail = EmailField()
    payRange = StringField()
    qualified = ListField(ReferenceField(User))

class Company(Document):
    meta = {"collection": "companies"}
    managers = ListField(ReferenceField(User))
    jobs = ListField(ReferenceField(Job))

class Rank(Document):
    meta = {"collection": "ranks"}
    coursesComplete = IntField()
    flagsObtained = IntField()
    position = IntField()

class University(Document):
    meta = {"collection": "universities"}
    team = ReferenceField(Team)
    domain = StringField()
    
class Team(Document):
    meta = {"collection": "teams"}
    members = ListField(ReferenceField(User))

class User(Document):
    meta = {"collection": "users"}
    manager = BooleanField()
    email = EmailField()
    level = IntField()
    rank = ReferenceField(Rank)
    subscription = ReferenceField(Subscription)
    admin = BooleanField()
    recruiter = BooleanField()
    team = ReferenceField(Team)
    courses = ListField(ReferenceField(Course))
    loggedIn = BooleanField()

class Credential(Document):
    meta = {"collection": "credentials"}
    ID = ObjectIdField()
    username = StringField()
    password = StringField()
    publicKey = StringField()
    privateKey = StringField()

class Configuration(Document):
    meta = {"collection": "configurations"}
    ID = ObjectIdField()
    port = IntField()
    url = URLField()
    credentals = ReferenceField(Credential)

class Competency(Document):
    meta = {"collection": "competencies"}
    ID = ObjectIdField()
    value = StringField()

class Topic(Document):
    meta = {"collection": "topics"}
    ID = ObjectIdField()
    competency = ReferenceField(Competency)
    value = StringField()

class Scope(Document):
    meta = {"collection": "scopes"}
    ID = ObjectIdField()
    topic = ReferenceField(Topic)
    value = StringField()

class Solution(Document):
    meta = {"collection": "solutions"}
    ID = ObjectIdField()    
    value = StringField()

class Question(Document):
    meta = {"collection": "questions"}
    ID = ObjectIdField()
    solutions = ReferenceField(Solution)
    scope = ReferenceField(Scope)
    attempts = IntField()
    value = StringField()

class Dummy(Document):
    meta = {"collection": "dummies"}
    ID = ObjectIdField()
    intent = StringField()
    purchases = IntField()
    active = BooleanField()

class Application(Document):
    meta = {"collection": "applications"}
    ID = ObjectIdField()
    value = StringField()
    status = StringField()
    configuration = ReferenceField(Configuration)
    questions = ListField(ReferenceField(Question))
    dummies = ListField(ReferenceField(Dummy))

class Metric(Document):
    meta = {"collection": "metrics"}
    ID = ObjectIdField()
    uptime = DateTimeField()
    downtime = DateTimeField()
    activeUsers = IntField()
    purchases = IntField()
    revenue = FloatField()

class Service(Document):
    meta = {"collection": "services"}
    ID = ObjectIdField()
    value = StringField()
    applications = ListField(ReferenceField(Application))

class Report(Document):
    meta = {"collection": "reports"}
    ID = ObjectIdField()
    score = IntField()

class Category(Document):
    meta = {"collection": "categories"}
    ID = ObjectIdField()
    value = StringField()
    label = StringField()
    color = StringField()
    
class Container(Document):
    meta = {"collection": "containers"}
    ID = ObjectIdField()
    services = ListField(ReferenceField(Service))
    status = StringField() 

class Cluster(Document):
    meta = {"collection": "clusters"}
    ID = ObjectIdField()
    name = StringField()
    status = StringField()
    containers = ListField(ReferenceField(Container))

class Container(Document):
    meta = {"collection": "steps"}
    ID = ObjectIdField()
    title = StringField()
    content = StringField()

class Course(Document):
    meta = {"collection": "courses"}
    ID = ObjectIdField()
    activeStep = IntField()
    description = StringField()
    length = IntField()
    slug = StringField()
    title = StringField()
    totalSteps = IntField()
    category = ReferenceField(Category)
    report = ReferenceField(Report)
    cluster = ReferenceField(Cluster)
    steps = ListField(ReferenceField(Step))
    status = StringField()