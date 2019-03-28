"""
Const Names
"""
# Login Details
EMAIL = 0
PASSWORD = 1

# Registration Details
EMAIL_ADD = 2
NAME= 3
ORGANISATION= 4
PASSWORD_1 = 5
PASSWORD_2 = 6


# Login window properties
LOGIN_MAIL = 0
LOGIN_PASS = 1

# index of args in the (test No.) -> args mapper
ARGS_FOR_TEST_1 = 0
ARGS_FOR_TEST_2 = 1
ARGS_FOR_TEST_3 = 2
ARGS_FOR_TEST_4 = 3
ARGS_FOR_TEST_5 = 4
ARGS_FOR_TEST_6 = 5
ARGS_FOR_TEST_7 = 6
ARGS_FOR_TEST_8 = 7

# etc.
NUMBER_OF_PAGES = 9
TIME_WAIT_FOR_PAGE_LOAD = 10


"""
Util class.
have a mapper that maps between test number (1,2,3..) and a list of args
for this test.
"""


class Util(object):
    def __init__(self):
        self.mapper = {}

    def start(self, file_name):
        i = 1
        with open(file_name, 'r') as input_file:
            content = input_file.readlines()
            for line in content:
                line.strip('\n')
                arr = line.split(';')
                size = len(arr)
                arr[size - 1] = arr[size-1].replace("\n", "")
                self.mapper[i] = arr
                i += 1
