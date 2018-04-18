from mongoengine import*


class User(Document):
    fullname = StringField(required=True)
    email = EmailField(required=True)
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
