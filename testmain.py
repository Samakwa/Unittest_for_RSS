import time
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.common.keys import Keys
import unittest
from utils import Util
from unittest import TestLoader, TextTestRunner, TestSuite
from testClass import *
from pyunitreport import HTMLTestRunner
#import HtmlTestRunner
import HTMLTestRunner


from jinja2 import Template
from unittest import TestResult, TextTestResult



"""
Login class.
include all Tests that are related to the login window
"""
loc1 = os.getcwd()

class Unit1(unittest.TestCase):
    # set the environment for tests
    def setUp(self):
        self.tester = TestUnit1()
        self.util = Util()
        self.util.start('inputs')


    # Test 1
    def test_check_LoginDetails(self):
        try:
            self.assertEqual('Connected Successfully', self.tester.sign_in(
                self.util.mapper[ARGS_FOR_TEST_1][LOGIN_MAIL], self.util.mapper[ARGS_FOR_TEST_1][LOGIN_PASS]))
        except Exception as e:
            print('Test 1 Failed Because ' + str(e))

    # Test 2
    def test_wrong_credentials(self):
        try:
            self.assertEqual('Invalid Login Credentials', self.tester.sign_in(
                self.util.mapper[ARGS_FOR_TEST_2][LOGIN_MAIL], self.util.mapper[ARGS_FOR_TEST_2][LOGIN_PASS]))
        except Exception as e:
            print('Test 2 Failed Because ' + str(e))


    # Test 3
    def test_email_validity(self):
        expected_res = 'The Email field must contain a valid email address.'
        try:
            self.assertEqual(expected_res, self.tester.sign_in(
                self.util.mapper[ARGS_FOR_TEST_3][LOGIN_MAIL], self.util.mapper[ARGS_FOR_TEST_3][LOGIN_PASS]))
        except Exception as e:
            print('Test 3 Failed because ' + str(e))

    # Test 4
    def test_blank_details(self):
        try:
            self.assertFalse(self.tester.sign_in(
                self.util.mapper[ARGS_FOR_TEST_4][EMAIL], self.util.mapper[ARGS_FOR_TEST_4][PASSWORD_1]))
        except Exception as e:
            print('Test 4 Failed because ' + str(e))

        #self.driver.save_screenshot('screenshot-deskto-chrome.png')
    def tearDown(self):
        self.tester.shutdown_driver()


    """
    Unit2 class.
    include all tests that related to the action of add and delete a user
    """

    """
    class Unit2(unittest.TestCase):

    def setUp(self):
        self.tester = TestUnit2()
        self.util = Util()
        self.util.start('inputs')
    """
    # Test 5
    def test_add_user_with_short_password(self):
        try:
            user1 = (self.util.mapper[ARGS_FOR_TEST_5])
            array_of_errors = self.tester.user(user1)
            self.assertIn('The Password field must be at least 6 characters in length.', array_of_errors)
        except Exception as e:
            print('Test 5 Failed because ' + str(e))

    # Test 6
    def test_add_user_with_name_field_missing(self):
        try:
            user1 = (self.util.mapper[ARGS_FOR_TEST_6])
            array_of_errors = self.tester.add_new_user(user1)
            self.assertIn('The First Name field is required.', array_of_errors)
        except Exception as e:
            print('Test 6 Failed because' + str(e))

    # Test 7
    def test_add_user_correctly(self):
        try:
            user1 = (self.util.mapper[ARGS_FOR_TEST_7])
            array_of_notes = self.tester.add_new_user(user1)
            self.assertIn('user Added Successfully', array_of_notes)
        except Exception as e:
            print('Test 7 Failed because ' + str(e))

    # Test 8
    def test_if_user_deleted_successfully(self):
        try:
            user = (self.util.mapper[ARGS_FOR_TEST_8])
            self.tester.entry()
            self.tester.activeUsers.update()
            self.assertEqual('Success', self.tester.delete_user(user))
        except Exception as e:
            print('Test 7 Failed because ' + str(e))

    def test_succesful_log_out(self):
        try:
            self.tester.entry()
            self.sign_out()
        except Exception as e:
            print('Test 8 Failed because ' + str(e))

    def tearDown(self):
        self.tester.shutdown_driver()

    """
    Unit3 class.
    include Scenario creation 
    """


    #class Unit3(unittest.TestCase):
    """
    def setUp(self):
        self.tester = TestUnit3()
        self.util = Util()
        self.util.start('inputs')
    """

    # Test 9
    def test_scenario_creation(self):
        try:
            self.tester.entry()
            self.tester.sign_out()
        except Exception as e:
            print('Test 8 Failed because ' + str(e))

    # Test 10


    def tearDown(self):
        self.tester.shutdown_driver()



if __name__ == '__main__':
    unittest.main()
    loader = TestLoader()
    suite = TestSuite([
        loader.loadTestsFromTestCase(Unit1),
        #loader.loadTestsFromTestCase(Unit2),
        #loader.loadTestsFromTestCase(Unit3)
    ])
    outfile = open(loc1 + "\Rep_TestResult.html", "w")

    runner1 = HTMLTestRunner.HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Web Re-Plan Tests (CSCE 6420 project)'
    )

    #runner1.run(smoke_test)
    runner = TextTestRunner(verbosity=2)


    runner.run(suite)
    #h = HTMLTestRunner(combine_reports=True, report_name="MyReport", add_timestamp=False).run(suite)
