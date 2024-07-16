from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

SQLALCHEMY_DATABASE_URL = URL(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="Iconic@1234",
    database="feedalyzer",
    host="localhost",
    port="5432",
    query= {"sslmode":"prefer"}
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()