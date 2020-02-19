from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ReferenceField
)
from app_models.graphql.application import Application

class Service(Document):
    meta = {"collection": "services"}
    value = StringField()
    label = StringField()
    application = ReferenceField(Application)