
import pandas as pd

# Create two Pandas Series
names_series = pd.Series(['Alice', 'Bob', 'Charlie', 'David'])
ages_series = pd.Series([25, 30, 22, 35])

# Create a dictionary where keys are column names and values are the Series
data_dict = {'Name': names_series, 'Age': ages_series}

# Create a DataFrame from the dictionary of Series and print it
# Your code here
dic=pd.DataFrame(data_dict)
print(dic)
