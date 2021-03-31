from selenium.webdriver.common.by import By
from BaseClass.base_class import BaseClass


class SearchPage:
    SEARCH_RESULT = (By.XPATH, '//span[contains(text(),"samsung")]')
    SECOND_PAGE = (By.CLASS_NAME, 'a-normal')
    IS_SECOND_PAGE = (By.XPATH, "//li[@class='a-selected']/a[contains(text(),'2')]")
    THIRD_PRODUCT = (By.XPATH, '//*[@data-index="3"]//img')
    THIRD_PRODUCT_CLICKED = (By.ID, 'breadcrumb-back-link')
    name = "samsung"

    def __init__(self, driver):
        self.driver = driver
        self.functions = BaseClass(self.driver)

    def search_result(self):
        result = self.functions.exist_element(self.SEARCH_RESULT)
        assert result, "aranan urun için sonuc bulunamadı! "

    def second_page_click(self):
        self.functions.wait_for_element(self.SECOND_PAGE).click()
        is_second_page = self.functions.exist_element(self.IS_SECOND_PAGE)
        assert is_second_page, "ikinci sayfaya ulasamadin!"

    def third_product_click(self):
        self.functions.wait_for_element(self.THIRD_PRODUCT).click()
        third_product_clicked = self.functions.wait_for_element(self.THIRD_PRODUCT_CLICKED)
        assert third_product_clicked, "urune tiklanamadi!"
