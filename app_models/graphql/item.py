
class Item(Document):
    meta = {"collection": "items"}
    value = StringField()
    label = StringField()