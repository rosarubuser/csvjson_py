import unittest
import sys
import os

sys.path.append(os.path.dirname(__file__) + os.sep + '..')  # TODO Not quite understand
from src.csv_json import csv2js
from src.csv_json import js2csv


class TestCsvJson(unittest.TestCase):

    def test_csv2js(self):
        in_str = "Name, Age, Sex\n" \
                 "John, 22, M\n" \
                 "Amy, 50, F"
        result = csv2js(in_str)
        expected = "[\n" \
                   "  {\n" \
                   "    \"Name\": \"John\",\n" \
                   "    \"Age\": \"22\",\n" \
                   "    \"Sex\": \"M\"\n" \
                   "  },\n" \
                   "  {\n" \
                   "    \"Name\": \"Amy\",\n" \
                   "    \"Age\": \"50\",\n" \
                   "    \"Sex\": \"F\"\n" \
                   "  }\n" \
                   "]"
        self.assertEqual(result, expected)

    def test_js2csv(self):
        in_str = "[\n" \
                 "  {\n" \
                 "    \"Name\": \"John\",\n" \
                 "    \"Age\": \"22\",\n" \
                 "    \"Sex\": \"M\"\n" \
                 "  },\n" \
                 "  {\n" \
                 "    \"Name\": \"Amy\",\n" \
                 "    \"Age\": \"50\",\n" \
                 "    \"Sex\": \"F\"\n" \
                 "  }\n" \
                 "]"
        result = js2csv(in_str)
        expected = "Name,Age,Sex\r\n" \
                   "John,22,M\r\n" \
                   "Amy,50,F\r\n"
        # TODO why there is \r; is it necessary?\
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

# TODO fix the logic error: python -m unittest
