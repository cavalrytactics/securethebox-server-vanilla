from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ReferenceField
)

class Start(Document):
    meta = {"collection": "start"}
    title = StringField()
    content = StringField()