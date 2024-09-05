from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from test_base.locators import ProductPageLocators, LoginPageLocators

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_product_page(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 30).until(
            EC.url_contains("inventory.html")
        )

    def add_product_to_cart(self, product_locator):
        try:
            self.driver.find_element(*product_locator).click()
        except NoSuchElementException:
            for name, remove_locator in ProductPageLocators.REMOVE_PRODUCT_LOCATORS.items():
                try:
                    self.driver.find_element(*remove_locator).click()
                except NoSuchElementException:
                    continue
            self.driver.find_element(*product_locator).click()

    def remove_product_from_cart(self, remove_locator):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(remove_locator)
        ).click()

    def go_to_cart(self, your_cart_page_class):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(ProductPageLocators.CART)
        ).click()
        return your_cart_page_class(self.driver)

    def reset_cart(self):
        for name, remove_locator in ProductPageLocators.REMOVE_PRODUCT_LOCATORS.items():
            try:
                element = self.driver.find_element(*remove_locator)
                if element.is_displayed():
                    element.click()
            except NoSuchElementException:
                continue
