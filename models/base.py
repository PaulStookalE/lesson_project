import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

# Створюємо 'мотор' бази даних.
database = create_engine(os.getenv('DATABASE'))

# Робимо сесію, яка дозволяє працювати з БД.
Session = sessionmaker(database)
session = Session()

# Збирає класи і створює з них БД.
Base = declarative_base()


# Створюємо функцію для створення бази даних.
def create_db():
    Base.metadata.create_all(database)

# Створюємо функцію для видалення бази даних.
def drop_db():
    Base.metadata.drop_all(database)