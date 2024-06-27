import pandas as pd
import numpy as np
data = pd.read_csv("data.csv")
data = data.dropna(subset=['column1'])
data['column2'] = data['column2'].fillna(data['column2'].mean())
data['column3'] = (data['column3'] - data['column3'].min()) / (data['column3'].max() - data['column3'].min()) * (1 - 0) + 0
data['column4'] = (data['column4'] - data['column4'].mean()) / data['column4'].std()
data['column5'] = np.log1p(data['column5'])
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
data['column6'] = kmeans.fit_predict(data['column6'].values.reshape(-1, 1))
train_data, validate_data, test_data = np.split(data.sample(frac=1, random_state=42), [int(0.1*len(data)), int((0.1+0.2)*len(data))])
