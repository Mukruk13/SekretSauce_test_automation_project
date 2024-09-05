from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_base.locators import YourCartLocators

class YourCartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        items = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((YourCartLocators.INVENTORY_ITEM_NAME))
        )
        return [item.text for item in items]

    def remove_product_from_cart(self, remove_locator):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(remove_locator)
        ).click()
        WebDriverWait(self.driver, 30).until_not(
            EC.element_to_be_clickable(remove_locator)
        )

    def continue_shopping(self, product_page_class):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(YourCartLocators.CONTINUE_SHOPPING)
        ).click()
        return product_page_class(self.driver)

    def proceed_to_checkout(self, checkout_confirmation_page_class):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(YourCartLocators.CHECKOUT_BUTTON)
        ).click()
        return checkout_confirmation_page_class(self.driver)
