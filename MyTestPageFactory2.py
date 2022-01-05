from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver
import unittest

class BasePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver


    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def waitVisibilityOfElement(self, second, element):
        wait = WebDriverWait(self.driver, second)
        wait.until(EC.element_to_be_clickable((By.XPATH, element)))

class HomePage(BasePage):

    locators = {
        "bottom_mi": ('XPATH', "//img [contains(@src,'mi-brand')]")
    }

    def clickButtonMi(self):
        self.bottom_mi.click()

class XiaomiPage(BasePage):

    SEARCH_RESULT_PRODUCT = "//article [@class='brand__item']"

    locators = {
        "search_result_product": ('XPATH', "//article [@class='brand__item']")
    }

    def getElementsList(self):
        return len(self.driver.find_elements_by_xpath(self.SEARCH_RESULT_PRODUCT))

    # def getElementsList(self):
    #     return self.search_result_product.get_list_item_count()

class PhonesAndAccessoriesPage(BasePage):

    locators = {
        "button_smartphones": ('XPATH', "//div/a[@href='https://avic.ua/smartfonyi']")
    }

    def clickButtonSmartphones(self):
        self.button_smartphones.click()

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
    unittest.main()