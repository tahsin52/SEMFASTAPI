from database import Base
from sqlalchemy import Column, Integer, String


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, nullable=True, primary_key=True)
    bodystyle = Column(String, index=True)
    canonical_mmt = Column(String, index=True)
    customer_id = Column(String, nullable=True)
    fuel_type = Column(String, nullable=True)
    listing_id = Column(String, primary_key=True)
    make = Column(String, nullable=True)
    mileage = Column(String, nullable=True)
    model = Column(String, nullable=True)
    msrp = Column(String, nullable=True)
    price = Column(String)
    seller_type = Column(String)
    stock_type = Column(String)
    trim = Column(String)
    vin = Column(String)
    year = Column(String)
    exterior_color = Column(String, nullable=True)

    def __repr__(self):
        return f'{self.year} {self.make} {self.model} {self.exterior_color}'