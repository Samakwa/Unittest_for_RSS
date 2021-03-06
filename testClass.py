from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
import time
from utils import *


class TestUnit1(object):
    """
    LoginTest1 class.
    Tests codes related to sign_in section
    """
    def __init__(self, username):
        #self.driver = webdriver.Chrome(executable_path="C:/Users/sea0153/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path="C:/Users/sea0153/Downloads/chromedriver_win32/chromedriver.exe")

    def sign_in(self, username, password):
        """
        sign_in method.

        """
        self.driver.get("http://localhost:8082/#/")
        self.driver.find_element_by_name('email').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_css_selector('Submit').click()
        try:
            WebDriverWait(self.driver, TIME_WAIT_FOR_PAGE_LOAD).until(expected_conditions.title_contains('ScenarioList'))
        except Exception:
            err_elm = self.driver.find_element_by_xpath("//form/div[contains(@class, 'loginform')]").text
            return err_elm
        return 'Connected Successfully'

    def test_Heading(self):
        heading = self.driver.title

        assert heading == "RE-PLAN"

    #def shutdown_driver(self):
     #   self.driver.close()


    #class TestUnit2(object):

    #user class represents a given user.


    def test_registration(self, args_for_user):
        self.email = args_for_user[EMAIL]
        self.password = args_for_user[PASSWORD]
        self.name = args_for_user[NAME]
        self.organisation = args_for_user[ORGANISATION]
        self.password_1 = args_for_user[PASSWORD_1]
        self.password_2 = args_for_user[PASSWORD_2]

    def registration2(self, email, password_1, name,organization, password_2):
        self.driver.get("http://localhost:8082/#/")
        self.driver.find_element_by_name('email').send_keys(email)
        self.driver.find_element_by_name('Name').send_keys(name)
        self.driver.find_element_by_name('Organization').send_keys(organization)
        self.driver.find_element_by_name('Password').send_keys(password_1)
        self.driver.find_element_by_name('Confirm Password').send_keys(password_2)
        self.driver.find_element_by_css_selector('REGISTER').click()
        try:
            WebDriverWait(self.driver, TIME_WAIT_FOR_PAGE_LOAD).until(expected_conditions.title_contains('Create User Account'))
        except Exception:
            err_elm = self.driver.find_element_by_xpath("//form/div[contains(@class, 'registerform')]").text
            return err_elm
        return 'User is successfully registered'
    def tearDown(self):
        self.driver.close()

    #class TestUnit3(object):


    def add_new_user(self, user) -> list:

        self.entry()
        self.add_new_user(user)
        res, notes = self.add_user(user)
        if not res:
            return notes
        WebDriverWait(self.driver, TIME_WAIT_FOR_PAGE_LOAD).until(expected_conditions.title_contains('user/addNewUser'))
        if not self.check_if_user_added(user):
            notes.append('User not added')
            return notes
        notes.append('user Added Successfully')
    def delete_user(self, user) -> str:
        """
        delete user. Using given user details, search and delete user
        :param user:
        :return:
        """
        flag = False    # not found
        path1 = "//td[contains(text(), '" + user.name + "')]"
        path2 = "//td[contains(text(), '" + user.email + "')]"

        i = 1           # starting with page 1
        while i < NUMBER_OF_PAGES:
            elements_in_table = self.driver.find_elements_by_xpath("//tbody/tr")
            for element in elements_in_table:
                if self.checkIfPath_exist(path1, element) and self.checkIfPath_exist(path2, element) :
                    element.find_element_by_xpath("//td/span/a[@title='DELETE']").click()
                    wait = WebDriverWait(self.driver, TIME_WAIT_FOR_PAGE_LOAD)
                    wait.until(expected_conditions.alert_is_present())
                    alert = self.driver.switch_to.alert
                    alert.accept()
                    flag = True
                    break
            if flag:
                break
            i += 1
            self.driver.find_element_by_xpath("//li/a[text()='{}']".format(i)).click()
            WebDriverWait(self.driver, TIME_WAIT_FOR_PAGE_LOAD).until(expected_conditions.title_contains('UserSettings'))
        return 'Success' if flag else 'Fail'

    def checkIfPath_exist(self, path, driver=None) -> bool:
        """
        is_x_path method.
        check if xpath expression is exist. if it doesnt find it, it raises error message
        """
        try:
            driver = self.driver if driver is None else driver
            driver.find_element_by_xpath(path)
        except Exception as e:
            print(e)
            return False
        return True

    def check_if_user_added(self, user) -> bool:

        path_email = "//tr/td[text()='"+str(user.email)+"']"
        path_name = "//tr/td[text()='"+str(user.name)+"']"
        path_orga = "//tr/td[text()='" + str(user.organisation) + "']"
        path_password_1 = "//tr/td/a[text()='" + str(user.password) + "']"
        return self.checkIfPath_exist(path_email) and self.checkIfPath_exist(path_name) and self.checkIfPath_exist(path_orga)and self.checkIfPath_exist(path_password_1)

    def entry(self):
        """
        entry method.
        enter to the main menu with the correct username and password.
        :return:
        """
        self.driver.get("http://localhost:8082/#/")
        self.driver.find_element_by_name('email').send_keys('15@15.com')
        self.driver.find_element_by_name('password').send_keys('password1')
        self.driver.find_element_by_css_selector('Submit').click()
        WebDriverWait(self.driver, TIME_WAIT_FOR_PAGE_LOAD).until(expected_conditions.title_contains('Dashboard'))

    def add_user(self, user) -> (bool, list):
        """
        add_user method.
        add a user to table.
        :param user:
        :return:
        """
        add_button_path = "//div/form/button[contains(text(), 'Add')]"
        self.driver.find_element_by_xpath(add_button_path).click()
        self.driver.find_element_by_xpath("//input[@name='address1']").send_keys(user.address_1)
        self.driver.find_element_by_xpath("//input[@name='address2']").send_keys(user.address_2)
        elements = self.driver.find_element_by_xpath("//div[@class ='panel-body']")
        self._fill_fields(elements, user)
        self.driver.find_element_by_css_selector('button').click()
        try:
            WebDriverWait(self.driver, TIME_WAIT_FOR_PAGE_LOAD).until(
                expected_conditions.title_contains("UserSetting"))
        except Exception:
            return False, self._check_reason_of_fail()
        return True, []

    def _check_reason_of_fail(self) -> list:
        """
        check_reason_of_fail method.
        retrieve the reasons which the addition of user failed and return
        it in a list
        :return: list of warnings
        """
        str_alerts = []
        alerts = self.driver.find_elements_by_xpath("//div[@class='alert alert-danger']/p")
        for alert in alerts:
            str_alerts.append(alert.text)
        return str_alerts

    def _fill_fields(self, elements, user):

        list_of_forms = elements.find_elements_by_xpath("C:/Users/sea0153/WebstormProjects/Sampson_backend/src/main")

        list_of_forms[EMAIL_ADD].send_keys(user.userEmail)
        list_of_forms[NAME].send_keys(user.userName)
        list_of_forms[ORGANISATION].send_keys(user.userOrganization)
        list_of_forms[PASSWORD_1].send_keys(user.registerPassword)
        list_of_forms[PASSWORD_2].send_keys(user.ConfirmPassword)



    def scenario(self):
        """
        Check if a new scenario is returned
        """
        self.driver.get("http://localhost:8082/#/ScenarioList")
        self.driver.find_element_by_name('email').send_keys('15@15.com')
        self.driver.find_element_by_name('password').send_keys('password1')
        self.driver.find_element_by_xpath("//a[contains(text(), 'LOAD SCENARIO')]").click()
        WebDriverWait(self.driver, TIME_WAIT_FOR_PAGE_LOAD).until(expected_conditions.title_contains('Scenario'))

    def tearDown(self):
        self.driver.close()

    def shutdown_driver(self):
        """
        shutdown_driver method.
        close the driver
        :return: void
        """
        self.driver.close()
