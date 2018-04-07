from mongoengine import*


#tạo collection
#design database
class Service(Document): #trong các document có các cặp key value lần lượt là
    name = StringField() #là 1 field thuộc kiểu string
    yob = IntField()
    gender = IntField() #0: female, 1: female
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = URLField()
    description = StringField()
    measurements = ListField(IntField())
