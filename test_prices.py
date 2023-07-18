from Page.main_page import Main_Page
from Page.category_prices import Category_Prices
from test_data import test_data
import logging


def test(driver):
    main_page = Main_Page(driver)
    main_page.open_page()
    main_page.choose_language()
    category_prices = Category_Prices(driver)

    prices = category_prices.get_prices()
    for price in prices:
        splited = (price.text).split(" ")
        number = int(splited[0].replace(',', ''))
        assert int(test_data["price_from"]) <= number <= int(
            test_data["price_to"]), logging.error("Fail")
    logging.info("Test is passed!!")
