from mongoengine import*
import datetime

class Order(Document):
    userid = StringField(required=True)
    serviceid = StringField(required=True)
    time = DateTimeField(required=True, default=datetime.datetime.now)
    is_accepted = BooleanField(required=True)
