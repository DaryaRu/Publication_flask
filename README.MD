# Publications app

Demo Python application about publications with rubrics, likes and JWT auth.

## Used technologies

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
* [Flask-JWT](https://flask-jwt.readthedocs.io/en/latest/)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)

## Quick start

### Add venv and install packages

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r API/requirements.txt
```

### Add env.py to API folder

#### configuration options

| name  | type  |
|---|---|
| app_secret  |  string |
| is_debug  |  boolean |

#### example

```python
app_secret="my_secret_key"
is_debug=True
```

### Run project

```bash
cd API
python app.py
```

## Project structure

```
root
|
| - API - Flask application
    |
    | - models - ORM classes
    |   |
    |   | db.py - ORM config
    |
    | - resoureces - application endpoinds
    |
    | app.py - application startup
    | env.py - application config
    | securite.py - JWT auth config
```
