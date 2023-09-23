# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
  '''
  Parse a CSV file into a list of records
  '''
  with open(filename) as f:
    rows = csv.reader(f, delimiter=delimiter)

    if has_headers:
      # Read the file headers
      headers = next(rows)

    if select:
      indices = [headers.index(col) for col in select]
      headers = select if has_headers else None
    else:
      indices = []

    records = []
    for row in rows:
      if not row:
        continue

      if indices:
        row = [ row[idx] for idx in indices]
      if types:
        row = [func(val) for func, val in zip(types, row) ]
      if has_headers:
        record = dict(zip(headers, row))
        records.append(record)
      else:
        records.append(row)

  return records
