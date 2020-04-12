import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = os.getenv('DB_URL')
db_url = db_url.replace('mysql://', 'mysql+pymysql://')
engine = create_engine(db_url, pool_recycle=3600)
SessionFactory = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = SessionFactory()
    try:
        yield session
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise
    finally:
        session.close()