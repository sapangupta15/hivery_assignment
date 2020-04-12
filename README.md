# This project uses Flask to create APIS to get information about paranuara planet.

### Setup


1. Run git clone https://github.com/sapangupta15/paranuara_planet.git to clone the project on local system.
2. Navigate to root directory of checkout path - BASE_PROJECT_DIR

---

#### Windows
RUN following commands in cmd line:
```bat
$ cd <BASE_PROJECT_DIR>
$ SET PYTHONPATH=<BASE_PROJECT_DIR>
$ SET DB_URL=mysql://<username>:<password>>@<host>:<port>/<db_name>
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ pytest tests\
$ python db_migrations.py
$ python paranuara_challenge\app.py
```

---
#### Linux/MacOS
RUN following commands in terminal:
```bash
$ cd <BASE_PROJECT_DIR>
$ export PYTHONPATH=<BASE_PROJECT_DIR>
$ export DB_URL=mysql://<username>:<password>>@<host>:<port>/<db_name>
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ $ pytest tests/
$ python db_migrations.py
$ python paranuara_challenge/app.py
```

---
These steps essentially perform the following steps:
- navigate to project root directory
- set PYTHONPATH env variable
- set DB_URL env variable, which will be used by the main app, as well as db migrations script
- create virtual environment, activate venv and install dependencies
- Run unit tests
- Run db migrations to create tables in database (This project yoyo-migratons. Checkout https://pypi.org/project/yoyo-migrations/4.2.0/ for more details). This also sets up the required data from json files into database.
##### For this to work, it is important that json files are placed at resources directory of the project.
- Run the flask app


The endpoints are available at for documentation as well as testing:
http://127.0.0.1:5000/swagger/

There are 3 endpoints:
1. /employees - takes company_name as query param and returns employees for a company
2. /persons - takes 2 params, name1 and name2 and returns details for these persons as well as mutual funds who are alive and have brown eyes
3. /person - takes name as query param and returns details for person with that name. Also splits favourite food for the person into vegetables and fruits.
