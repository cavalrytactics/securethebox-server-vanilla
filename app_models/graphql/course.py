from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField,
    EmbeddedDocumentField,
    ListField,
    ReferenceField,
    StringField,
    IntField,
    DictField,
)
# from app_models.graphql.step import Step

class Course(Document):
    meta = {"collection": "courses"}
    activeStep = IntField()
    description = StringField()
    length = IntField()
    slug = StringField()
    # steps = ListField(EmbeddedDocumentField(Step))
    title = StringField()
    totalSteps = IntField()