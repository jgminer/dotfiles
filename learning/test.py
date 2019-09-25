#!/usr/bin/python

import os
import csv
import requests

all_resorts = []
mapquest_key = os.environ.get('MAPQUEST_KEY')

def get_loc(name, address):
  print(f'getting location for {name}')
  params = {'key': mapquest_key, 'location': address}
  res = requests.get('http://open.mapquestapi.com/geocoding/v1/address', params=params)
  print(res.json()['results'][0]['locations'][0]['latLng'])

def open_csv():
    with open('epic-local-locations.csv') as open_file:
        reader = csv.DictReader(open_file, delimiter = ',', quotechar = '"')
        for row in reader:
            all_resorts.append(row)

def get_all_locations():
    open_csv()
    for resort in all_resorts:
        print(get_loc(resort['Name'], resort['Address']))

if __name__ == '__main__':
    get_all_locations()
