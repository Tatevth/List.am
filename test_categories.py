from Page.main_page import Main_Page
from Page.home_page import Home
import logging


def test(driver):
    main_page = Main_Page(driver)
    main_page.open_page()
    home = Home(driver)
    els = home.get_categories()
    for el in els:
        txt = el.text
        el.click()
        cat_name = home.find_text(home.cat_name)
        assert txt == cat_name, logging.error("FAIL")
        logging.info("Pass")


# Anna jan,
# > where should I put try/except
# > I have an error - StaleElementReferenceException: , I understand the issue , but can't solve it,
# > Why doesn't the logging work?
