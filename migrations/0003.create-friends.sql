--
-- file: migrations/0003.create-friends.sql
--
create table FRIENDS
(
    PERSON_ID int,
    FRIEND_ID int,
    CONSTRAINT person_friend_pk PRIMARY KEY (PERSON_ID, FRIEND_ID),
    CONSTRAINT fk_person
      FOREIGN KEY (PERSON_ID) REFERENCES PERSON (PERSON_ID),
    CONSTRAINT fk_friend
      FOREIGN KEY (FRIEND_ID) REFERENCES PERSON (PERSON_ID)
);