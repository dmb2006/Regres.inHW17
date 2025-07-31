import requests
from jsonschema import validate

from project.schemas.schemas import post_users, login_user, single_user

url = 'https://reqres.in/api'
user = f'?{6}'
users_end_points = '/users'
login = '/login'

headers = {
    'x-api-key': 'reqres-free-v1'
}

def test_get_users_returns_200():
    response = requests.get(url + users_end_points, params={'page': 1})
    assert response.status_code == 200
    assert response.json()['total'] == 12
    assert response.json()['page'] == 1
    assert response.json()['per_page'] == 6

def test_get_user_returns_200():
    response = requests.get(url + users_end_points + user, headers=headers)
    assert response.status_code == 200
    users = response.json()["data"]
    assert users[5]["email"] == 'tracey.ramos@reqres.in'

def test_get_user_not_register_returns_404():
    response = requests.get(url + users_end_points + '/66', headers=headers)
    assert response.status_code == 404

def test_created_user_returns_201():
    name = 'palpatine'
    job = 'dark lord'

    payload = {
        "name": name,
        "job": job
    }

    response = requests.post(url + users_end_points, json=payload, headers=headers)
    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    body = response.json()
    validate(body, post_users)

def test_create_user_returns_401():
    name = 'palpatine'
    job = 'dark lord'

    payload = {
        "name": name,
        "job": job
    }
    response = requests.post(url + users_end_points, json=payload)
    assert response.status_code == 401

def test_user_change_name_and_job_returns_200():
    name = 'palpatine'
    job = 'dark lord'

    payload = {
        "name": name,
        "job": job
    }

    response = requests.put(url + users_end_points + '/111', headers=headers)
    assert response.status_code == 200

def test_user_change_name_and_job_returns_401():
    name = 'palpatine'
    job = 'dark lord'

    payload = {
        "name": name,
        "job": job
    }

    response = requests.put(url + users_end_points + '/111')
    assert response.status_code == 401

def test_deleted_user_returns_204():
    response = requests.delete(url + users_end_points + '/100', headers=headers)
    assert response.status_code == 204

def test_deleted_user_returns_401():
    response = requests.delete(url + users_end_points + '/100')
    assert response.status_code == 401

def test_login_user_returns_200():
    password = 'cityslicka'
    email = 'eve.holt@reqres.in'

    payload = {
        'email': email,
        'password': password
    }

    response = requests.post(url + login, json=payload, headers=headers)
    assert response.status_code == 200
    body = response.json()
    validate(body, login_user)

def test_login_user_returns_400():
    password = 'qwerty'
    email = 'test@test.in'

    payload = {
        'email': email,
        'password': password
    }

    response = requests.post(url + login, json=payload, headers=headers)
    assert response.status_code == 400
