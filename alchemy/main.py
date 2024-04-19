import os
from models.database import DATABASE_NAME, Session, Base
import create_database as db_creator

from models.people import People
from models.special import Special
from sqlalchemy import and_, or_, not_, desc

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

    for it in session.query(People):
        print(it)
    print(60 * '*')

    print(session.query(People).count(), 'персон')
    print(60 * '*')

    for person in (session.query(People).join(People.special) .filter(Special.special_title == 'Программист').all()):
        print(person)
    print(60 * '*')

    print(session.query(People).filter(People.age.between(16, 17)).all())
    print(60 * '*')

    for it in session.query(People).order_by(desc(People.surname)):
        print(it)
    print(60 * '*')

    session.add(Special(special_title="Инвестор"))
    session.commit()