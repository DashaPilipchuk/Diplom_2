from client.order import Order
from const import Constants, ResponseBody
import allure


class TestOrder:
    @allure.title('create order with authorization')
    def test_create_order_with_authorization(self, prepare_user):
        data = {
            "ingredients": Constants.VALID_HASH
        }
        order = Order()
        headers = {'Authorization': prepare_user}
        response = order.post_create_order(Constants.URL, headers=headers, data=data)
        response_data = response.json()
        assert response.status_code == 200 and response_data.get("success") == ResponseBody.SUCCESS

    @allure.title('create order without authorization')
    def test_create_order_without_authorization(self, prepare_user):
        data = {
            "ingredients": Constants.VALID_HASH
        }
        order = Order()
        headers = {'Authorization': ''}
        response = order.post_create_order(Constants.URL, headers=headers, data=data)
        response_data = response.json()
        assert response.status_code == 200 and response_data.get("success") == ResponseBody.SUCCESS

    @allure.title('create order without Ingredients')
    def test_create_order_without_Ingredients(self, prepare_user):
        data = {
            "ingredients": ""
        }
        order = Order()
        headers = {'Authorization': prepare_user}
        response = order.post_create_order(Constants.URL, headers=headers, data=data)
        assert response.status_code == 400 and response.json() == ResponseBody.ORDER_WITHOUT_INGREDIENTS

    @allure.title('create order with incorrect hash Ingredients')
    def test_create_order_with_Ingredients(self, prepare_user):
        data = {
            "ingredients": Constants.INVALID_HASH
        }
        order = Order()
        headers = {'Authorization': ''}
        response = order.post_create_order(Constants.URL, headers=headers, data=data)
        assert response.status_code == 400 and response.json() == ResponseBody.ORDER_WITH_INCORRECT_HASH

    @allure.title('get order list with authorization')
    def test_get_order_list_with_authorization(self, prepare_order):
        order = Order()
        headers = {'Authorization': prepare_order}
        response = order.get_user_orders(Constants.URL, headers=headers)
        response_data = response.json()
        assert response.status_code == 200 and response_data.get("success") == ResponseBody.SUCCESS

    @allure.title('get order list without authorization')
    def test_get_order_list_without_authorization(self, prepare_order):
        order = Order()
        headers = {'Authorization': ''}
        response = order.get_user_orders(Constants.URL, headers=headers)
        assert response.status_code == 401 and response.json() == ResponseBody.USER_RESPONSE_WITHOUT_TOKEN
