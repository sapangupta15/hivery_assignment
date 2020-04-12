from dataclasses import dataclass
from typing import List


@dataclass
class PersonDetails:
    name: str
    age: int
    address: str
    phone: str


@dataclass
class FriendDetails:
    name: str
    age: int
    gender: str
    eye_color: str
    has_died: bool
    email: str
    phone: str
    address: str


@dataclass
class MultiPersonDetails:
    first_person: PersonDetails
    second_person: PersonDetails
    mutual_friends: List[FriendDetails]