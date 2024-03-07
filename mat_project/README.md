![Logo of the project](https://crowdbotics.ghost.io/content/images/2019/05/django.png)

# Django Side Project
> Uses the Django Rest Framework (DRF)

A django application that populates the DB using a csv file and exposes the data through a REST API. 

## Installing / Getting started

### Requirements
* [Docker](https://docs.docker.com/engine/install/)
* [Poetry](https://python-poetry.org/docs/)


### Run Postgresql DB
```
docker-compose -f infrastructure/docker-compose.yaml up -d 
```

### Install Python Dependencies
```
cd mat_project
poetry install
```

### Run DB Migrations
```
python manage.py migrate 
```

### Run Tests
```
python manage.py test 
```

### Run App
```
python manage.py runserver
```

### Create Super User to access Admin Page (Optional)
```
python manage.py createsuperuser
```


### TODO
- [ ] Add Deployment process
- [ ] Add CI/CD Pipeline to build project and run tests
- [ ] Add Error Monitoring (e.g [Sentry](https://sentry.io/))
- [ ] Add User Data Analytics (e.g [Mixpanel](https://mixpanel.com/))