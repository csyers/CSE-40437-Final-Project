#!/usr/bin/env python

from csv import DictReader
import json
import sys
import json

option = sys.argv[2]

return_json = {}

with open(sys.argv[1]) as f:
    return_json["dates"] = [row["date"] for row in DictReader(f)]
    f.seek(0)
    return_json["ratings"] = [row[option] for row in DictReader(f)]

print(json.dumps(return_json))
