from selenium.webdriver.common.by import By
from BaseClass.base_class import BaseClass


class SearchPage:
    SEARCH_RESULT = (By.XPATH, '//span[contains(text(),"samsung")]')
    SECOND_PAGE = (By.CLASS_NAME, 'a-normal')
    IS_SECOND_PAGE = (By.LINK_TEXT, "2")
    THIRD_PRODUCT = (By.CSS_SELECTOR, '.a-section.aok-relative.s-image-fixed-height')
    THIRD_PRODUCT_CLICKED = (By.ID, 'breadcrumb-back-link')
    name = "samsung"

    def __init__(self, driver):
        self.driver = driver
        self.functions = BaseClass(self.driver)

    def search_result(self):
        """
        Checks if there are any results for the searched word
        """
        result = self.functions.exist_element(self.SEARCH_RESULT)
        assert result, "didn't found for searched word! "

    def second_page_click(self):
        """
        loads the second page on the search page and checks it
        """
        self.functions.wait_for_element(self.SECOND_PAGE).click()
        is_second_page = self.functions.exist_element(self.IS_SECOND_PAGE)
        assert is_second_page, "the second page could not be reached!"

    def third_product_click(self):
        """
        Clicks the third product on the second page and checks it
        """
        self.functions.wait_for_elements(self.THIRD_PRODUCT)[2].click()
        third_product_clicked = self.functions.wait_for_element(self.THIRD_PRODUCT_CLICKED)
        assert third_product_clicked, "didn't clicked product"
