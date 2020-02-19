from mongoengine import Document
from mongoengine.fields import (
    FloatField,
    StringField,
    ListField,
    URLField,
    ObjectIdField,
    ReferenceField,
    URLField,
    IntField
)
from app_models.graphql.questions.models import Question

class Credential(Document):
    meta = {"collection": "credentials"}
    ID = ObjectIdField()
    username = StringField()
    password = StringField()

class Configuration(Document):
    meta = {"collection": "configurations"}
    ID = ObjectIdField()
    port = IntField()
    url = URLField()
    credentals = ReferenceField(Credential)

class Application(Document):
    meta = {"collection": "applications"}
    ID = ObjectIdField()
    value = StringField()
    configuration = ReferenceField(Configuration)
    questions = ListField(ReferenceField(Question))

class Service(Document):
    meta = {"collection": "services"}
    ID = ObjectIdField()
    value = StringField()
    applications = ListField(ReferenceField(Application))