import pandas as pd

my_mixed_list = [10, 'apple', 20, 'banana', 30]

# convert the python-list into pandas-series
my_mixed_series=pd.Series(my_mixed_list)
print(my_mixed_series)
