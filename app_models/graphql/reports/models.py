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

class Report(Document):
    meta = {"collection": "reports"}
    ID = ObjectIdField()
    score = IntField()
