from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

<<<<<<< HEAD
#SQLALCHEMY_DATABASE_URL = "sqlite:///fastapi-practice.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/sistema"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    )


=======
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/sistema"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
>>>>>>> 01480abdaa879c674741d43e01f5255f38bd5a2c
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()