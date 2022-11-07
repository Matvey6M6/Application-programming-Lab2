import csv
from operator import truediv
import os


def write_as_csv(path_to_dataset, paths_to_files):

    with open("dataset_csv.csv", "w+", encoding='utf-8', newline='') as file:
     with open("dataset_csv_first.csv", "w+", encoding='utf-8', newline='') as file:
        csv_file = csv.writer(file ,delimiter=';')
        csv_file.writerow(["Absolute path","Relative path","Class"])