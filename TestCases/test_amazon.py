import unittest
from selenium import webdriver
from PageClasses.main_page import MainPage
from BaseClass.base_class import BaseClass
from PageClasses.login_page import LoginPage
from PageClasses.search_page import SearchPage
from PageClasses.product_page import ProductPage
from PageClasses.wishlist_page import WishlistPage


class TestAmazon(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/esra.cakmakli/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver.maximize_window()
        self.base_class = BaseClass(self.driver)
        self.amazon_main = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.wishlist_page = WishlistPage(self.driver)

    def test_amazon(self):
        self.amazon_main.load_main_page()
        self.amazon_main.load_login_page()
        self.login_page.login_amazon()
        self.amazon_main.search_amazon()
        self.search_page.search_result()
        self.search_page.second_page_click()
        self.search_page.third_product_click()
        self.product_page.add_to_list_click()
        self.product_page.create_button_click()
        self.product_page.close_button_click()
        self.product_page.go_to_shopping_list()
        self.wishlist_page.is_there_wishlist_product()
        self.wishlist_page.wishlist_delete()
