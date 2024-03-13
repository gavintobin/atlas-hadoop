#!/usr/bin/env python3
'''task 7'''
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    #  array to hold the top 10 salaries
    top_salaries = []

    # input
    data = read_mapper_output(sys.stdin, separator=separator)
    for employee_id, total_compensation in data:

        total_compensation = float(total_compensation)

        # add to list
        top_salaries.append((total_compensation, employee_id))
        
        top_salaries.sort(reverse=True)

