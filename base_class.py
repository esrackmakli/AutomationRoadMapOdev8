from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 45)

    def wait_for_element(self, selector):
        return self.wait.until(ec.element_to_be_clickable(selector))

    def exist_element(self, selector, multiple=False):
        """
        Return true if element/elements present and false if element/elements absent
        :param selector: locator of the element to find
        :param multiple: False in default, if True returns the list of WebElements once they are located

        """
        if not multiple:
            try:
                self.wait.until(ec.presence_of_element_located(selector))
                return True
            except TimeoutException:
                return False
        else:
            try:
                self.wait.until(ec.presence_of_all_elements_located(selector))
                return True
            except TimeoutException:
                return False

    def hover_element(self, selector):
        """
        Hover over the selected element
        :param selector: locator of the element to find

        """
        hover_element = self.wait_for_element(selector)
        hover = ActionChains(self.driver).move_to_element(hover_element)
        hover.perform()
