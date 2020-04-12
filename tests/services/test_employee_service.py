import json
from unittest.mock import patch

from paranuara_challenge.services.employee_service import get_employees_for_company
from paranuara_challenge.models.db.person import Person
from sqlalchemy.orm.session import Session


@patch('paranuara_challenge.services.employee_service.get_persons_by_company_id')
@patch('paranuara_challenge.services.employee_service.get_company_by_name')
def test_get_employees_for_company_returns_employees_and_employee_count_for_a_company(mock_company_id, mock_employees):
    employee = Person(person_id=5, name='abc pqr', email='abc', address='abc', phone='abc', age=50,
                      gender='abc', has_died=False, about='abc', registered='abc', tags=['abc'])
    mock_company_id.return_value = 1
    mock_employees.return_value = [employee]

    company_name = 'xyz'
    expected_response = {
        'company_name': company_name,
        'employee_count': 1,
        'employees': [{
            'name': employee.name,
            'email': employee.email,
            'address': employee.address,
            'phone': employee.phone,
            'age': employee.age,
            'gender': employee.gender,
            'has_died': employee.has_died,
            'about': employee.about,
            'registered': employee.registered,
            'tags': employee.tags
        }]
    }
    session = Session()

    company_employees_response = get_employees_for_company(session, company_name=company_name)
    assert company_employees_response == json.dumps(expected_response)
    mock_company_id.assert_called_once_with(session, company_name=company_name)
    mock_employees.assert_called_once_with(session, company_id=1)


@patch('paranuara_challenge.services.employee_service.get_persons_by_company_id')
@patch('paranuara_challenge.services.employee_service.get_company_by_name')
def test_get_employees_for_company_returns_employee_count_zero_when_no_employee_for_company(mock_company_id,
                                                                                            mock_employees):
    mock_company_id.return_value = 1
    mock_employees.return_value = []

    company_name = 'xyz'
    expected_response = {
        'company_name': company_name,
        'employee_count': 0,
        'employees': []
    }
    session = Session()

    company_employees_response = get_employees_for_company(session, company_name=company_name)
    assert company_employees_response == json.dumps(expected_response)
    mock_company_id.assert_called_once_with(session, company_name=company_name)
    mock_employees.assert_called_once_with(session, company_id=1)


