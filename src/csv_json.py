import csv
import json
import argparse
import io
from io import StringIO


def csv2js(csv_str):
    dict_f = csv.DictReader(StringIO(csv_str), skipinitialspace=True)  # read from file into dictionary
    js_str = ""
    for row in dict_f:
        js_str = js_str + json.dumps(row, indent=4) + '\n'  # convert dict to string
    return js_str


def js2csv(js_str):
    list_f = json.loads(js_str)  # convert str to list (which is composed of dicts)

    fieldnames = []  # fieldnames to store keys
    for key in list_f[0]:  # find the keys
        fieldnames.append(key)
    csv_str = io.StringIO()
    writer = csv.DictWriter(csv_str, fieldnames)    # here csv_str requires file form
    writer.writeheader()  # add the keys as first row
    for row in list_f:  # for each dict in list
        writer.writerow(row)  # convert dict values to csv
    return csv_str.getvalue()


''' for testing input
inF_path = "../test/testing.json"
outF_path = "../test/result.csv"
'''

parser = argparse.ArgumentParser()
parser.add_argument("input", help="the input file path")
parser.add_argument("output", help="the output file path")
parser.add_argument("choice", type=int, choices=[1, 2], help="converting method (choose from 1,2):"
                                                             "1 - from csv to json; "
                                                             "2 - from json to csv")
args = parser.parse_args()

with open(args.input, 'r') as inF:
    in_str = inF.read()  # read the input file into string

if args.choice == 1:  # convert csv to json
    out_str = csv2js(in_str)
elif args.choice == 2:  # convert json to csv
    out_str = js2csv(in_str)

with open(args.output, 'w') as outF:
    outF.write(out_str)
