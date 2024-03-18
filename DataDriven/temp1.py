import pandas as pd

def compare_csv_rows(file1_path, file2_path, row_num):
    # Read the specified row from each file
    row_file1 = pd.read_csv(file1_path, skiprows=row_num - 1, nrows=1).values.flatten()
    row_file2 = pd.read_csv(file2_path, skiprows=row_num - 1, nrows=1).values.flatten()

    # Compare the values in the two rows
    rows_equal = all(row_file1 == row_file2)

    # Output the result
    if rows_equal:
        print(f"Row {row_num} from File 1 is equal to Row {row_num} from File 2.")
    else:
        print(f"Row {row_num} from File 1 is not equal to Row {row_num} from File 2.")
        print_differences(row_file1, row_file2)

def print_differences(row1, row2):
    print("Differences:")
    for i, (value1, value2) in enumerate(zip(row1, row2), start=1):
        if value1 != value2:
            print(f"Column {i}:")
            print(f"  File 1: {value1}")
            print(f"  File 2: {value2}")

def main():
    file1_path = 'path/to/file1.csv'
    file2_path = 'path/to/file2.csv'

    path = "C:\\Users\\SC-229-USER\\Desktop\\ks\\"
    file_name1 = "pf_hp"
    file_name2 = "pf_lp"

    file_loc1 = path + str(file_name1) + str(".csv")
    file_loc2 = path + str(file_name2) + str(".csv")
    row_number = 1  # Specify the row number to compare

    compare_csv_rows(file1_path, file2_path, row_number)

if __name__ == "__main__":
    main()
