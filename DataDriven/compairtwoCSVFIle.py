import csv

from DataDriven.compairingTwoCSV import diff_row

#configuring the path
path = "C:\\Users\\SC-229-USER\\Desktop\\sweta\\"
file1 = 'req_locked_hp'
file2 = 'req_locked_lp'

file_loc1 =  path + str(file1)+str(".csv")
file_loc2 =  path + str(file2)+str(".csv")

def compare_csv_files(file1, file2):
    with open(file1, 'r') as csvfile1, open(file2, 'r') as csvfile2:
        reader1 = csv.reader(csvfile1)
        reader2 = csv.reader(csvfile2)

        for row1, row2 in zip(reader1, reader2):
            if row1 != row2:
                print("Difference found:")
                print("File 1:", row1)
                print("File 2:", row2)
                print()

        # Check for any extra rows in file 1
        for row in reader1:
            print("Extra row in File 1:", row)
            print()

        # Check for any extra rows in file 2
        for row in reader2:
            print("Extra row in File 2:", row)
            print()

compare_csv_files(file_loc1, file_loc2)
