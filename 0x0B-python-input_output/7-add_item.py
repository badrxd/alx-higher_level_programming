#!/usr/bin/python3
"""function for saving to json"""
import json
import os.path
from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
ls = []
if os.path.exists(filename):
    ls = load_from_json_file(filename)

for i in range(1, len(sys.argv)):
    ls.append(sys.argv[i])

save_to_json_file(ls, filename)
