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

PATH_TO_CSV_DIRECTORY = os.getcwd() + '/02-library/tests/test_files/'  # get path/to/test_files/


def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    # Concatenate PATH_TO_CSV_DIRECTORY and csv_file_path
    csv_file_path = PATH_TO_CSV_DIRECTORY + csv_file_path
    # row major matrix
    row_major = []
    try:
        # try to open path/to/csv
        with open(csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            temp = []  # temp list to contain a single row
            for row in csv_reader:
                # get each row
                temp = [row[0], row[1]]
                # place 1-D object as an item in 2-D array
                row_major.append(temp)
                # empty temp before moving onto new row
                temp = []
    except FileNotFoundError:
        # Could not find the CSV file
        print(f'The following path {csv_file_path} does not exist.')
    return row_major
