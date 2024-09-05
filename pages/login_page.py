from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_base.locators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(LoginPageLocators.USERNAME_INPUT)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

    def login(self, username, password):
        print("Navigating to login page")
        self.driver.get("https://www.saucedemo.com/")
        print("Page loaded, entering username")
        self.enter_username(username)
        print("Username entered, entering password")
        self.enter_password(password)
        print("Password entered, clicking login button")
        self.click_login_button()

    def get_error_message(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE)
        ).text
