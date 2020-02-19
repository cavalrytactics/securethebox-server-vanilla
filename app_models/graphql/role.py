class Role(Document):
    meta = {"collection": "roles"}
    value = StringField(unique=True)
    label = StringField(unique=True)