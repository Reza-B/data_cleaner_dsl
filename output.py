import pandas as pd
import numpy as np
data = pd.read_csv("data.csv")
columns_to_delete_outlier = [col for col in data.columns if col not in ['age', 'price']]

for col in columns_to_delete_outlier:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
            
