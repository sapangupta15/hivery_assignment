import json
from unittest.mock import patch, call
from sqlalchemy.orm.session import Session

from paranuara_challenge.services.people_service import get_details_for_two_people, get_details_for_single_person
from paranuara_challenge.models.db.person import Person


@patch('paranuara_challenge.services.people_service.get_alive_common_friends_with_brown_eyes')
@patch('paranuara_challenge.services.people_service.get_person_by_name')
def test_get_details_for_two_people_returns_people_and_mutual_friend_details(mock_person_by_name_dao,
                                                                             mock_mutual_friends):
    person1 = Person(person_id=1, name='abc', age=40, address='abc', phone='abc',
                     friends=[Person(person_id=10, name='pqr')])
    person2 = Person(person_id=2, name='xyz', age=50, address='abc', phone='abc',
                     friends=[Person(person_id=10, name='pqr')])
    mock_person_by_name_dao.side_effect = [person1, person2]
    mock_mutual_friends.return_value = []

    session = Session()

    expected_response = {
        'first_person': {
            'name': person1.name,
            'age': person1.age,
            'address': person1.address,
            'phone': person1.phone
        },
        'second_person': {
            'name': person2.name,
            'age': person2.age,
            'address': person2.address,
            'phone': person2.phone
        },
        'mutual_friends': []
    }

    people_friend_details_response = get_details_for_two_people(session, name1=person1.name, name2=person2.name)
    assert people_friend_details_response == json.dumps(expected_response)

    calls = [call(session, name=person1.name, fetch_friends=True), call(session, name=person2.name, fetch_friends=True)]
    assert mock_person_by_name_dao.call_count == 2
    mock_person_by_name_dao.assert_has_calls(calls)
    mock_mutual_friends.assert_called_once()


@patch('paranuara_challenge.services.people_service.get_food_as_fruits_and_vegetables')
@patch('paranuara_challenge.services.people_service.get_person_by_name')
def test_get_details_for_single_person_returns_person_details_and_fruits_vegetables(mock_person_by_name_dao,
                                                                                    mock_fruits_and_vegetables):
    person = Person(person_id=1, name='abc', age=40, favourite_food=['carrot', 'orange'])
    mock_person_by_name_dao.return_value = person
    mock_fruits_and_vegetables.return_value = {'fruits': ['orange'], 'vegetables': ['carrot']}

    session = Session()

    expected_response = {
        'username': person.name,
        'age': person.age,
        'fruits': ['orange'],
        'vegetables': ['carrot']
    }

    single_person_details = get_details_for_single_person(session, name=person.name)
    assert single_person_details == json.dumps(expected_response)
    mock_person_by_name_dao.assert_called_once_with(session, name=person.name)
    mock_fruits_and_vegetables.assert_called_once_with(person.favourite_food)
