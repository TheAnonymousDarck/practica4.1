import HtmlTestRunner
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from decouple import config


class TestDragAndDrop(unittest.TestCase):
    def setUp(self):
        self.site = config('URL_SCRAPPING')
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)
        self.answers = {
            '//*[@id="box1"]': '//*[@id="box101"]',
            '//*[@id="box2"]': '//*[@id="box102"]',
            '//*[@id="box3"]': '//*[@id="box103"]',
            '//*[@id="box4"]': '//*[@id="box104"]',
            '//*[@id="box5"]': '//*[@id="box105"]',
            '//*[@id="box6"]': '//*[@id="box106"]',
            '//*[@id="box7"]': '//*[@id="box107"]',
        }
        # time.sleep(2)

    def test_drag_and_drop(self):
        self.driver.get(self.site)
        self.driver.maximize_window()

        for key, value in self.answers.items():
            element = self.driver.find_element(By.XPATH, key)
            target = self.driver.find_element(By.XPATH, value)
            self.action.drag_and_drop(element, target).perform()
            time.sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
