import unittest
from ..src import csv2js


class TestCsvJson(unittest.TestCase):

    def test_csv2js(self):
        in_str = "Name, Age, Sex" \
                 "John, 22, M" \
                 "Amy, 50, F"
        result = csv2js(in_str)
        expected = "{" \
                   " \"Name\": \"John\"" \
                   " \"Age\": \"22\"" \
                   " \"Sex\": \"M\"" \
                   "}" \
                   "{" \
                   " \"Name\": \"Amy\"" \
                   " \"Age\": \"50\"" \
                   " \"Sex\": \"F\"" \
                   "}"
        self.assertEqual(result == expected, "Should be" + expected)

    def test_js2csv(self):
        pass


if __name__ == "__main__":
    unittest.main()
