from models.service import Service
import mlab
from faker import Faker
from random import randint, choice
mlab.connect()

fake = Faker()

for i in range(100):
    print('Saving service',i+1,"...")
    gender = choice([0, 1])
    name = fake.name_male() if gender==1 else fake.name_female()
    new_service = Service(
                name = name,
                yob =randint(1995,2000),
                gender = gender,
                height = randint(150,180),
                phone = fake.phone_number(),
                address = fake.address(),
                status = choice([True, False]),
                description = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
                measurements = [randint(60, 100), randint(60, 100), randint(60, 100)],
                image = 'http://lorempixel.com/300/200/cats'
    )

    new_service.save()

print(fake.address())
