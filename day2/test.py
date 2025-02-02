import csv

# Path to your CSV file
file_path = 'your_file.csv'

# Read the existing CSV data
with open(file_path, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    rows = list(reader)

# Modify the second row (index 1)
# Make sure there are at least two rows in the CSV before modifying
if len(rows) > 1:
    # Example: Modify second row by changing the values in that row (for demonstration)
    rows[1] = ['new_value1', 'new_value2', 'new_value3']  # Adjust the values as needed

# Write the modified data back to the CSV
with open(file_path, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print("Second row has been updated successfully!")
