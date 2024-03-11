import requests
import allure


class User:
    @allure.step('create new user')
    def post_create_user(self, url, data):
        return requests.post(f'{url}/api/auth/register', json=data)

    @allure.step('login user')
    def post_login_user(self, url, data):
        return requests.post(f'{url}/api/auth/login', json=data)

    @allure.step('change user data')
    def patch_change_user_data(self, url, headers, data):
        return requests.patch(f'{url}/api/auth/user', headers=headers, json=data)

    @allure.step('delete user')
    def delete_user(self, url, headers):
        return requests.delete(f'{url}/api/auth/user', headers=headers)
