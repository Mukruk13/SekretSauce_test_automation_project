
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_base.locators import CheckoutOverviewLocators

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def finish_checkout(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(CheckoutOverviewLocators.FINISH_BUTTON)
        ).click()
