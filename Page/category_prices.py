from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver
from test_data import test_data


class Category_Prices(General_Helper):

    electronics = (By.XPATH, "//div[@data-c='4']//a[text()='Electronics']")
    mobile_phones = (By.XPATH, "//div[@data-c='4']//a[text()='Mobile Phones']")
    price_from = (By.XPATH, "//input[@id='idprice1']")
    price_to = (By.XPATH, "//input[@id='idprice2']")
    currency = (
        By.XPATH, "//div[text()='Currency']//parent::div//child::div[@class='me']")
    go_btn = (By.XPATH, "//img[@id='gobtn']")
    prices = (By.XPATH, "//div[@class='p']")
    amd = (By.XPATH, "//div[@data-value='0']")

    def get_prices(self):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.find(self.electronics)).perform()
        self.find_and_click(self.mobile_phones)
        self.find_and_send_keys(self.price_from, test_data["price_from"])
        self.find_and_send_keys(self.price_to, test_data["price_to"])
        self.find_and_click(self.currency)
        self.find_and_click(self.go_btn)
        self.find_and_click(self.amd)
        prices = self.find_elements(self.prices)
        return prices
