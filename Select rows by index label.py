
import pandas as pd

# Create a DataFrame
data = {'Color': ['Red', 'Yellow', 'Green'],
        'Sweetness': ['High', 'Medium', 'Low']}
fruits_df = pd.DataFrame(data, index=['Apple', 'Banana', 'Grape'])

# Access the row for 'Banana'
# Your code here to select the row for 'Banana'
banana_row=fruits_df.loc["Banana"]
print(banana_row)
