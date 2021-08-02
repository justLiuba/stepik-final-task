from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators import ProductPageLocators


class ProductPage(BasePage):
	def add_to_basket(self):
		button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		button.click()
			

	def should_be_right_goods_name_in_the_success_message(self):
		goods_message = self.browser.find_element(*ProductPageLocators.GOODS_NAME_IN_MESSAGE)
		success_text = goods_message.text
		goods = self.browser.find_element(*ProductPageLocators.GOODS_NAME)
		goods_name_text = goods.text
		assert success_text  == goods_name_text, f'Wrong goods name in the success message, "{success_text}" instead of "{goods_name_text}"'

	def should_be_right_price_in_success_message(self):
		price_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE)
		price_text = price_message.text
		goods_price = self.browser.find_element(*ProductPageLocators.GOODS_PRICE)
		goods_price_text = goods_price.text
		assert price_text  == goods_price_text, f'Wrong price in the success message, "{price_text }" instead of "{goods_price_text}"'

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCES_MESSAGE), "Success message is presented, but should not be"

	def message_should_disappear(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCES_MESSAGE), "Success message is presented, but should disappear"




