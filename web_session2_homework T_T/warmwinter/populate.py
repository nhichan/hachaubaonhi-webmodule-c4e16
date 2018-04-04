from models.service import Service
import mlab
from faker import Faker
from random import randint, choice
mlab.connect()

fake = Faker()
#name va yob cac kieu chung la 1 oject
for i in range(100):
    print('Saving service',i+1,"...")
    new_service = Service(
                name = fake.name(),
                yob =randint(1995,2000),
                gender = choice([0,1]),
                height = randint(150,180),
                phone = fake.phone_number(),
                address = fake.address(),
                status = choice([True, False])
    )
    #creat a document
    new_service.save()

print(fake.address())
