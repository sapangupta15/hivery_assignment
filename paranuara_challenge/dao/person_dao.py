import os
import json
from sqlalchemy import func
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from paranuara_challenge.dao import resource_path
from paranuara_challenge.services.mapper.person_mapper import map_person_attributes
from paranuara_challenge.models.db.person import Person
from paranuara_challenge.services.db.session_manager import session_manager
from paranuara_challenge.utils.person_utils import get_friends_by_person
from paranuara_challenge.exceptions.ProcessingException import ProcessingException


@session_manager
def add_persons(session):
    with open(os.path.join(resource_path, 'people.json'), 'r') as people_file:
        people_data = json.loads(people_file.read())
    persons = [map_person_attributes(**data)for data in people_data]

    person_by_person_id = {person.person_id: person for person in persons}
    person_friend_ids = get_friends_by_person(people_data)
    for person in persons:
        friend_ids = person_friend_ids.get(person.person_id, [])
        for friend_id in friend_ids:
            friend = person_by_person_id[friend_id]
            person.add_friend(friend)
    session.add_all(persons)


@session_manager
def get_person_by_name(session, name, fetch_friends=False):
    try:
        person = session.query(Person).filter(func.lower(Person.name) == name.lower()).one()
        if fetch_friends:
            friends = person.friends
        return person
    except MultipleResultsFound:
        raise ProcessingException(f'more than 1 result exists for name: {name}')
    except NoResultFound:
        raise ProcessingException(f'more than 1 result exists for name: {name}')
    except Exception as e:
        raise ProcessingException(f'Error has occurred, message: {e.message}')


@session_manager
def get_persons_by_company_id(session, company_id):
    try:
        persons = session.query(Person).filter(Person.company_id == company_id).all()
        return persons
    except Exception as e:
        raise ProcessingException(f'Error has occurred, message: {e.message}')
