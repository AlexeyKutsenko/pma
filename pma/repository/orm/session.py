import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

configuration = {
    "POSTGRES_USER": os.environ["POSTGRES_USER"],
    "POSTGRES_PASSWORD": os.environ["POSTGRES_PASSWORD"],
    "POSTGRES_HOSTNAME": os.environ["POSTGRES_HOSTNAME"],
    "POSTGRES_PORT": os.environ["POSTGRES_PORT"],
    "APPLICATION_DB": os.environ["APPLICATION_DB"],
}

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    configuration["POSTGRES_USER"],
    configuration["POSTGRES_PASSWORD"],
    configuration["POSTGRES_HOSTNAME"],
    configuration["POSTGRES_PORT"],
    configuration["APPLICATION_DB"],
)

engine = create_engine(SQLALCHEMY_DATABASE_URI)

DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
