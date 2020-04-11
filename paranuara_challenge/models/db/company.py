from sqlalchemy import Column, Integer, String
from paranuara_challenge.models.db import Base


class Company(Base):
    __tablename__ = 'company'

    company_id = Column('company_id', Integer, primary_key=True, nullable=False)
    company_name = Column('company_name', String(255))

    def __repr__(self):
        return "<User(company_id='%d', company_name='%s')>" % (self.company_id, self.company_name)
