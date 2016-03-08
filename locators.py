from selenium.webdriver.common.by import By

class CartPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    CONTINUE_BUTTON = (By.CLASS_NAME, 'button-continue')

    REMOVE_KIT_BUTTON = (By.CLASS_NAME, 'js-remove-last-kit')

    ADD_KIT_BUTTON = (By.CLASS_NAME, 'js-add-kit')

    KIT_NAME_INPUT_FIELD = (By.CLASS_NAME, 'js-kit-name')

    EMPTY_CART_DIV = (By.CLASS_NAME, 'cart-empty')

    CART_ROW = (By.CLASS_NAME, 'cart-item-row')

    TOTAL_ROW = (By.CLASS_NAME, 'total-row')

    ITEM_PRICE = (By.CLASS_NAME, 'item-price')

class ShippingPageLocators(object):
    """A class for shipping page locators. All checkout page locators should come here"""

    FIRST_NAME_INPUT = (By.ID, 'id_first_name')

    LAST_NAME_INPUT = (By.ID, 'id_last_name')

    COMPANY_INPUT = (By.ID, 'id_company')

    ADDRESS_INPUT = (By.ID, 'id_address')

    APARTMENT_NUMBER_INPUT = (By.ID, 'id_address2')

    CITY_INPUT = (By.ID, 'id_city')

    STATE_DROPDOWN = (By.ID, 'id_state')

    ZIPCODE_INPUT = (By.ID, 'id_postal_code')

    COUNTRY_DROPDOWN = (By.ID, 'id_country')

    SHIPPING_DROPDOWN = (By.ID, 'id_shipping_method')

    EMAIL_INPUT = (By.ID, 'id_email')

    PHONE_INPUT = (By.ID, 'id_int_phone')

    CONTINUE_BUTTON = (By.CLASS_NAME, 'button-continue')


class VerificationPageLocators(object):
    """A class for verification page locators"""

    UNVERIFIED_DIV = (By.CLASS_NAME, 'unverified')
