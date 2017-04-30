#!/usr/bin/env python2

from csv import DictReader
import json
import sys
import json

option = sys.argv[2]

return_json = {}

with open(sys.argv[1]) as f:
    return_json["dates"] = [row["date"] for row in DictReader(f)]
    f.seek(0)
    return_json["ratings"] = [float(row[option]) for row in DictReader(f)]
for rating in return_json["ratings"]:
    print rating,
print
for date in return_json["dates"]:
    date_parts = date.split("/")
    print date_parts[2] + "-" + date_parts[0] + "-" + date_parts[1],
print
