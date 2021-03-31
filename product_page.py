from selenium.webdriver.common.by import By
from BaseClass.base_class import BaseClass
from time import sleep


class ProductPage:
    ADD_TO_LIST_BUTTON = (By.ID, 'wishlistButtonStack')
    CREATE_BUTTON = (By.ID, "wl-redesigned-create-list")
    ADDED_TO_LIST = (By.XPATH, "//span[contains(text(),'1 item added to Shopping List')]")
    CONTINUE_SHOPPING = (By.XPATH, "//button[contains(text(),'Continue shopping')]")
    SHOPPING_LIST = (By.XPATH, "//span[contains(text(),'Shopping List')]")
    ACCOUNT_AND_LIST = (By.ID, "nav-link-accountList")
    text = "1 item added to Shopping List"

    def __init__(self, driver):
        self.driver = driver
        self.functions = BaseClass(self.driver)

    def add_to_list_click(self):
        self.functions.wait_for_element(self.ADD_TO_LIST_BUTTON).click()

    def create_button_click(self):
        self.functions.wait_for_element(self.CREATE_BUTTON).click()
        added_to_list = self.functions.wait_for_element(self.ADDED_TO_LIST).text
        assert added_to_list == self.text, "ürün listeye eklenemedi!"

    def close_button_click(self):
        self.functions.wait_for_element(self.CONTINUE_SHOPPING).click()

    def go_to_shopping_list(self):
        sleep(2)
        self.functions.hover_element(self.ACCOUNT_AND_LIST)
        self.functions.wait_for_element(self.SHOPPING_LIST).click()
