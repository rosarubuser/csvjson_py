import csv
import json

with open("testing.csv", 'r') as inF:
	dict_f = csv.DictReader(inF)	#read from csv into dictionary
	with open("result.json", 'w') as outF:
		for row in dict_f:
			result = json.dumps(row, indent = 4)	#read from dict to json
			outF.write(result + '\n')