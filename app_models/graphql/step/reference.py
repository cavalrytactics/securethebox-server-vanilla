from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ReferenceField
)

class Reference(Document):
    meta = {"collection": "reference"}
    url = StringField()
    description = StringField()