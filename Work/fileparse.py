# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None):
  '''
  Parse a CSV file into a list of records
  '''
  with open(filename) as f:
    rows = csv.reader(f)

    # Read the file headers
    headers = next(rows)

    if select:
      indices = [headers.index(col) for col in select]
      headers = select
    else:
      indices = []

    records = []
    for row in rows:
      if not row:
        continue

      if indices:
        row = [ row[idx] for idx in indices]
      record = dict(zip(headers, row))
      records.append(record)

  return records
