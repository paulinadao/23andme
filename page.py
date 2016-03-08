from locators import CartPageLocators, ShippingPageLocators, VerificationPageLocators
from random import randint
from selenium.webdriver.support.ui import Select
import random, string
import unittest

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class CartPage(BasePage):
    """Cart page methods belong here"""

    def is_title_matches(self):
        """Verifies that correct page is returned"""
        return "Store - 23andMe - DNA Genetic Testing & Analysis" in self.driver.title

    def generate_random_name(self, length=10):
        """Generates a random name for order"""
        first_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
        last_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
        return first_name + ' ' + last_name

    def input_unique_name_per_product(self):
        """Enters a random name for each input field in cart"""
        cart_rows = self.driver.find_elements(*CartPageLocators.CART_ROW)
        
        for row in cart_rows:
            row.find_element(*CartPageLocators.KIT_NAME_INPUT_FIELD).send_keys(self.generate_random_name())

    def verify_individual_product_cost(self):
        """Verifies that the product cost is correct. First item is full priced. Additional items are 10 percent off"""
        cart_rows = self.driver.find_elements(*CartPageLocators.CART_ROW)
        
        for index, row in enumerate(cart_rows):
            if index==0:
                price = row.find_element(*CartPageLocators.ITEM_PRICE).text
                assert '$199.00' == price
            else:
                assert row.find_element(*CartPageLocators.ITEM_PRICE).find_element_by_class_name('discount').is_displayed()
                price = row.find_element(*CartPageLocators.ITEM_PRICE).find_element_by_class_name('discount').text.lstrip('10% off: ')
                assert '$179.10' == price

    def calculate_total(self, quantity):
        """Calculates the total cost of order"""
        if quantity == 1:
            total = 199.00
        else:
            total = 199.00 + 179.10*(quantity-1)
        return float(total)

    def get_total(self):
        """Gets the total cost of order"""
        return float(self.driver.find_element(*CartPageLocators.TOTAL_ROW).find_element_by_class_name('price-display').text.lstrip('$'))

    def get_cart_rows_count(self):
        """Returns the count of rows in the shopping cart"""
        return len(self.driver.find_elements(*CartPageLocators.CART_ROW))

    def add_product_to_cart(self, quantity):
        """Adds product to cart"""
        for x in range(0, quantity):
            self.driver.find_element(*CartPageLocators.ADD_KIT_BUTTON).click()

    def verify_empty_cart(self):
        """Verifies cart is empty"""
        empty_text = self.driver.find_element(*CartPageLocators.EMPTY_CART_DIV).text
        assert 'There are currently no items in your order.' in empty_text

    def click_continue(self):
        """Submits the form"""
        self.driver.find_element(*CartPageLocators.CONTINUE_BUTTON).click()

class ShippingPage(BasePage):
    """Shipping page methods belong here"""

    def enter_first_name(self, first_name):
        """Fills in first name"""
        self.driver.find_element(*ShippingPageLocators.FIRST_NAME_INPUT).send_keys(first_name)

    def enter_last_name(self, last_name):
        """Fills in last name"""
        self.driver.find_element(*ShippingPageLocators.LAST_NAME_INPUT).send_keys(last_name)

    def enter_address(self, address):
        """Fills in address for shipping"""
        self.driver.find_element(*ShippingPageLocators.ADDRESS_INPUT).send_keys(address)

    def enter_city(self, city):
        """Fills in city"""
        self.driver.find_element(*ShippingPageLocators.CITY_INPUT).send_keys(city)

    def select_state(self, state):
        select = Select(self.driver.find_element(*ShippingPageLocators.STATE_DROPDOWN))
        if state==None:
            state_number = randint(0,49)
            select.select_by_index(state_number)
        else:
            select.select_by_visible_text(state)

    def enter_email(self, email):
        """Fills in email"""
        self.driver.find_element(*ShippingPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_phone(self, phone):
        """Fills in phone information"""
        self.driver.find_element(*ShippingPageLocators.PHONE_INPUT).send_keys(phone)

    def select_state(self, country):
        select = Select(self.driver.find_element(*ShippingPageLocators.STATE_DROPDOWN))
        if country==None:
            random = randint(0,3)
            select.select_by_index(state_number)
        else:
            select.select_by_visible_text(country)

    def enter_zip_code(self, zipcode):
        """Fills in phone information"""
        self.driver.find_element(*ShippingPageLocators.ZIPCODE_INPUT).send_keys(zipcode)

    def click_continue(self):
        """Submits the form"""
        self.driver.find_element(*ShippingPageLocators.CONTINUE_BUTTON).click()

class VerificationPage(BasePage):
    """Verification page methods belong here"""

    def verify_unverified_information(self, first_name, last_name, address, city, zipcode, state='CA', country='US', company=None, address2=None):
        """Verifies the address information was entered correctly"""
        text_to_verify = self.driver.find_element(*VerificationPageLocators.UNVERIFIED_DIV).text
        assert first_name in text_to_verify
        assert last_name in text_to_verify
        assert address in text_to_verify
        assert city in text_to_verify
        assert zipcode in text_to_verify
        assert country in text_to_verify

