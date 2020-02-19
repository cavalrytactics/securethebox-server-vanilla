from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ListField,
    ReferenceField,
    StringField
)
from app_models.graphql.category import Category

class Step(EmbeddedDocument):
    meta = {"collection": "steps"}
    label = StringField()
    value = StringField()
    component = StringField() # textfull, select
    componentTextType = StringField() # only for textfull
    componentSelectItems = ListField(ReferenceField(Category))
