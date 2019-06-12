import unittest
import re
from schemas import ENA_project, SRA_sample, SRA_experiment, SRA_receipt, SRA_run, SRA_study, SRA_submission


class Test_xml_parsing(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_parse_ena_project(self):
        """Caution: The study XML format is defined by the ENA.project.xsd XML schema. 
        Studies can also be submitted using the SRA.study.xsd XML schema. """

        xml = self._readXml("ena_project")

        project_set = ENA_project.CreateFromDocument(xml)

        self.assertEqual("cheddar_cheese", project_set.PROJECT[0].alias)
        self.assertIn("Characterisation of Microbial Diversity",
                      project_set.PROJECT[0].TITLE)

    def test_parse_sra_experiment(self):
        xml = xml = self._readXml("sra_experiment")

        experiment_set: SRA_experiment.ExperimentSetType = SRA_experiment.CreateFromDocument(
            xml)

        self.assertEqual(experiment_set.EXPERIMENT[0].TITLE,
                         "The 1KITE project: evolution of insects")
        self.assertEqual(
            "SRS462875", experiment_set.EXPERIMENT[0].DESIGN.SAMPLE_DESCRIPTOR.accession)
        self.assertEqual(
            "RNA-Seq", experiment_set.EXPERIMENT[0].DESIGN.LIBRARY_DESCRIPTOR.LIBRARY_STRATEGY)
        self.assertEqual(
            "2010-08", experiment_set.EXPERIMENT[0].EXPERIMENT_ATTRIBUTES.EXPERIMENT_ATTRIBUTE[0].VALUE)

    def test_parse_sra_sample(self):
        xml = xml = self._readXml("sra_sample")

        sample_set: SRA_sample.SampleSetType = SRA_sample.CreateFromDocument(
            xml)

        self.assertEqual("human gastric microbiota, mucosal",
                         sample_set.SAMPLE[0].TITLE)
        self.assertEqual(1284369, sample_set.SAMPLE[0].SAMPLE_NAME.TAXON_ID)
        self.assertEqual(
            "investigation type", sample_set.SAMPLE[0].SAMPLE_ATTRIBUTES.SAMPLE_ATTRIBUTE[0].TAG)

    def _readXml(self, name):
        xml = open(f'tests/test_data/{name}.xml').read()
        return xml


if __name__ == '__main__':
    unittest.main()
