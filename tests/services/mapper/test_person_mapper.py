from paranuara_challenge.services.mapper.person_mapper import map_person_attributes

def test_map_person_attributes_returns_person_with_custom_setters_applied():
    person_attributes = {
        "_id": "595eeb9c898ae2a0e9655fa9",
        "index": 995,
        "guid": "3f659dff-2f07-4697-b743-cf622b131203",
        "has_died": False,
        "balance": "$3,168.09",
        "picture": "http://placehold.it/32x32",
        "age": 20,
        "eyeColor": "blue",
        "name": "Sawyer Bruce",
        "gender": "male",
        "company_id": 95,
        "email": "sawyerbruce@earthmark.com",
        "phone": "+1 (993) 439-2320",
        "address": "343 Voorhies Avenue, Chelsea, District Of Columbia, 175",
        "about": "Irure aliqua voluptate aliquip qui. Quis proident elit anim pariatur culpa quis proident dolor. Ea fugiat laboris qui dolor sit laboris in nisi nulla duis. Labore proident velit ipsum laboris incididunt enim esse minim. Quis cillum nisi nisi aliquip incididunt nostrud do ipsum nisi dolore magna. Amet do aliquip pariatur est enim officia ullamco mollit adipisicing non occaecat.\r\n",
        "registered": "2015-03-31T01:31:29 -11:00",
        "tags": [
            "ea",
            "do"
        ],
        "friends": [
            {
                "index": 0
            }],
        "greeting": "Hello, Sawyer Bruce! You have 4 unread messages.",
        "favouriteFood": ["cucumber"]
    }

    mapped_person = map_person_attributes(**person_attributes)
    assert mapped_person.person_id == person_attributes['index']
    assert mapped_person.name == person_attributes['name']
    assert mapped_person.balance == person_attributes['balance']
    assert mapped_person._balance == 3168.09
    assert mapped_person.tags == person_attributes['tags']
    assert mapped_person._tags == 'ea,do'
    assert mapped_person.favourite_food == person_attributes['favouriteFood']
    assert mapped_person._favourite_food == 'cucumber'