import os
from yoyo import read_migrations
from yoyo import get_backend
from paranuara_challenge.dao.company_dao import add_companies
from paranuara_challenge.dao.person_dao import add_persons


path_to_migrations = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'migrations'))
backend = get_backend(os.getenv('DB_URL'))
migrations = read_migrations(path_to_migrations)

with backend.lock():
    # Apply any outstanding migrations
    backend.apply_migrations(backend.to_apply(migrations))
    add_companies()
    add_persons()
