import os
import re
import csv
from rename import *

folder_path = '/Users/jessicawong/Downloads/PWP2022'

old_names = open_folder(folder_path)

new_names = get_new_names(old_names)
print(new_names)

aligned_names = align_names(new_names)
print(aligned_names)

rename(folder_path, aligned_names)

# Combine old and new names into a list of tuples
data = list(zip(old_names, aligned_names))

# Specify the CSV file path
csv_file_path = 'image_names.csv'

# Write data to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header (optional)
    csv_writer.writerow(['Old Files', 'Renamed Files'])

    # Write the data
    csv_writer.writerows(data)
