from selenium.webdriver.common.by import By

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
	LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
	EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
	PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
	CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
	REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')
	SUCCES_MESSAGE = (By.CSS_SELECTOR,'.alert-success .alertinner')

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
	SUCCES_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1)')
	GOODS_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert-success:nth-child(1) strong')
	GOODS_NAME = (By.CSS_SELECTOR, '.page_inner h1')
	PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')
	GOODS_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.CSS_SELECTOR, '.btn-group .btn-default:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	ITEMS_TO_BYE = (By.CSS_SELECTOR, 'h2.col-sm-6')
	EMPTY_BASKET_MESSSAGE = (By.XPATH, '//p[contains(text(), "Your basket is empty.")]')

