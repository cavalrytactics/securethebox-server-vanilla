from mongoengine import Document
from mongoengine.fields import (
    StringField,
)

class Category(Document):
    meta = {"collection": "categories"}
    value = StringField()
    label = StringField()
    color = StringField()