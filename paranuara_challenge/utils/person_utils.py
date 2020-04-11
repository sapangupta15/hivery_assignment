from paranuara_challenge.models.response.multi_person_details import FriendDetails
from paranuara_challenge.services.constants import VEGETABLES, FRUITS
from paranuara_challenge.utils.logger import logger


def get_friends_by_person(people_data):
    """
    For list containing people data, create a dictionary with person id as key and list of his friends' IDs as value
    If friend id and person id match, then tha record is ignored from friends
    :param people_data:
    :return:
    """
    person_friends_ids = {}
    for data in people_data:
        person_id = data['index']
        friends = [friend['index'] for friend in data['friends'] if friend['index'] != person_id]
        person_friends_ids.update({person_id: friends})
    return person_friends_ids


def get_alive_common_friends_with_brown_eyes(person1_friends, person2_friends):
    """
    Apply intersection on list of friends for person1 and person2
    then filter those friends who are alive and have brown eyes
    :param person1_friends:
    :param person2_friends:
    :return:
    """

    # apply intersection on friends on person 1 and person2
    mutual_friends = list(set(person1_friends) & set(person2_friends))

    return [FriendDetails(
        name=friend.name,
        age=friend.age,
        gender=friend.gender,
        eye_color=friend.eye_color,
        has_died=friend.has_died,
        email=friend.email,
        phone=friend.phone,
        address=friend.address
    ) for friend in mutual_friends
        if not friend.has_died
        and friend.eye_color == 'brown']


def get_food_as_fruits_and_vegetables(food_items):
    """
    Split favourite food items into fruits and vegetables
    After analysis of data for people, a list of fruits and vegetables
    has been prepared and stored in constants file
    :param food_items:
    :return:
    """
    fruits = []
    vegetables = []
    for item in food_items:
        if item in FRUITS:
            fruits.append(item)
        elif item in VEGETABLES:
            vegetables.append(item)
        else:
            logger.warning(f'Food item: ite is neither a fruit or a vegetable')
    return {
        'fruits': fruits,
        'vegetables': vegetables
    }
