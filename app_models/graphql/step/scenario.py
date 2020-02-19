from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ReferenceField,
    ListField,
)
from app_models.graphql.application import Application

class Scenario(Document):
    meta = {"collection": "scenario"}
    title = StringField()
    content = StringField()
    applications = ListField(ReferenceField(Application))