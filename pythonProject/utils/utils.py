from faker import Faker


def get_random_person():
    fake = Faker('ru_RU')
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'birth_date': fake.date_of_birth(),
        'company': fake.company(),
        'job': fake.job()
    }
    return user
