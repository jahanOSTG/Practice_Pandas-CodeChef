import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Score': [85, 92, np.nan, 78, 95],
        'City': ['NY', 'LA', 'Chicago', 'NY', 'LA']}
df = pd.DataFrame(data)

# find median of 'Score' and replace all missing values with the median score
# Your code here
# Calculate the average score
average_score = df['Score'].median()
df['Score'] = df['Score'].fillna(average_score)

# Use existing df and select Name, Age, and updated Score
show = df[['Name','Score','City']]
print(show)

