import csv

import pandas as pd
import numpy as np

from DataDriven.compairingTwoCSV import diff_row

#configuring the path
path = "C:\\Users\\SC-229-USER\\Desktop\\multimodel test\\final test case\\"
file_name1 = "issue_users_hp"
file_name2 = "issue_users_lp"

file_loc1 =  path + str(file_name1)+str(".csv")
file_loc2 =  path + str(file_name2)+str(".csv")


# Load the CSV files into DataFrames
df1 = pd.read_csv(file_loc1)
df2 = pd.read_csv(file_loc2)


# Merge the DataFrames on "user_id" with an outer join
merged_df = pd.merge(df1, df2, on='user_id', how='outer', suffixes=('_HP', '_LP'))

# Calculate the difference between columns 2 and 3
merged_df['STATUS_differance'] = merged_df['status_HP'] == merged_df['status_LP']
merged_df['lp_differance'] = merged_df['loan_product_id_HP'] - merged_df['loan_product_id_LP']
merged_df['PV_differance'] = merged_df['processing_version_HP'] < merged_df['processing_version_LP']
# merged_df['status'] = merged_df['STATUS_differance']=='FALSE' and merged_df['PV_differance']=='TRUE'


# Fill missing values with empty strings
merged_df = merged_df.fillna('')

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('merged_result.csv', sep='\t', index=False)
merged_df.to_csv(path+file_name1+file_name2+"_diff.csv", sep=',', index=False)

