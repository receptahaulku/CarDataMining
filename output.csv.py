import csv

input_file_path = 'output2.txt'
output_file_path = 'output.csv'

# Open the input and output files with explicit encoding
with open(input_file_path, 'r', encoding='utf-8') as txt_file, open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Iterate through each line in the TXT file
    for line in txt_file:
        # Split the line into fields (adjust the delimiter if needed)
        fields = line.strip().split('\t')  # Assuming tab-separated values, adjust as needed

        # Write the fields to the CSV file
        csv_writer.writerow(fields)