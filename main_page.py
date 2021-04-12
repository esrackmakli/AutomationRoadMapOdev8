from selenium.webdriver.common.by import By
from BaseClass.base_class import BaseClass
from time import sleep


class MainPage:
    website = "http://www.amazon.com/"
    MAIN_PAGE_CONTROL = (By.ID, 'gw-card-layout')
    SIGN_IN_HOVER = (By.ID, 'nav-link-accountList')
    LOGIN_PAGE_NAVIGATE = (By.CLASS_NAME, 'nav-action-inner')
    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    word_to_search = "samsung"

    def __init__(self, driver):
        self.driver = driver
        self.functions = BaseClass(self.driver)

    def load_main_page(self):
        """
        loads the given website and checks if it loads successfully
        """
        self.driver.get(self.website)
        main_page_loaded = self.functions.exist_element(self.MAIN_PAGE_CONTROL)
        assert main_page_loaded, "didn't loaded main page!"

    def load_login_page(self):
        """
        loads the login page
        """
        sleep(2)
        self.functions.hover_element(self.SIGN_IN_HOVER)
        self.functions.wait_for_element(self.LOGIN_PAGE_NAVIGATE).click()

    def search_amazon(self):
        """
        It enters the searchbar and searches for the word to be searched.
        """
        self.functions.wait_for_element(self.SEARCH_BAR).send_keys(self.word_to_search)
        self.functions.wait_for_element(self.SEARCH_BUTTON).click()
