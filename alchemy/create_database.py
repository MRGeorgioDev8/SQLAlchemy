from models.database import create_db, Session
from models.people import People
from models.special import Special
from faker import Faker

def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())

def _load_fake_data(session):
    faker = Faker('ru_Ru')

    special_titles = ['Инженер', 'Программист', 'Дизайнер', 'Аналитик', 'Архитектор']
    for title in special_titles:
        special = Special(special_title=title)
        session.add(special)

    session.commit()

    for _ in range(50):
        full_name = faker.name().split()
        age = faker.random.randint(16, 25)
        random_special_id = faker.random.randint(1, 6)
        person = People(full_name, age, random_special_id)
        session.add(person)

    session.commit()
    session.close()