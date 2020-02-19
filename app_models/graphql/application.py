from mongoengine import Document
from mongoengine.fields import (
    StringField,
)

class Application(Document):
    meta = {"collection": "applications"}
    value = StringField()
    label = StringField()