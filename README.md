# Task Management API

A RESTful API built with Django and Django REST Framework for managing users and their tasks.

---

## Technologies used

* Django
* Django REST Framework
* Djoser
* Insomnia

---

## Features

* Ordering,Filtering,Pagination,Throttling
* Token Based Authentification
* Secure
* Browsable API Interface


## API Endpoints

---

### Token
* `POST /token/`- Gets the User Token for Requests outside of the browser

### Users

* `GET /api/users/<id>/` - See a user with their tasks

### Tasks

* `GET /api/tasks/` - Retrieve all tasks

* `POST /api/tasks/`- Create a new task/A list of tasks

* `GET /api/tasks/<id>/`- Retrieve a specific task

* `PUT /api/tasks/<id>/`- Update a task

* `DELETE /api/tasks/<id>/` - Delete a task

