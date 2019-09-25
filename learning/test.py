#!/usr/bin/python

import csv
import requests

def get_loc(name, address):
  print(f"getting location for {name}")


with open('epic_local_locations.csv') as open_file:
    reader = csv.reader(open_file, delimiter = ',', quotechar = '"')
    for row in reader:
        print(row)
