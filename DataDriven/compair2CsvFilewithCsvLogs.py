import csv

def compare_csv_files(file1, file2, output_file):
    differences = []
    extra_rows_file1 = []
    extra_rows_file2 = []

    with open(file1, 'r') as csvfile1, open(file2, 'r') as csvfile2:
        reader1 = csv.reader(csvfile1)
        reader2 = csv.reader(csvfile2)

        for row1, row2 in zip(reader1, reader2):
            if row1 != row2:
                differences.append([row1, row2])

        # Check for any extra rows in file 1
        for row in reader1:
            extra_rows_file1.append(row)

        # Check for any extra rows in file 2
        for row in reader2:
            extra_rows_file2.append(row)

    # Write differences and extra rows to output file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Differences'])
        writer.writerows(differences)
        writer.writerow([])
        writer.writerow(['Extra rows in File 1'])
        writer.writerows(extra_rows_file1)
        writer.writerow([])
        writer.writerow(['Extra rows in File 2'])
        writer.writerows(extra_rows_file2)

# Example usage
#configuring the path
path = "C:\\Users\\SC-229-USER\\Desktop\\sweta\\"
#file_name = "premium_hp"
file1 = 'req_locked_hp'
file2 = 'req_locked_lp'
file_loc1 =  path + str(file1)+str(".csv")
file_loc2 =  path + str(file2)+str(".csv")

output_file = 'comparison_output.csv'
compare_csv_files(file_loc1, file_loc2, output_file)
