from mongoengine import Document
from mongoengine.fields import (
    StringField,
    ReferenceField
)

class Overview(Document):
    meta = {"collection": "overview"}
    title = StringField()
    content = StringField()