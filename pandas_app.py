#Import libraries
import pandas as pd

#set up data set file path
excel_file_path = "datasrc/vgsales.csv"

#read csv into df
df = pd.read_csv(excel_file_path)
print(df.columns)

#get info on dataset
#df_info = df.info()
#print(df_info)

#get basic descriptive stats on dataset
#note the use of [index] to look at specifc column's summary 
#print(df.describe()["i_d"])
print(df.describe())

#group on one column by another 
#group one measure by one dimension
#grouped_df = df.groupby(["Platform"])
#print(grouped_df)

#filter information based on a certain criteria
#returns rows that meet the specified columns parameter 
# (e.g. profile_id = 4)
#print(df[df["profile_id"] == 4])

#create new spreadsheet with just this filtered table
#1. create vairable of filtered dataframe
#profile_id_4_df = df[df["profile_id"] == 4]
#2. send df to excel
#profile_id_4_df.to_excel('output.xlsx')