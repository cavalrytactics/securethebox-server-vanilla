from mongoengine import Document
from mongoengine.fields import (
    FloatField,
    StringField,
    ListField,
    URLField,
    ObjectIdField,
    ReferenceField,
    IntField
)

class Competency(Document):
    meta = {"collection": "competencies"}
    ID = ObjectIdField()
    value = StringField()

class Topic(Document):
    meta = {"collection": "topics"}
    ID = ObjectIdField()
    competency = ReferenceField(Competency)
    value = StringField()

class Scope(Document):
    meta = {"collection": "scopes"}
    ID = ObjectIdField()
    topic = ReferenceField(Topic)
    value = StringField()

class Solution(Document):
    meta = {"collection": "solutions"}
    ID = ObjectIdField()    
    value = StringField()

class Question(Document):
    meta = {"collection": "questions"}
    ID = ObjectIdField()
    solutions = ReferenceField(Solution)
    scope = ReferenceField(Scope)
    attempts = IntField()
    value = StringField()