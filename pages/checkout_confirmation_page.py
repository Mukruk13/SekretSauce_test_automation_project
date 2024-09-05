
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_base.locators import CheckoutYourInformationLocators

class CheckoutConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_information(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(CheckoutYourInformationLocators.FIRST_NAME)
        ).send_keys(first_name)
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(CheckoutYourInformationLocators.LAST_NAME)
        ).send_keys(last_name)
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(CheckoutYourInformationLocators.POSTAL_CODE)
        ).send_keys(postal_code)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(CheckoutYourInformationLocators.CONTINUE_BUTTON)
        ).click()

    def submit_empty_form(self):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(CheckoutYourInformationLocators.CONTINUE_BUTTON)
        ).click()
