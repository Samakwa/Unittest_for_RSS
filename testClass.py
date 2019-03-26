from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
import time
from utils import *


class LoginTest1(object):
    """
    LoginTest1 class.
    an helper class that his methods are responsible of testing the
    first step of assignment - the part of login
    """
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/sea0153/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path="C:/Users/sea0153/Downloads/chromedriver_win32/chromedriver.exe")
    def sign_in(self, username, password):
        """
        sign_in method.
        sign in to the menu
        :param username:
        :param password:
        :return: message of the result of login
        """
        self.driver.get("http://localhost:8082/#/")
        self.driver.find_element_by_name('loginEmail').send_keys(username)
        self.driver.find_element_by_name('loginPassword').send_keys(password)
        self.driver.find_element_by_css_selector('Submit').click()
        try:
            WebDriverWait(self.driver, TIME_WAIT_FOR_PAGE_LOAD).until(expected_conditions.title_contains('ScenarioList'))
        except Exception:
            err_elm = self.driver.find_element_by_xpath("//form/div[contains(@class, 'loginform')]").text
            return err_elm
        return 'Connected Successfully'

    def shutdown_driver(self):
        self.driver.close()

