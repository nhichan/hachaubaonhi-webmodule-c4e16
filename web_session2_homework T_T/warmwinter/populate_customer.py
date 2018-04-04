from models.customer import Customer
import mlab
from faker import Faker
from random import randint, choice
mlab.connect()

fake = Faker()
for i in range(100):
    print('Saving customer',i+1,"...")
    gender = choice([0,1])
    name = fake.name_male() if gender==1 else fake.name_female()
    new_customer = Customer(
                name = name,
                gender = gender,
                email = fake.safe_email(),
                phone = fake.phone_number(),
                job = fake.job(),
                company = fake.company(),
                contacted = choice([True, False])
    )
    #creat a document
    new_customer.save()

