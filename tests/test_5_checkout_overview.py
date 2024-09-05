import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_base.sekret_sauce_test_base import BaseTest
from test_base.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.your_cart_page import YourCartPage
from pages.checkout_confirmation_page import CheckoutConfirmationPage
from pages.checkout_overview_page import CheckoutOverviewPage

class TestCheckoutOverview(BaseTest):

    def setUp(self):
        super().setUp()
        self.user = self.standard_user
        self.product_page = ProductPage(self.driver)
        self.product_page.navigate_to_product_page(self.user['username'], self.user['password'])
        self.product_page.add_product_to_cart(ProductPageLocators.ADD_BACKPACK)
        self.cart_page = self.product_page.go_to_cart(YourCartPage)
        self.checkout_confirmation_page = self.cart_page.proceed_to_checkout(CheckoutConfirmationPage)
        # przenieść do config
        self.checkout_confirmation_page.fill_information("First", "Last", "12345")
        self.checkout_overview_page = CheckoutOverviewPage(self.driver)

    def test_checkout_overview(self):
        self.checkout_overview_page.finish_checkout()
        confirmation_text = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.complete-header"))
        ).text
        self.assertIn('Thank you for your order!', confirmation_text)

if __name__ == "__main__":
    unittest.main()
