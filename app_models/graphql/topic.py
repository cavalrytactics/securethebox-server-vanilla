class Topic(Document):
    meta = {"collection": "topics"}
    value = StringField(unique=True)
    label = StringField(unique=True)