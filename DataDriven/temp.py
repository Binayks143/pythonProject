import pandas as pd

# Install Jinja2 and openpyxl if not already installed
try:
    import jinja2
except ImportError:
    import subprocess
    subprocess.check_call(["pip", "install", "Jinja2", "openpyxl"])

def highlight_difference(val):
    color = 'yellow' if val else ''
    return f'background-color: {color}'

def compare_csv_files(file1, file2, output_file):
    # Read both CSV files into pandas DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Compare the DataFrames to get the differences
    differences = df1.compare(df2)

    # Temporarily reset the multi-index columns to regular columns
    differences.columns = differences.columns.map(lambda x: '_'.join(x) if isinstance(x, tuple) else x)

    # Highlight the differences using the highlight_difference function
    differences_styled = differences.style.applymap(highlight_difference)

    # Write the highlighted differences to a new Excel file
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        differences_styled.to_excel(writer, index=False)

    # Set the multi-index columns back (convert list to tuple)
    differences.columns = pd.MultiIndex.from_tuples([tuple(col.split('_')) for col in differences.columns])



# Replace 'file1.csv' and 'file2.csv' with your CSV file paths
path = "C:\\Users\\SC-229-USER\\Desktop\\ravi_multiModel\\"
file_name1 = "premium_hp_temp"
file_name2 = "premium_lp_temp"

file_loc1 =  path + str(file_name1)+str(".csv")
file_loc2 =  path + str(file_name2)+str(".csv")

# Replace 'differences_log.csv' with the desired log file path
log_file_path = path + str("diff_")+file_name1+str("___")+file_name2+str(".xlsx")

compare_csv_files(file_loc1, file_loc2, log_file_path)

