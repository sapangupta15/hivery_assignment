import json
from paranuara_challenge.services.db.session_manager import session_manager
from paranuara_challenge.dao.company_dao import get_company_by_name
from paranuara_challenge.dao.person_dao import get_persons_by_company_id
from paranuara_challenge.models.response.company_employees import CompanyEmployees, Employee
from paranuara_challenge.utils.json_utils import DataClassJSONEncoder


@session_manager
def get_employees_for_company(session, company_name):
    """
    Given a company name, fetch company id from db
    and then look up employees for that particular company id.
    If no employees are present, then employees attribute is set to be empty list
    :param session:
    :param company_name:
    :return:
    """
    company_id = get_company_by_name(session, company_name=company_name)
    employees = get_persons_by_company_id(session, company_id=company_id)
    employee_attrs = [Employee(
        name=employee.name,
        email=employee.email,
        address=employee.address,
        phone=employee.phone,
        age=employee.age,
        gender=employee.gender,
        has_died=employee.has_died,
        about=employee.about,
        registered=employee.registered,
        tags=employee.tags)
        for employee in employees]
    company_employees = CompanyEmployees(company_name=company_name,
                                         employee_count=len(employees),
                                         employees=employee_attrs)
    return json.dumps(company_employees, cls=DataClassJSONEncoder)