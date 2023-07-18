from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By


class Home(General_Helper):

    welcome_form = (By.XPATH, "//div[@id='dlgLangSel']")
    english = (By.XPATH, "//div[@id='dlgLangSel']//a[@href='/en/']")
    categories = (By.XPATH, "//div[@data-c='0']//div[@class='c']//span")
    all_cat_field = (By.XPATH, "//span[text()='All Categories']")
    cat_name = (By.XPATH, "//div[@id='crumb']//child::span[@itemprop='name']")

    def get_categories(self):
        self.find_and_click(self.english)
        # action = webdriver.ActionChains(self.driver)
        # action.move_to_element(self.find(self.all_cat_field)).perform()
        self.find_and_click(self.all_cat_field)
        elements = self.find_elements(self.categories)
        return elements
