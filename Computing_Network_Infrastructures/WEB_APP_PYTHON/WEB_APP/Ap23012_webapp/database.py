from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base
from config import connection_string

#Setting Up SQLAlchemy Engine and Scoped Session
engine = create_engine(connection_string, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
#Assigning Query Property to Base Class in SQLAlchemy Configuration
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)