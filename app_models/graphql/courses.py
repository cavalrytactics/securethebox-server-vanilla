from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField,
    EmbeddedDocumentField,
    ListField,
    ReferenceField,
    StringField,
    IntField,
    DictField,
)

class Category(Document):
    meta = {"collection": "category"}
    value = StringField()
    label = StringField()
    color = StringField()

class Topic(Document):
    meta = {"collection": "topic"}
    value = StringField(unique=True)
    label = StringField(unique=True)

class Role(Document):
    meta = {"collection": "role"}
    value = StringField(unique=True)
    label = StringField(unique=True)

class Step(EmbeddedDocument):
    meta = {"collection": "step"}
    title = StringField()
    content = StringField()

class Course(Document):
    meta = {"collection": "course"}
    activeStep = IntField()
    description = StringField()
    length = IntField()
    slug = StringField()
    # steps = ListField(EmbeddedDocumentField(Step))
    title = StringField()
    totalSteps = IntField()
    # created_on = DateTimeField(default=datetime.now)
    category = ReferenceField(Category)
    # role = ReferenceField(Role)
    # topics = ListField(ReferenceField(Topic))
    # challenge = ReferenceField("Course")