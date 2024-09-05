from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_base.locators import CheckoutCompleteLocators

class CheckoutCompletePage:

    def __init__(self, driver):
        self.driver = driver

    def back_to_home(self):
        # Dodanie oczekiwania na załadowanie strony
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(CheckoutCompleteLocators.BACK_TO_PRODUCTS_BUTTON)
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CheckoutCompleteLocators.BACK_TO_PRODUCTS_BUTTON)).click()
