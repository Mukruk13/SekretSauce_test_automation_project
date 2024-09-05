import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_base.sekret_sauce_test_base import BaseTest
from test_base.locators import ProductPageLocators, CheckoutYourInformationLocators
from pages.product_page import ProductPage
from pages.your_cart_page import YourCartPage
from pages.checkout_confirmation_page import CheckoutConfirmationPage

class TestCheckoutConfirmation(BaseTest):

    def setUp(self):
        super().setUp()
        self.user = self.standard_user
        self.product_page = ProductPage(self.driver)
        self.product_page.navigate_to_product_page(self.user['username'], self.user['password'])
        self.product_page.reset_cart()
        self.product_page.add_product_to_cart(ProductPageLocators.ADD_BACKPACK)
        self.cart_page = self.product_page.go_to_cart(YourCartPage)
        self.checkout_confirmation_page = self.cart_page.proceed_to_checkout(CheckoutConfirmationPage)

    def test_checkout_confirmation(self):
        self.checkout_confirmation_page.fill_information("First", "Last", "12345")
        WebDriverWait(self.driver, 30).until(
            EC.url_contains(self.config['urls']['checkout_step_two'])
        )
        self.assertIn("Checkout: Overview", self.driver.page_source)

    def test_checkout_confirmation_with_empty_fields(self):
        # Przejście do strony potwierdzenia zamówienia bez wypełniania formularza
        self.checkout_confirmation_page.submit_empty_form()

        # Sprawdzenie, czy komunikat błędu jest wyświetlany
        error_message = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(CheckoutYourInformationLocators.ERROR_MESSAGE)
        ).text
        expected_error_message = "Error: First Name is required"
        self.assertEqual(error_message, expected_error_message)

if __name__ == "__main__":
    unittest.main()
