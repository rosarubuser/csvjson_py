import csv
import json
import argparse
import io
from io import StringIO
import os


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
    writer = csv.DictWriter(csv_str, fieldnames)  # here csv_str requires file form
    writer.writeheader()  # add the keys as first row
    for row in list_f:  # for each dict in list
        writer.writerow(row)  # convert dict values to csv
    return csv_str.getvalue()


''' for testing input
input = "testing"
output = "result"
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the input file name")
    parser.add_argument("output", help="the output file name")
    parser.add_argument("choice", choices=["csv2js", "js2csv"], help="converting method:"
                                                                     "- from csv to json or"
                                                                     "- from json to csv")
    args = parser.parse_args()

    # complete the full file path
    if args.choice == "csv2js":  # convert csv to json
        input_path = "../test/" + args.input + ".csv"
        output_path = "../test/" + args.output + ".json"
    elif args.choice == "js2csv":  # convert json to csv
        input_path = "../test/" + args.input + ".json"
        output_path = "../test/" + args.output + ".csv"

    # check whether the input file exists
    if not os.path.isfile(input_path):
        print("The input file path is invalid.")
        exit()

    # exam the file opening
    try:
        inF = open(input_path, 'r')
        in_str = inF.read()  # read the input file into string
    except:
        print("Something went wrong in reading the input file")
    else:
        if args.choice == "csv2js":  # convert csv to json
            out_str = csv2js(in_str)
        elif args.choice == "js2csv":  # convert json to csv
            out_str = js2csv(in_str)

        try:
            outF = open(output_path, 'w')
            outF.write(out_str)
        except:
            print("Something went wrong in writing the output file")
        finally:
            outF.close()
    finally:
        inF.close()
