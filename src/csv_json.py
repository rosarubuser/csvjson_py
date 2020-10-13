import csv
import json


def csv2js(inF_path, outF_path):
    with open(inF_path, 'r') as inF:
        dict_f = csv.DictReader(inF, skipinitialspace=True)  # read from csv into dictionary
        with open(outF_path, 'w') as outF:
            for row in dict_f:
                result = json.dumps(row, indent=4)  # read from dict to json
                outF.write(result + '\n')


def js2csv(inF_path, outF_path):
    with open(inF_path, 'r') as inF:
        data = inF.read()  # convert io.TextIOWrapper to str
        dict_f = json.loads(data)  # convert json to list
        with open(outF_path, 'w') as outF:
            fieldnames = []  # fieldnames to store keys
            for key in dict_f[0]:  # for keys in ele0
                fieldnames.append(key)
            writer = csv.DictWriter(outF, fieldnames)
            writer.writeheader()  # add the keys as first row
            for row in dict_f:  # for each dict in list
                writer.writerow(row)  # convert dict values to csv


'''
testing input
inF_path = "../test/testing.csv"
outF_path = "../test/result.json"
'''
inF_path = input("Enter the input file path:")
outF_path = input("Enter the output file path:")
choice = input("Convert csv to json[1] or json to csv[2]? (Enter 1 or 2):")

if choice == '1':  # convert csv to json
    csv2js(inF_path, outF_path)
elif choice == '2':  # convert json to csv
    js2csv(inF_path, outF_path)