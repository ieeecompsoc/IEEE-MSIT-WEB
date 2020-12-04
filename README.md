# IEEE-MSIT-WEB
Website for IEEE MSIT

# Setting up

### Follow these steps to setup the project locally
```sh
$ git clone https://github.com/ieeecompsoc/IEEE-MSIT-WEB.git
$ cd IEEE-MSIT-WEB
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

After these steps the project should be up at [http://localhost:8000/](http://localhost:8000/)

Now you can access the Admin Panel through [http://localhost:8000/admin](http://localhost:8000/admin) and login with your newly created username and password.

# Alternate Method (updated for windows)
### Setting Up the Code

```sh
> md ieeeMsitWebsite
> cd ieeeMsitWebsite
> pip install -U virtualenv
> virtualenv env
> env/scripts/activate
> git clone https://github.com/ieeecompsoc/IEEE-MSIT-WEB.git
> cd IEEE-MSIT-WEB
> python manage.py makemigrations
> python manage.py migrate
> python manage.py cretesuperuser
```

### Running the Code

Install and setup Postgresql on your system before running the Django Server and configure the dbconfig according to it. (But dont push the changes of this file in your commit).

```
> cd ieeeMsitWebsite
> env/scripts/activate
> cd IEEE-MSIT-WEB
> python manage.py runserver
```

Now you can run the project at [http://localhost:8000/](http://localhost:8000/) .

The Admin Panel is available at [http://localhost:8000/admin](http://localhost:8000/admin) where you can login with your newly created username and password.
