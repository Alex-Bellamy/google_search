import unittest
from http.client import HTTPResponse
from bs4 import BeautifulSoup
from search import
from io import StringIO


class TestSearchMethods(unittest.TestCase):

    def setUp(self):
        self.scraper = search("https://docs.python.org/2/library/unittest.html")
        self.scraper.makeDataDictionary()

    def test_dataDictionaryContents(self):
        self.assertTrue(isinstance(self.scraper.dataDictionary, dict))
        self.assertTrue(isinstance(self.scraper.dataDictionary["html"], HTTPResponse))
        self.assertTrue(isinstance(self.scraper.dataDictionary["text"], str))
        self.assertTrue(isinstance(self.scraper.dataDictionary["soup"], BeautifulSoup))
        self.assertSetEqual(set(self.scraper.dataDictionary.keys()), set(["text", "soup", "html"]))

    def test_writeSoup(self):
        filePath = "/users/bellamy/desktop/testFile.html"
        self.scraper.writeSoup(filePath)
        self.writtenData = open(filePath, "r").read()
        self.assertEqual(self.writtenData, self.scraper.dataDictionary["soup"].prettify())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAbstractScraperMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)