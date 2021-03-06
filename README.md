# python-web-app

### References
* https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

### Dependencies

* list down dependencies
```sh
pip freeze > requirements.txt
```

### Virtual Environment

* create virtual env
```sh
python3 -m venv vir-env
```

* activate virtual env
```sh
source vir-env/bin/activate
```

### Flask

* install flask
```sh
pip install flask
```

* set main script to run
```sh
export FLASK_APP=app
```

* set development mode
```sh
export FLASK_ENV=development
```

* run flask
```sh
flask run
```

### Database

* create `init_db.py` to create table & insert static data to db
* execute `init_db.py`, and file `database.db` will appear
```sh
python3 db_setup/init_db.py
```