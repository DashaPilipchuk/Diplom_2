import requests
import allure


class Order:
    @allure.step('create new order')
    def post_create_order(self, url, headers, data):
        return requests.post(f'{url}/api/orders', headers=headers, json=data)

    @allure.step('get user orders')
    def get_user_orders(self, url, headers):
        return requests.get(f'{url}/api/orders', headers=headers)
