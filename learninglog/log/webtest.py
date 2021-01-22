import unittest
from selenium.webdriver import chrome

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = chrome.webdriver.WebDriver.get(self,"http://localhost:5000")
    def testOne(self):
        self.shortDescription()

if __name__ == '__main__':
    unittest.main()
