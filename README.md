``` bash
git clone
source venv/bin/activate or virtualenv venv
pip install requirements.txt

uvicorn main:app --reload
```

``` bash
    GET /datas - Get all datas and write to json file
    GET /cars/ - Get all cars in db
    GET /car/ - Get all cars multiple filters (car/?make=Toyota&model=Corolla&year=2022)
    POST /create/car/ - Create all cars

```