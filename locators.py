from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
	LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
	GOODS_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert-success:nth-child(1) strong')
	GOODS_NAME = (By.CSS_SELECTOR, '.page_inner h1')
	PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')
	GOODS_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')

