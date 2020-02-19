from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ReferenceField,
    ListField,
)
from app_models.graphql.step.reference import Reference

class Resource(Document):
    meta = {"collection": "resource"}
    title = StringField()
    content = StringField()
    references = ListField(ReferenceField(Reference)) 