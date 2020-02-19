from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ReferenceField
)

class Scoring(Document):
    meta = {"collection": "scoring"}
    title = StringField()
    content = StringField()