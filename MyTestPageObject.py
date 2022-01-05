from page_factory.internet_example.pageobject_support import callable_find_by as find_by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest
import pytest

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def waitVisibilityOfElement(self, second, element):
        wait = WebDriverWait(self.driver, second)
        wait.until(EC.element_to_be_clickable((By.XPATH, element)))

class HomePage(BasePage):

    BUTTOM_MI = "//img [contains(@src,'mi-brand')]"

    def clickButtonMi(self):
        self.driver.find_element_by_xpath(self.BUTTOM_MI).click()

class XiaomiPage(BasePage):

    SEARCH_RESULT_PRODUCT = "//article [@class='brand__item']"

    def getElementsList(self):
        return len(self.driver.find_elements_by_xpath(self.SEARCH_RESULT_PRODUCT))

class PhonesAndAccessoriesPage(BasePage):
    BUTTON_SMARTPHONES = "//div/a[@href='https://avic.ua/smartfonyi']"

    def clickButtonSmartphones(self):
        self.driver.find_element_by_xpath(self.BUTTON_SMARTPHONES).click()

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://avic.ua/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def getHomePage(self):
        return HomePage(self.driver)

    def getXiaomiPage(self):
        return XiaomiPage(self.driver)


class XiaomiPageTest(BaseTest):

    def test_ButtonMi(self):
        NUMBER_ELEMENT_PRODUCT = 45
        home_page = self.getHomePage()
        home_page.clickButtonMi()
        home_page.implicitly_wait(30)
        number = self.getXiaomiPage().getElementsList()
        assert NUMBER_ELEMENT_PRODUCT == number

if __name__ == "__main__":
    # pytest.main(["-x", "tests/home_page_test.py"])
    pytest.main(["-x"])