import pandas as pd

# Create the first DataFrame based on input

data1 = pd.read_csv(input("Enter name of file 1: "), sep='\t')
df1 = pd.DataFrame(data1)
print(df1)

# Create the second DataFrame based on input

data2 = pd.read_csv(input("Enter name of file 2: "), sep='\t')
df2 = pd.DataFrame(data2)
print(df2)

# Merge the DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')

# Print the merged DataFrame

print("After merging both files:\n", merged_df)
