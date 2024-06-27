import unittest
import os
import argparse
from main import main as run_data_cleaner


class TestDataCleanerCodeGeneration(unittest.TestCase):
    def setUp(self):
        self.input_file = r'unittest.datacleaner'
        self.output_file = r'test_output.py'

        with open(self.input_file, 'w') as f:
            f.write("""
    load "data.csv"
    remove_rows_missing column1
    fill_missing column2 with mean
    normalize column3 to_range(0, 1)
    standardize column4
    log_transform column5
    auto_categorize column6 n_clusters=3
    split_data train=0.7, validate=0.2, test=0.1
            """)

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_code_generation(self):
        argparser = argparse.ArgumentParser()
        argparser.add_argument('-i', '--input', help='Input source', default=self.input_file )
        argparser.add_argument('-o', '--output', help='Output path', default=self.output_file )
        args = argparser.parse_args()
        run_data_cleaner(args)

        with open(self.output_file, 'r') as file:
            generated_code = file.read()

        expected_code = """import pandas as pd
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
train_data, validate_data, test_data = np.split(data.sample(frac=1, random_state=42), [int(0.7*len(data)), int((0.7+0.2)*len(data))])
"""
        self.assertEqual(generated_code.strip(), expected_code.strip())


if __name__ == '__main__':
    unittest.main()
