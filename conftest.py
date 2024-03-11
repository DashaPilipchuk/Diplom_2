import pytest
from client.user import User
from client.order import Order
from const import Constants
from faker import Faker
fake = Faker()

fake_email = fake.email()
fake_password = fake.password()
fake_name = fake.name()


@pytest.fixture()
def prepare_user():
    data = {
        "email": fake_email,
        "password": fake_password,
        "name": fake_name
    }
    user = User()
    response = user.post_create_user(Constants.URL, data)
    token = response.json()["accessToken"]
    headers = {'Authorization': token}
    yield token
    user.delete_user(Constants.URL, headers=headers)


@pytest.fixture()
def delete_user():
    user = User()
    headers = {}
    yield headers
    user.delete_user(Constants.URL, headers=headers)


@pytest.fixture()
def prepare_order(prepare_user):
    data_order = {
        "ingredients": Constants.VALID_HASH
    }
    order = Order()
    headers = {'Authorization': prepare_user}
    order.post_create_order(Constants.URL, headers=headers, data=data_order)
    return prepare_user

