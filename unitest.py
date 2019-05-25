import unittest
from study_subs import validate_credentials


class Test1(unittest.TestCase):
    
    def setUp(self):
        pass

#submit = True
    def test_username_right_submit(self):
        self.assertEqual(validate_credentials("IgF_APB", "APB2019", submit = True),True)

    def test_username_wrong_submit(self):
        self.assertEqual(validate_credentials("IgF_APB_false", "APB2019", submit = True),False)

    def test_password_right_submit(self):
        self.assertEqual(validate_credentials("IgF_APB", "APB2019", submit = True),True)

    def test_password_wrong_submit(self):
        self.assertEqual(validate_credentials("IgF_APB", "APB2019_wrong", submit = True),False)

#submit = False
    def test_username_right_nosubmit(self):
        self.assertEqual(validate_credentials("IgF_APB", "APB2019", submit = False),True)

    def test_username_wrong_nosubmit(self):
        self.assertEqual(validate_credentials("IgF_APB_false", "APB2019", submit = False),False)

    def test_password_right_nosubmit(self):
        self.assertEqual(validate_credentials("IgF_APB", "APB2019", submit = False),True)

    def test_password_wrong_nosubmit(self):
        self.assertEqual(validate_credentials("IgF_APB", "APB2019_wrong", submit = False),False)

if __name__ == '__main__':
    unittest.main()

