"""
    Usage:
    ------
    utility function to read a CSV file.

    Command:
    --------
    >>. read_csv('dataset_1.csv')

    *Note:
        assuming that CSV files are stores under the following directory:
        'path/to/repo/CS506-Fall2020/02-library/tests/test_files/'
"""

import csv
import os


def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    # row major matrix
    row_major = []
    try:
        # try to open path/to/csv
        with open(csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            temp = []  # temp list to contain a single row
            for row in csv_reader:
                # get each row
                temp = [dynamic_caster(r) for r in row]
                # place 1-D object as an item in 2-D array
                row_major.append(temp)
                # empty temp before moving onto new row
                temp = []
    except FileNotFoundError:
        # Could not find the CSV file
        print(f'The following path {csv_file_path} does not exist.')
    return row_major


def dynamic_caster(x):
    """
        Given a certain paramter x check to see if we can cast it successfully
        either to an integer or string
    """
    try:
        return int(x)
    except ValueError:
        return str(x)
