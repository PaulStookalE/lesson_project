# У даному файлі створюємо колонки у DB таблиці.

from enum import Enum
from .base import Base
from sqlalchemy import Column, Float, Integer, String, Enum as Enum_SQLALCHEMY

# Створюємо вибір типів палива.
class FuelChoices(Enum):
    Gasoline = 'Gasoline'
    Diesel = 'Diesel'
    Gas = 'Gas'


# Створюємо таблицю Car.
class Car(Base):
    __tablename__ = 'cars'              # Називаємо таблицю.

    # Створюємо рядки таблиці.
    id = Column(Integer, primary_key=True)
    model_name = Column(String(50), nullable=False)
    engine = Column(Float, nullable=False)
    
    # Підключаємо вибір типів палива
    type_of_fuel = Column(Enum_SQLALCHEMY(FuelChoices, name='fuelchoices_type', create_type=True), nullable=False)


    def __init__(self, model, engine, tof):
        self.model_name = model
        self.engine = engine
        self.type_of_fuel = tof

    
    def __str__(self):
        return f'Car {self.model_name}'