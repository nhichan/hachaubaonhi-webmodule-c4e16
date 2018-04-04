from mongoengine import *

host = "ds121588.mlab.com"
port = 21588
db_name = "mua_dong_khong_lanh"
user_name = "johnprice"
password = "johnprice"


class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

connect(db_name, host=host, port=port, username=user_name, password=password)


print(Service.objects.first().delete())
