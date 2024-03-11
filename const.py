class Constants:
    URL = 'https://stellarburgers.nomoreparties.site'
    OLD_EMAIL = "test-dasha@yandex.ru"
    OLD_PASSWORD = "2345678"
    OLD_NAME = "sasa"
    VALID_HASH = ["61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa70"]
    INVALID_HASH = "60d3b41abdacab0026a733c6"


class ResponseBody:
    USER_RESPONSE_ALREADY_EXISTS = {
        "success": False,
        "message": "User already exists"
    }
    USER_RESPONSE_WITHOUT_FIELDS = {
        "success": False,
        "message": "Email, password and name are required fields"
    }
    USER_RESPONSE_UNAUTHORIZED = {
        "success": False,
        "message": "email or password are incorrect"
    }
    USER_RESPONSE_WITHOUT_TOKEN = {
        "success": False,
        "message": "You should be authorised"
    }
    ORDER_WITHOUT_INGREDIENTS = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }
    ORDER_WITH_INCORRECT_HASH = {
        "success": False,
        "message": "One or more ids provided are incorrect"
    }
    SUCCESS = True

