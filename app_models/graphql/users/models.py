from mongoengine import Document
from mongoengine.fields import (
    FloatField,
    StringField,
    ListField,
    URLField,
    ObjectIdField,
    ReferenceField,
    BooleanField,
    EmailField,
    IntField,
)

class User(Document):
    meta = {"collection": "users"}
    manager = BooleanField()
    email = EmailField()
    level = IntField()
    rank = IntField()
    subscription = ReferenceField(Subscription)

class Subscription(Document):
    meta = {"collection": "subscriptions"}
    stripeCustomerPlan = StringField()
    stripeCustomerId = StringField()
    stripeCustomerSubscriptionId = StringField()
    active = BooleanField()