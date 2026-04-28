<<<<<<< HEAD
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column



class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
=======
from .database import Base
from sqlalchemy import Column, Integer, String


class DbUser(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
>>>>>>> 01480abdaa879c674741d43e01f5255f38bd5a2c
