import pandas as pd
import numpy as np
data = pd.read_csv("sample_data.csv")

# remove missing rows
data = data.dropna(subset=['salary'])
data.reset_index(drop=True, inplace=True)

# drop row
data = data.drop([4])

# remove duplicate
data = data.drop_duplicates()

# fill missing with mean
data['salary'] = data['salary'].fillna(round(data['salary'].mean(), 2))

# normalize column
data['salary'] = (data['salary'] - data['salary'].min()) / (data['salary'].max() - data['salary'].min()) * (1 - 0) + 0

# standardize column
data['tax'] = (data['tax'] - data['tax'].mean()) / data['tax'].std()

# logarithm transform column
data['experience'] = np.log1p(data['experience'])

# auto categorize column
from sklearn.cluster import KMeans
try:
    kmeans = KMeans(n_clusters=3)
    data['salary'] = kmeans.fit_predict(data['salary'].values.reshape(-1, 1))
except:
    print('Invalid Data!')

# split data
train_data, test_data = np.split(data.sample(frac=1, random_state=42), [int(r * len(data)) for r in np.cumsum([0.7, 0.3][:-1])])
train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)

# integrate inconsistent
data['department'] = data['department'].replace(['IT', 'removeDuplicates'], 'Finance')

# delete outliers
columns_to_delete_outlier = ['salary']

for col in columns_to_delete_outlier:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
            

# drop column
data = data.drop(columns=['id'])

# encode
data = pd.get_dummies(data)

# print & save
print(data)
data.to_csv('cleaned_data.csv', index=False)
