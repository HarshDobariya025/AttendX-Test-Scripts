# AttendX - Login test (Selenium + unittest)
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://attendx.example.com/login")  # demo URL

    def test_valid_login(self):
        d = self.driver
        d.find_element(By.ID, "username").send_keys("teacher01")
        d.find_element(By.ID, "password").send_keys("Pass@123")
        d.find_element(By.ID, "loginBtn").click()
        self.assertIn("Dashboard", d.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()