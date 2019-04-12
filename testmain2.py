import json
import InputSearchClass
import unittest

class TestBasic(unittest.TestCase):
    ''''@classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""
    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""
    def setUp(self):
        """This method is run once before _each_ test method is executed"""
    def teardown(self):
        """This method is run once after _each_ test method is executed""" '''

    def test_sample_json_file(self):
        """Test all sample json files in the testdata directory."""
        json_file = "InputCases"
        #json_file = "InputCases_reg"
        #json_file = "InputCases_Sce"
        json_fp = open(json_file, 'r')
        json_content = json_fp.read()
        json_fp.seek(0)
        json_data = json.load(json_fp)
        json_fp.close()
        '''
            json.load(file_pointer) where file_pointer open json file in read mode. This method creates and returns a dictionary
            from JSON file
            json.loads(file_pointer(read)) where file_pointer.read() is a string and rest is same as json.load(). But, we need
            to use pprint() to print the dictionary
        '''
        for elements in json_data:                           # Each elements is a tag under json_data
            # print "Details of ", elements                  # description of elements
            # print json_data[elements]                      # Each elements is a list of dictionaries
            for entry in range(len(json_data[elements])):    # entry stands for a dictionary from a list of dictionaries for elements
                email_id = json_data[elements][entry]['emailAddress']
                name = json_data[elements][entry]['firstName']
                uid = json_data[elements][entry]['userId']
                reg = json_data[elements][entry]['State']
                flname = json_data[elements][entry]['preferredFullName']
                county = json_data[elements][entry]['County']
                contact = json_data[elements][entry]['phoneNumber']

                # Here elements stands for Employees of an organisation and each entry stands for details of an Employee

                for item in json_data[elements][entry]:
                    if item == 'userId':
                        uid_value = InputSearchClass.check_userID(uid)
                        self.assertEqual(uid_value, True, msg="user ID is not valid")


                    if item == 'firstName':
                        fname_value = InputSearchClass.check_firstName(name)
                        self.assertEqual(fname_value, True, msg="Name is not valid")

                    if item == 'Organisation':
                        lname_value = InputSearchClass.check_lastName(county)
                        self.assertEqual(lname_value, True, msg="Organisation is not valid")

                    if item == 'FullName':
                        flname_value = InputSearchClass.check_preferredFullName(flname)
                        self.assertEqual(flname_value, True, msg="Employee Preferred full name is not valid")



                    if item == 'State':
                        reg_value = InputSearchClass.check_region(reg)
                        self.assertEqual(reg_value, True, msg="Working region is not valid")

                    if item == 'phoneNumber':
                        contact_value = InputSearchClass.check_phoneNumber(contact)
                        self.assertEqual(contact_value, True, msg="Contact number is not valid")

                    if item == 'emailAddress':
                        email_id_value = InputSearchClass.check_emailAddress(email_id)
                        self.assertEqual(email_id_value, True, msg="Email ID is not valid")

if __name__ == '__main__':
    unittest.main()
