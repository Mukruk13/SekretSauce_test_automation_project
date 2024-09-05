import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = load_config()
        options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        cls.driver.maximize_window()
        cls.users = cls.config['users']
        cls.standard_user = next(user for user in cls.users if user['username'] == 'standard_user')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
