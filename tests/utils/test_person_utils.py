from paranuara_challenge.utils.person_utils import get_friends_by_person, get_alive_common_friends_with_brown_eyes, \
    get_food_as_fruits_and_vegetables, get_mutual_friends
from paranuara_challenge.models.db.person import Person
from paranuara_challenge.models.response.multi_person_details import FriendDetails


def test_get_friends_by_person_returns_person_id_friend_ids_dict():
    people_data = [{
        'index': 0,
        'friends': [
            {
                'index': 1
            },
            {
                'index': 2
            }
        ]
    }]

    expected_result = {0: [1, 2]}
    person_friends_dict = get_friends_by_person(people_data)
    assert person_friends_dict == expected_result


def test_get_friends_by_person_does_not_include_friend_id_matching_person_id():
    people_data = [{
        'index': 0,
        'friends': [
            {
                'index': 1
            },
            {
                'index': 2
            }
        ]
    },
        {
            'index': 1,
            'friends': [{
                'index': 0
            }, {
                'index': 1
            }]
        }]

    expected_result = {0: [1, 2], 1: [0]}
    person_friends_dict = get_friends_by_person(people_data)
    assert person_friends_dict == expected_result


def test_get_mutual_friends_applies_intersection_on_friends_of_person1_and_person2():
    friend1 = Person(person_id=10, name='abc')
    friend2 = Person(person_id=11, name='pqr')
    friend3 = Person(person_id=12, name='xyz')

    person1_friends = [friend1, friend2]
    person2_friends = [friend1, friend3]

    expected_result = [friend1]

    mutual_friends = get_mutual_friends(person1_friends, person2_friends)
    assert mutual_friends == expected_result


def test_get_alive_common_friends_with_brown_eyes_returns_mutual_friends_alive_and_having_brown_eyes():
    friend1 = Person(person_id=10, name='abc', has_died=False, eye_color='brown', age=50,
                     gender='abc', email='abc', phone='abc', address='pqr')
    friend2 = Person(person_id=11, name='pqr', has_died=False, eye_color='blue')
    friend3 = Person(person_id=12, name='xyz', has_died=True, eye_color='brown')

    person1_friends = [friend1, friend2, friend3]
    person2_friends = [friend1, friend2, friend3]
    expected_result = [FriendDetails(name=friend1.name, has_died=friend1.has_died, eye_color=friend1.eye_color,
                                     age=friend1.age, gender=friend1.gender, email=friend1.email,
                                     phone=friend1.phone, address=friend1.address)]

    alive_mutual_friends_with_brown_eyes = get_alive_common_friends_with_brown_eyes(person1_friends, person2_friends)
    assert alive_mutual_friends_with_brown_eyes == expected_result


def test_get_food_as_fruits_and_vegetables_returns_dict_of_fruits_and_vegetables():
    favourite_food = ['carrot', 'orange']
    expected_result = {'fruits': ['orange'], 'vegetables': ['carrot']}

    fruit_and_vegetables_dict = get_food_as_fruits_and_vegetables(favourite_food)
    assert fruit_and_vegetables_dict == expected_result


def test_get_food_as_fruits_and_vegetables_returns_fruits_as_empty_list_if_no_fruit_present():
    favourite_food = ['carrot', 'celery']
    expected_result = {'fruits': [], 'vegetables': ['carrot', 'celery']}

    fruit_and_vegetables_dict = get_food_as_fruits_and_vegetables(favourite_food)
    assert fruit_and_vegetables_dict == expected_result


def test_get_food_as_fruits_and_vegetables_returns_vegetables_as_empty_list_if_no_vegetable_present():
    favourite_food = ['orange', 'banana']
    expected_result = {'fruits': ['orange', 'banana'], 'vegetables': []}

    fruit_and_vegetables_dict = get_food_as_fruits_and_vegetables(favourite_food)
    assert fruit_and_vegetables_dict == expected_result


def test_get_food_as_fruits_and_vegetables_ignores_item_if_neither_fruit_nor_vegetable():
    favourite_food = ['carrot', 'orange', 'abc']
    expected_result = {'fruits': ['orange'], 'vegetables': ['carrot']}

    fruit_and_vegetables_dict = get_food_as_fruits_and_vegetables(favourite_food)
    assert fruit_and_vegetables_dict == expected_result
