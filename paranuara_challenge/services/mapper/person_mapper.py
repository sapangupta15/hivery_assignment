from paranuara_challenge.models.db.person import Person


def map_person_attributes(**person_attributes):
    person = Person(
        person_id=person_attributes['index'],
        internal_id=person_attributes['_id'],
        guid=person_attributes['guid'],
        has_died=person_attributes['has_died'],
        picture=person_attributes['picture'],
        age=person_attributes['age'],
        eye_color=person_attributes['eyeColor'],
        name=person_attributes['name'],
        gender=person_attributes['gender'],
        company_id=person_attributes['company_id'],
        email=person_attributes['email'],
        phone=person_attributes['phone'],
        address=person_attributes['address'],
        about=person_attributes['about'],
        registered=person_attributes['registered'],
        greeting=person_attributes['greeting']
    )
    person.balance = person_attributes['balance']
    person.tags = person_attributes['tags']
    person.favourite_food = person_attributes['favouriteFood']

    return person
