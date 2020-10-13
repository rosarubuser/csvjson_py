import json
import csv

with open("testing.json", 'r') as inF:
    data = inF.read()  # convert io.TextIOWrapper to str
    dict_f = json.loads(data)  # convert json to list
    with open("result.csv", 'w') as outF:
        fieldnames = []  # fieldnames to store keys
        for key in dict_f[0]:  # for keys in ele0
            fieldnames.append(key)
        writer = csv.DictWriter(outF, fieldnames)
        writer.writeheader()  # add the keys as first row
        for row in dict_f:  # for each dict in list
            writer.writerow(row)  # convert dict values to csv
