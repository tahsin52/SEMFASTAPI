``` bash
git clone
source venv/bin/activate or virtualenv venv
pip install requirements.txt

add new database in postgresql and path to it in database.py

uvicorn main:app --reload
```

``` bash
    GET /datas - Get all datas and write to json file (2 min)
    GET /cars/ - Get all cars in db
    GET /car/ - Get all cars multiple filters (car/?make=Toyota&model=Corolla&year=2022&transmission=Automatic)
    POST /create/car/ - Create all cars

```