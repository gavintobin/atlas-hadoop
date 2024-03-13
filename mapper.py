#!/usr/bin/env python3
import sys

# read input from sys
for line in sys.stdin:
    # spli into fields?
    fields = line.strip().split(',')

    # get whats needed
    if len(fields) >= 3:
        employee_id, company, total_compensation = fields[0], fields[1], fields[2]

        # make key val pairs
        print(f"{employee_id}\t{company},{total_compensation}")

