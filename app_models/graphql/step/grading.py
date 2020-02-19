from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ReferenceField
)

class Grading(Document):
    meta = {"collection": "grading"}
    title = StringField()
    content = StringField()
    role = StringField()