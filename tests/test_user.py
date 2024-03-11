from client.user import User
from const import Constants, ResponseBody
import pytest
import allure
from faker import Faker
fake = Faker()

fake_email = fake.email()
fake_password = fake.password()
fake_name = fake.name()


class TestUser:
    @allure.title('create user')
    def test_create_user(self, delete_user):
        data = {
            "email": fake_email,
            "password": fake_password,
            "name": fake_name
            }
        user = User()
        response = user.post_create_user(Constants.URL, data)
        token = response.json()["accessToken"]
        delete_user['Authorization'] = token
        assert response.status_code == 200

    @allure.title('can`t create user that already exists')
    def test_create_user_that_already_exist(self):
        data = {
            "email": Constants.OLD_EMAIL,
            "password": Constants.OLD_PASSWORD,
            "name": Constants.OLD_NAME
            }
        user = User()
        response = user.post_create_user(Constants.URL, data)
        assert response.status_code == 403 and response.json() == ResponseBody.USER_RESPONSE_ALREADY_EXISTS

    @allure.title('can`t create user without required field')
    @pytest.mark.parametrize('email, password, name', [('', fake_password, fake_name), (fake_email, '', fake_name),
                                                       (fake_email, fake_password, ''), ('', '', '')])
    def test_create_user_without_required_field(self, email, password, name):
        data = {
            "email": email,
            "password": password,
            "name": name
                }
        user = User()
        response = user.post_create_user(Constants.URL, data)
        assert response.status_code == 403 and response.json() == ResponseBody.USER_RESPONSE_WITHOUT_FIELDS

    @allure.title('login user with valid data')
    def test_login_user_with_valid_data(self):
        data = {
            "email": Constants.OLD_EMAIL,
            "password": Constants.OLD_PASSWORD
        }
        user = User()
        response = user.post_login_user(Constants.URL, data)
        assert response.status_code == 200

    @allure.title('login user with incorrect data')
    @pytest.mark.parametrize('email, password', [(fake_email, Constants.OLD_PASSWORD),
                                                 (Constants.OLD_EMAIL, fake_password), (fake_email, fake_password)])
    def test_login_user_with_incorrect_data(self, email, password):
        data = {
            "email": email,
            "password": password
        }
        user = User()
        response = user.post_login_user(Constants.URL, data)
        assert response.status_code == 401 and response.json() == ResponseBody.USER_RESPONSE_UNAUTHORIZED

    @allure.title('change_user_data with authorization')
    def test_change_user_data_with_authorization(self, prepare_user):
        data = {
            "email": fake_email,
            "password": fake_password
        }
        headers = {'Authorization': prepare_user}
        user = User()
        response = user.patch_change_user_data(Constants.URL, headers=headers, data=data)
        assert response.status_code == 200

    @allure.title('change_user_data without authorization')
    def test_change_user_data_without_authorization(self, prepare_user):
        data = {
            "email": fake_email,
            "password": fake_password
        }
        headers = {'Authorization': ''}
        user = User()
        response = user.patch_change_user_data(Constants.URL, headers=headers, data=data)
        assert response.status_code == 401 and response.json() == ResponseBody.USER_RESPONSE_WITHOUT_TOKEN






