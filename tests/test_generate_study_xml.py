import unittest
from study_subs import generate_study_xml
import xml.etree.ElementTree as ElementTree
from lxml import etree
import os


class Test_generate_study_xml(unittest.TestCase):

    def setUp(self):
        generate_study_xml("tests\studySubmissionData.tsv", False)

    def test_if_xml_generated_correctly(self):
        tree = ElementTree.parse('project_set.xml')
        xml2string = ElementTree.tostring(tree.getroot(), encoding = 'UTF8', method = 'xml')
        print(xml2string)
        expected_string = b'<?xml version=\'1.0\' encoding=\'UTF8\'?>\n<PROJECT_SET>\n  <PROJECT alias="study_alias01">\n    <NAME>Study Name 1</NAME>\n    <TITLE>Title of first study</TITLE>\n    <DESCRIPTION>This study is a test</DESCRIPTION>\n    <SUBMISSION_PROJECT>\n      <SEQUENCING_PROJECT />\n    </SUBMISSION_PROJECT>\n  </PROJECT>\n</PROJECT_SET>'
        self.assertEqual(xml2string,expected_string)
        os.remove('project_set.xml')

if __name__ == '__main__':
    unittest.main()
