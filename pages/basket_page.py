from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
	def should_not_be_goods_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BYE), 'Some items present in the basket, but should not be'
		assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSSAGE), 'No message, about the basket is empty'
