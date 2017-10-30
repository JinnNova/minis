# Not so useful Python minis by Hanna "Jinn" Enqvist

# This program will take a CSV file-name as command line parameter argv[1], and output JSON file-name as command line parameter argv[2]
# In this example CSV file contains data in format: '"Jane Doe / Department / Occupation";ageInt;salaryFloat' per row
from sys import argv
import csv
import json

if len(argv) < 3:
    print("Give CSV and JSON filenames as commandline parameters [1] and [2] \nProgram will exit.")
else:
    with open(argv[1], "r", encoding="utf-8") as infile:
        readCSV = csv.reader(infile, delimiter=";")
        data = []
        for row in readCSV:
            person = {}
            person["age"] = int(row[1])
            person["salary"] = float(row[2])
            splitrow = row[0].split("/")
            person["name"] = splitrow[0].strip()
            person["department"] = splitrow[1].strip()
            person["occupation"] = splitrow[2].strip()
            data.append(person)

    with open(argv[2], "w") as outfile:
        json.dump(data, outfile, indent=3)
