#!/usr/bin/env python2

from csv import DictReader
import json
import sys
import json

return_json = {}

with open(sys.argv[1]) as f:
    return_json["dates"] = [row["date"] for row in DictReader(f)]
    f.seek(0)
    return_json["ratings"] = [float(row["rating"]) for row in DictReader(f)]
    f.seek(0)
    return_json["sentiment"] = [float(row["sentiment"]) for row in DictReader(f)]

for rating in return_json["ratings"]:
    print rating,
print
for date in return_json["dates"]:
    print date,
print
for sentiment in return_json["sentiment"]:
    print sentiment,

print
