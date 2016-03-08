from selenium import webdriver
import page
import unittest
from random import randint

class TwentyThreeandMeTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.get("http://store.23andme.com/en-us/")

	def test_add_product_to_cart_and_enter_shipping_information(self):
		"""Adds 5 tests to cart and enters in shipping information"""
		cart_page = page.CartPage(self.driver)
		assert cart_page.is_title_matches(), "23andMe title doesn't match."
		cart_page.verify_empty_cart()

		cart_page.add_product_to_cart(5)
		count = cart_page.get_cart_rows_count()
		assert 5 == count, "Count was %r" % (count)

		cart_page.input_unique_name_per_product()

		cart_page.verify_individual_product_cost()
		expected = cart_page.calculate_total(5)
		actual = cart_page.get_total()
		assert expected == actual, "Expected amount: %r. Actual amount: %r" % (expected, actual)

		cart_page.click_continue()

		shipping_page = page.ShippingPage(self.driver)
		first_name = 'Paulina'
		last_name = 'Dao'
		address = '899 W Evelyn Ave'
		city = 'Mountain View'
		state = 'California'
		zipcode = '94041'
		email = 'test@test.com'
		phone = '5555555555'

		shipping_page.enter_first_name(first_name)
		shipping_page.enter_last_name(last_name)
		shipping_page.enter_address(address)
		shipping_page.enter_city(city)
		shipping_page.select_state(state)
		shipping_page.enter_zip_code(zipcode)
		shipping_page.enter_email(email)
		shipping_page.enter_phone(phone)

		shipping_page.click_continue()

		verification_page = page.VerificationPage(self.driver)
		verification_page.verify_unverified_information(first_name, last_name, address, city, zipcode)

	def tearDown(self):
		self.driver.close()

