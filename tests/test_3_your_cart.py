import unittest
import random
from test_base.sekret_sauce_test_base import BaseTest
from test_base.locators import ProductPageLocators, YourCartLocators
from pages.product_page import ProductPage
from pages.your_cart_page import YourCartPage

class TestYourCartPage(BaseTest):

    def setUp(self):
        super().setUp()
        self.user = self.standard_user
        self.product_page = ProductPage(self.driver)
        self.product_page.navigate_to_product_page(self.user['username'], self.user['password'])
        random_product_locator, self.product_name = random.choice(list(ProductPageLocators.ADD_PRODUCT_LOCATORS.items()))
        self.product_page.add_product_to_cart(random_product_locator)
        self.cart_page = self.product_page.go_to_cart(YourCartPage)

    def test_remove_product_from_cart(self):
        # Sprawdzenie, czy przedmiot został dodany do koszyka
        cart_items = self.cart_page.get_cart_items()
        self.assertIn(self.product_name, cart_items)

        # Usunięcie przedmiotu z koszyka
        remove_locator = YourCartLocators.REMOVE_PRODUCT_LOCATORS[self.product_name]
        self.cart_page.remove_product_from_cart(remove_locator)


if __name__ == "__main__":
    unittest.main()
