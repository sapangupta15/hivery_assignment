import os
import json
from sqlalchemy import func
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from paranuara_challenge.dao import resource_path
from paranuara_challenge.models.db.company import Company
from paranuara_challenge.services.db.session_manager import session_manager
from paranuara_challenge.exceptions.ProcessingException import ProcessingException


@session_manager
def add_companies(session):
    with open(os.path.join(resource_path, 'companies.json'), 'r') as companies_file:
        company_data = json.loads(companies_file.read())
    companies = [Company(company_id=data['index'], company_name=data.get('company')) for data in company_data]
    session.bulk_save_objects(companies)


@session_manager
def get_company_by_name(session, company_name):
    try:
        company = session.query(Company).filter(func.lower(Company.company_name) == company_name.lower()).one()
        return company.company_id
    except MultipleResultsFound:
        raise ProcessingException(f'more than 1 result exists for company name: {company_name}')
    except NoResultFound:
        raise ProcessingException(f'No result exists for company name: {company_name}')
    except Exception as e:
        raise ProcessingException(f'Error has occurred, message: {e.message}')
