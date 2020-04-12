import json
from paranuara_challenge.services.db.session_manager import session_manager
from paranuara_challenge.dao.person_dao import get_person_by_name
from paranuara_challenge.models.response.multi_person_details import PersonDetails, MultiPersonDetails
from paranuara_challenge.models.response.single_person_details import SinglePersonDetails
from paranuara_challenge.utils.json_utils import DataClassJSONEncoder
from paranuara_challenge.utils.person_utils import get_alive_common_friends_with_brown_eyes, \
    get_food_as_fruits_and_vegetables


@session_manager
def get_details_for_two_people(session, name1, name2):
    """
    Get peorson details for the 2 people, given their names.
    Additionally, their friend lists are also fetched.
    Then mutual friends are selected using intersection and
    filtered so that friends are alive and have brown eyes
    :param session:
    :param name1:
    :param name2:
    :return:
    """
    person1 = get_person_by_name(session, name=name1, fetch_friends=True)
    person2 = get_person_by_name(session, name=name2, fetch_friends=True)
    alive_mutual_friends_with_brown_eyes = get_alive_common_friends_with_brown_eyes(person1.friends, person2.friends)
    person_details_with_friends = MultiPersonDetails(
        first_person=PersonDetails(name=person1.name,
                                   age=person1.age,
                                   address=person1.address,
                                   phone=person1.phone),
        second_person=PersonDetails(name=person2.name,
                                    age=person2.age,
                                    address=person2.address,
                                    phone=person2.phone),
        mutual_friends=alive_mutual_friends_with_brown_eyes)
    return json.dumps(person_details_with_friends, cls=DataClassJSONEncoder)


@session_manager
def get_details_for_single_person(session, name):
    """
    Get person details for the name recieved in request.
    Friend details are not required, hence not fetched from db.
    Then split person's favourite food into fruits and vegetables
    :param session:
    :param name:
    :return:
    """
    person = get_person_by_name(session, name=name)
    food_as_fruits_and_vegetables = get_food_as_fruits_and_vegetables(person.favourite_food)
    person_details = SinglePersonDetails(username=person.name,
                                         age=person.age,
                                         fruits=food_as_fruits_and_vegetables['fruits'],
                                         vegetables=food_as_fruits_and_vegetables['vegetables'])
    return json.dumps(person_details, cls=DataClassJSONEncoder)
