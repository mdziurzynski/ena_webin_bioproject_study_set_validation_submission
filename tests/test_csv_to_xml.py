import unittest
from study_subs import csv_to_xml
import csv
import xml.etree.ElementTree as ElementTree
from lxml import etree
import os


class Test_csv_to_xml(unittest.TestCase):

    def setUp(self):
        test_data_path = os.path.join('tests', 'studySubmissionData.tsv')

        with open(test_data_path, 'r') as tsv_file:
            csv_rows = csv.reader(tsv_file, delimiter='\t')
            next(csv_rows) # Skips header row
            self.row = next(csv_rows)

    def test_csv_to_xml_correct(self):
        csv2xml = csv_to_xml(self.row)
        xml2string = ElementTree.tostring(csv2xml.getroot(), encoding = 'UTF8', method = 'xml')
        expected_string = b'<?xml version=\'1.0\' encoding=\'UTF8\'?>\n<PROJECT alias="study_alias01"><NAME>Study Name 1</NAME><TITLE>Title of first study</TITLE><DESCRIPTION>This study is a test</DESCRIPTION><SUBMISSION_PROJECT><SEQUENCING_PROJECT /></SUBMISSION_PROJECT></PROJECT>'
        self.assertEqual(xml2string,expected_string)

if __name__ == '__main__':
    unittest.main()
