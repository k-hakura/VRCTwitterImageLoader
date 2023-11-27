import csv
import random


def count_csv_rows(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
    return row_count


def random_line_numbers(total_lines, num_samples):
    return random.sample(range(total_lines), num_samples)
