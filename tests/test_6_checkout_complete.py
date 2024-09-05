import unittest
from test_base.sekret_sauce_test_base import BaseTest
from test_base.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.your_cart_page import YourCartPage
from pages.checkout_confirmation_page import CheckoutConfirmationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

class TestCheckoutComplete(BaseTest):

    def setUp(self):
        super().setUp()
        self.user = self.standard_user
        self.product_page = ProductPage(self.driver)
        self.product_page.navigate_to_product_page(self.user['username'], self.user['password'])
        self.product_page.add_product_to_cart(ProductPageLocators.ADD_BACKPACK)
        self.cart_page = self.product_page.go_to_cart(YourCartPage)
        self.checkout_confirmation_page = self.cart_page.proceed_to_checkout(CheckoutConfirmationPage)
        self.checkout_confirmation_page.fill_information("First", "Last", "12345")
        self.checkout_overview_page = CheckoutOverviewPage(self.driver)
        self.checkout_overview_page.finish_checkout()
        self.checkout_complete_page = CheckoutCompletePage(self.driver)

    def test_back_to_home(self):
        self.checkout_complete_page.back_to_home()
        assert "Swag Labs" in self.driver.title

if __name__ == "__main__":
    unittest.main()
