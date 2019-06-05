import unittest
from study_subs import validate_credentials, generate_submission_xml
import os

from tests.testing_credentials import TESTING_LOGIN, TESTING_PASSWORD

class Test1(unittest.TestCase):
    
    def setUp(self):
        generate_submission_xml("VALIDATE")

    def test_right_username_right_password_nosubmit(self):
        self.assertEqual(validate_credentials(TESTING_LOGIN, TESTING_PASSWORD, submit = False),True)

    def test_wrong_username_wrong_password_nosubmit(self):
        self.assertEqual(validate_credentials("wrong_login", "wrong_password", submit = False),False)

    def test_wrong_username_right_password_nosubmit(self):
        self.assertEqual(validate_credentials("wrong_login", TESTING_PASSWORD, submit = False),False)

    def test_right_username_wrong_password_nosubmit(self):
        self.assertEqual(validate_credentials(TESTING_LOGIN, "wrong_password", submit = False),False)

    def tearDown(self):
        os.remove('VALIDATE.xml')
        

if __name__ == '__main__':
    unittest.main()

