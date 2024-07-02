import pandas as pd
import numpy as np
data = pd.read_csv("sample_data.csv")
data = data.dropna(subset=['age'])
data.reset_index(drop=True, inplace=True)
data = data.drop([4])
data = data.drop_duplicates()
data['salary'] = data['salary'].fillna(round(data['salary'].mean(), 2))
data['salary'] = (data['salary'] - data['salary'].min()) / (data['salary'].max() - data['salary'].min()) * (1 - 0) + 0
data['tax'] = (data['tax'] - data['tax'].mean()) / data['tax'].std()
data['experience'] = np.log1p(data['experience'])
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
data['salary'] = kmeans.fit_predict(data['salary'].values.reshape(-1, 1))
data['department'] = data['department'].replace(['IT', 'splitDataStatement', '15', '15', '70'], 'Finance')
columns_to_delete_outlier = ['salary']

for col in columns_to_delete_outlier:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
            
data = data.drop(columns=['id'])
data = pd.get_dummies(data)
print(data)
data.to_csv('cleaned_data.csv', index=False)
