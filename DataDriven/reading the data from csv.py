import pandas as pd
#configuring the path

path = "C:\\Users\\SC-229-USER\\Desktop\\users_test\\"
file_name = 251771
file_loc1 =  path + str(file_name)+str(".csv")

df= pd.read_csv(file_loc1)

# print(df.columns)
# print(df[["user_id","loan_product_id","updated_by_strategy"]])
print (list(df["user_id"]))




