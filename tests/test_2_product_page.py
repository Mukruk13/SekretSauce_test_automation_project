import unittest
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_base.sekret_sauce_test_base import BaseTest
from test_base.locators import ProductPageLocators
from pages.product_page import ProductPage

class TestProductPage(BaseTest):

    def setUp(self):
        super().setUp()
        self.user = self.standard_user
        self.product_page = ProductPage(self.driver)
        self.product_page.navigate_to_product_page(self.user['username'], self.user['password'])

    def test_add_and_remove_random_product(self):
        print("Adding random product to cart")

        # zwraca widok obiektu klucz-wartosc
        random_product_locator, product_name = random.choice(list(ProductPageLocators.ADD_PRODUCT_LOCATORS.items()))

        self.product_page.add_product_to_cart(random_product_locator)

        # sprawdzenie, czy guzik zmienił się na "Remove"
        remove_locator = ProductPageLocators.REMOVE_PRODUCT_LOCATORS[product_name]
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(remove_locator)
        )
        print(f"Product added: {product_name}")
        print("Removing product from cart")
        self.product_page.remove_product_from_cart(remove_locator)


        # sprawdzenie, czy guzik zmienił się na "Add"
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(random_product_locator)
        )
        print(f"Product removed: {product_name}")

if __name__ == "__main__":
    unittest.main()
