from selenium.webdriver.common.by import By
from BaseClass.base_class import BaseClass


class LoginPage:
    email = ''
    password = ''
    EMAIL_TEXT = (By.ID, 'ap_email')
    CONTINUE_BUTTON = (By.ID, 'continue')
    PASSWORD_TEXT = (By.ID, 'ap_password')
    SIGN_IN_BUTTON = (By.ID, 'signInSubmit')

    def __init__(self, driver):
        self.driver = driver
        self.functions = BaseClass(self.driver)

    def login_amazon(self):
        """
        logins to site with given email and password
        
        """
        self.functions.wait_for_element(self.EMAIL_TEXT).send_keys(self.email)
        self.functions.wait_for_element(self.CONTINUE_BUTTON).click()
        self.functions.wait_for_element(self.PASSWORD_TEXT).send_keys(self.password)
        self.functions.wait_for_element(self.SIGN_IN_BUTTON).click()
