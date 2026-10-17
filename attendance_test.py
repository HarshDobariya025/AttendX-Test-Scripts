# AttendX - Attendance marking test (Selenium + unittest)
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class AttendanceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://attendx.example.com/attendance")  # demo URL

    def test_mark_present(self):
        d = self.driver
        d.find_element(By.ID, "student_101_present").click()
        d.find_element(By.ID, "submitAttendance").click()
        msg = d.find_element(By.ID, "successMsg").text
        self.assertIn("Attendance saved", msg)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()