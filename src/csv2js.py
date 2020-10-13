import csv
import json

with open("../test/testing.csv", 'r') as inF:
    dict_f = csv.DictReader(inF, skipinitialspace=True)  # read from csv into dictionary
    with open("../test/result.json", 'w') as outF:
        for row in dict_f:
            result = json.dumps(row, indent=4)  # read from dict to json
            outF.write(result + '\n')
