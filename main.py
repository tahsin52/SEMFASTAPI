import random
from fastapi import FastAPI, Request
from sqlalchemy.orm import Session
import models
import services
from collect import write_json
from database import engine, Base

app = FastAPI()
session = Session(bind=engine)


@app.get("/datas/", status_code=200)
async def get_datas():
    await write_json()
    return services.get_all_data_services()


@app.get("/cars/")
async def get_all_car():
    return session.query(models.Car).all()


@app.get("/car/")
async def multiple_query_by_car(request: Request):
    query_params = request.query_params
    if not query_params:
        return random.choices(session.query(models.Car).all(), k=50)
    cars = session.query(models.Car).filter_by(**query_params).all()
    list_cars = []
    for car in cars:
        a = {
            "id": car.id,
            'title': car.year + ' ' + car.make + ' ' + car.model,
            'make': car.make,
            'model': car.model,
            'listing_id': car.listing_id,
            'year': car.year,
            'price': car.price,
            'exterior_color': car.exterior_color,
            'transmission': car.transmission,
        }
        list_cars.append(a)

    return list_cars


@app.post("/create/car/", status_code=201)
async def create_car():
    for data in services.get_list_data():
        car = models.Car(
            id=random.randint(1, 100000),
            bodystyle=data['bodystyle'],
            canonical_mmt=data['canonical_mmt'],
            customer_id=data['customer_id'],
            fuel_type=data['fuel_type'],
            listing_id=data['listing_id'],
            make=data['make'],
            mileage=data['mileage'],
            model=data['model'],
            msrp=data['msrp'],
            price=data['price'],
            seller_type=data['seller_type'],
            stock_type=data['stock_type'],
            trim=data['trim'],
            vin=data['vin'],
            year=data['year'],
            exterior_color=data['exterior_color'],
            transmission=data['transmission']
        )
        session.add(car)
        session.commit()

    return {"message": "Cars created successfully!"}


Base.metadata.create_all(engine)
