import unittest
from test_base.sekret_sauce_test_base import BaseTest
from pages.login_page import LoginPage


class TestLoginPage(BaseTest):

    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)

    def test_navigate_to_login_page(self):
        self.driver.get(self.config['urls']['login'])
        self.assertIn("Swag Labs", self.driver.title)

    def test_login_users(self):
        for user in self.users:
            username = user['username']
            password = user['password']
            self.login_page.login(username, password)

            if username == 'locked_out_user':
                error_message = self.login_page.get_error_message()
                self.assertIn("Epic sadface: Sorry, this user has been locked out.", error_message)
            else:
                self.assertIn(self.config['urls']['inventory'], self.driver.current_url)
            self.driver.get(self.config['urls']['login'])  # Reset before next login attempt


if __name__ == "__main__":
    unittest.main()
