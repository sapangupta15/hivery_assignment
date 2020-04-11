from sqlalchemy import Column, Integer, String, Boolean, Numeric, Table, ForeignKey
from sqlalchemy.orm import relationship
from paranuara_challenge.models.db import Base
from paranuara_challenge.utils.currency_utils import convert_number_to_currency_value, \
    convert_currency_string_to_numeric


friendship = Table(
    'friends', Base.metadata,
    Column('person_id', Integer, ForeignKey('person.person_id'), index=True),
    Column('friend_id', Integer, ForeignKey('person.person_id'))
)


class Person(Base):
    __tablename__ = 'person'

    person_id = Column(Integer, primary_key=True, nullable=False)
    internal_id = Column('_id', String(50))
    guid = Column(String(36))
    has_died = Column(Boolean)
    _balance = Column('balance', Numeric(precision=12, scale=2))
    picture = Column(String(255))
    age = Column(Integer)
    eye_color = Column(String(100))
    name = Column(String(255))
    gender = Column(String(20))
    company_id = Column(Integer)
    email = Column(String(255))
    phone = Column(String(255))
    address = Column(String(255))
    about = Column(String(2000))
    registered = Column(String(255))
    _tags = Column('tags', String(255))
    greeting = Column(String(255))
    _favourite_food = Column('favourite_food', String(255))
    friends = relationship('Person',
                           secondary=friendship,
                           primaryjoin=person_id == friendship.c.person_id,
                           secondaryjoin=person_id == friendship.c.friend_id)

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    @property
    def balance(self):
        """Return the value of balance with currency sign appended and thousands separator"""
        if self._balance:
            return convert_number_to_currency_value(self._balance)
        else:
            return None

    @balance.setter
    def balance(self, balance):
        """Remove currency symbol and thousands separator and convert to numeric data type"""
        self._balance = convert_currency_string_to_numeric(balance)

    @property
    def tags(self):
        if self._tags:
            tag_list = self._tags.split(',')
            return [tag.strip() for tag in tag_list]
        else:
            return []

    @tags.setter
    def tags(self, tags):
        self._tags = ','.join(tags)

    @property
    def favourite_food(self):
        if self._favourite_food:
            favourite_food = self._favourite_food.split(',')
            return [food.strip() for food in favourite_food]
        else:
            return None

    @favourite_food.setter
    def favourite_food(self, favourite_food):
        self._favourite_food = ','.join(favourite_food)

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, obj):
        return isinstance(obj, Person) and obj.person_id == self.person_id and obj.name == self.name

    def __hash__(self):
        return hash((self.person_id, self.name))

