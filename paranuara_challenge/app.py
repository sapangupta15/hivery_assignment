from flask import Flask, request, make_response
from flask_swagger_ui import get_swaggerui_blueprint

from paranuara_challenge.services.employee_service import get_employees_for_company
from paranuara_challenge.services.people_service import get_details_for_two_people, get_details_for_single_person
from paranuara_challenge.exceptions.input_exception import InvalidInputException
from paranuara_challenge.exceptions.processing_exception import ProcessingException
from paranuara_challenge.utils.input_validator import validate_input_args

app = Flask(__name__)

# add swagger details
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "PARANUARA PLANET"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.errorhandler(InvalidInputException)
def handle_bad_request(e):
    return e.message, 400


@app.errorhandler(ProcessingException)
def handle_uncaught_errors(e):
    return e.message, 500


@app.route('/employees', methods=['GET'])
def get_employee_details_company():
    """
    This endpoint takes a company name and return employees associated with tha company
    If no employee is present, then kit returns employee count as 0 and empty list for employees
    :return:
    """
    company_name = request.args.get('company')
    if company_name is None:
        raise InvalidInputException('Mandatory request attribute: company_name is missing')

    # apply basic validations, to avoid sql inject, XSS, bffer overflow attacks
    validate_input_args(company_name)

    employee_details = get_employees_for_company(company_name)
    return make_response(employee_details, 200)


@app.route('/persons', methods=['GET'])
def get_multiple_people_details():
    """
    This endpoint takes 2 query params: name1 and name2 as names of 2 people
    Then it returns details of both the persons as well as their mutual friends that are alive and have brown eyes
    :return:
    """
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    if name1 is None or name2 is None:
        raise InvalidInputException('One or both person names are missing')

    # apply basic validations, to avoid sql inject, XSS, bffer overflow attacks
    validate_input_args(name1, name2)

    people_details = get_details_for_two_people(name1=name1, name2=name2)
    return make_response(people_details, 200)


@app.route('/person', methods=['GET'])
def get_single_person_details():
    """
    This endpoint takes person's name as the argument and pulls details for the person from db.
    additionally, it splits person's favourite food into fruits and vegetables
    :return:
    """
    name = request.args.get('name')
    if name is None:
        raise InvalidInputException('Name is missing for person details lookup')

    # apply basic validations, to avoid sql inject, XSS, bffer overflow attacks
    validate_input_args(name)

    people_details = get_details_for_single_person(name)
    return make_response(people_details, 200)


if __name__ == '__main__':
    app.run()
