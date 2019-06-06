import unittest
import re
from schemas import ENA_project
from pyxb.exceptions_ import IncompleteElementContentError
import pyxb


class Test_xml_generating(unittest.TestCase):

    def test_generate_ena_project(self):
        project_set = ENA_project.ProjectSetType()
        project = ENA_project.ProjectType()

        project.alias = "alias"
        project.TITLE = "title"
        project.DESCRIPTION = "description"

        # use `pyxb.BIND()` to create complex type instances.
        # Alternatively class constructors can be used, but in most
        # cases those are anonymous.
        # Eg. `project.SUBMISSION_PROJECT = ENA_project.CTD_ANON_()`
        project.SUBMISSION_PROJECT = pyxb.BIND()
        project.SUBMISSION_PROJECT.SEQUENCING_PROJECT = pyxb.BIND()

        project_set.PROJECT.append(project)

        generatedXml = project_set.toxml(
            "utf-8", element_name='PROJECT_SET').decode('utf-8')

        self.assertIn("<PROJECT alias=\"alias\">", generatedXml)
        self.assertIn(
            "<TITLE>title</TITLE>", generatedXml)
        self.assertIn(
            "<DESCRIPTION>description</DESCRIPTION>", generatedXml)
        self.assertIn(
            "<SUBMISSION_PROJECT><SEQUENCING_PROJECT/></SUBMISSION_PROJECT>", generatedXml)

    def test_generate_ena_project_raises_incomplete_element_content_error(self):
        project_set = ENA_project.ProjectSetType()
        project = ENA_project.ProjectType()

        project.alias = "alias"
        project.TITLE = "title"

        project_set.PROJECT.append(project)

        with self.assertRaises(IncompleteElementContentError) as contextManager:
            project_set.toxml(
                "utf-8", element_name='PROJECT_SET').decode('utf-8')

        ex = contextManager.exception
        details = ex.details()

        self.assertIn("DESCRIPTION", details)
        self.assertIn("SUBMISSION_PROJECT", details)


if __name__ == '__main__':
    unittest.main()
