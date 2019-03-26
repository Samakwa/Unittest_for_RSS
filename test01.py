import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.common.keys import Keys
import unittest
from utils import Util
from unittest import TestLoader, TextTestRunner, TestSuite
from testClass import *

"""
Login class.
include all Tests that related to the login window
"""


class Login(unittest.TestCase):
    # set the environment for tests
    def setUp(self):
        self.tester = LoginTest1()
        self.util = Util()
        self.util.start('inputs')

    # Test 1
    def test_if_enter_well(self):
        try:
            self.assertEqual('Connected Successfully', self.tester.sign_in(
                self.util.mapper[ARGS_FOR_TEST_1][LOGIN_MAIL], self.util.mapper[ARGS_FOR_TEST_1][LOGIN_PASS]))
        except Exception as e:
            print('Test 1 Failed Because ' + str(e))


if __name__ == '__main__':
    loader = TestLoader()
    suite = TestSuite((
         loader.loadTestsFromTestCase(Login)
        #loader.loadTestsFromTestCase(Unit2),
        #loader.loadTestsFromTestCase(Unit3)
    ))
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)