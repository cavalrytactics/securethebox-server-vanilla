from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ReferenceField,
    ListField
)

class Submission(Document):
    meta = {"collection": "submission"}
    title = StringField()
    content = StringField()
    questions = ListField(ReferenceField(Question))