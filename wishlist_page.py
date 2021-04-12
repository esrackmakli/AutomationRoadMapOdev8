from selenium.webdriver.common.by import By
from BaseClass.base_class import BaseClass


class WishlistPage:
    WISHLIST_PAGE = (By.ID, "wishlist-page")
    WISHLIST_PRODUCT = (By.CLASS_NAME, "g-span12when-narrow")
    WISHLIST_DELETE_BUTTON = (By.XPATH, '//span[@class="a-button-inner"]//input[@name="submit.deleteItem"]')
    DELETED = (By.CLASS_NAME, 'a-alert-inline-success')

    def __init__(self, driver):
        self.driver = driver
        self.functions = BaseClass(self.driver)

    def is_there_wishlist_product(self):
        wishlist_product = self.functions.wait_for_element(self.WISHLIST_PRODUCT)
        assert wishlist_product, "wishlistte urun yok!"

    def wishlist_delete(self):
        self.functions.wait_for_element(self.WISHLIST_DELETE_BUTTON).click()
        deleted = self.functions.wait_for_element(self.DELETED)
        assert deleted, "ürün wishlistten silinemedi!"
