from mongoengine import Document
from mongoengine.fields import (
    FloatField,
    StringField,
    ListField,
    URLField,
    ObjectIdField,
    ReferenceField
)

class Course(Document):
    meta = {"collection": "courses"}
    ID = ObjectIdField()
    activeStep = IntField()
    description = StringField()
    length = IntField()
    slug = StringField()
    # steps = ListField(EmbeddedDocumentField(Step))
    title = StringField()
    totalSteps = IntField()
    category = ReferenceField(Category)

class Category(Document):
    meta = {"collection": "categories"}
    ID = ObjectIdField()
    value = StringField()
    label = StringField()
    color = StringField()