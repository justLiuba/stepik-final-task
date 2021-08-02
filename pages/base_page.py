from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import math
from selenium.common.exceptions import NoAlertPresentException 
import time


class BasePage():
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True

	def open(self):
		self.browser.get(self.url)

	def solve_quiz_and_get_code(self):
		# alert = WebDriverWait(self.browser, 3).until(EC.alert_is_present())
		alert = self.browser.switch_to.alert
		alert_text = alert.text
		x = alert_text[4:7]
		print(alert_text)
		print(x)
		y = str(math.log(abs(12*math.sin(int(x)))))
		alert.send_keys(y) 
		alert.accept()
		try:
			# alert = WebDriverWait(self.browser, 3).until(EC.alert_is_present())
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			llist = alert_text.split()
			print(llist[-1])
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")
