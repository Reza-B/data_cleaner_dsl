class DataCleanerCodeGenerator:
    def __init__(self):
        self.non_operands = ['load', 'removeRowsMissing', 'fillMissing',
                             'normalize', 'standardize', 'logTransform',
                             'autoCategorize', 'splitData', 'remove_duplicates',
                             'dropRow', 'dropColumn', 'integrate', 'encode',
                             'exclude_columns', 'delete_outliers', 'program']
        self.operand_stack = []
        self.code_stack = []

    def csv_save(self, name):
        self.code_stack.append(f"data.to_csv('{name}.csv', index=False)")
        
    def is_operand(self, item):
        if item in self.non_operands:
            return False
        else:
            return True

    def generate_code(self, traversal):
        def print_csv():
            self.code_stack.append("\n# print & save")
            self.code_stack.append("print(data)")

        for node in traversal:
            label = node['label']
            if not self.is_operand(label):
                self.generate_code_based_on_non_operand(label)
            else:
                self.operand_stack.append(label)

        result = ''
        print_csv()
        self.csv_save('cleaned_data')
        for code_string in self.code_stack:
            if code_string is not None:
                result += code_string + "\n"
        print(result)
        return result

    def generate_code_based_on_non_operand(self, label):
        if label == 'load':
            self.generate_load_code()
        elif label == 'removeRowsMissing':
            self.generate_remove_rows_missing_code()
        elif label == 'fillMissing':
            self.generate_fill_missing_code()
        elif label == 'normalize':
            self.generate_normalize_code()
        elif label == 'standardize':
            self.generate_standardize_code()
        elif label == 'logTransform':
            self.generate_log_transform_code()
        elif label == 'autoCategorize':
            self.generate_auto_categorize_code()
        elif label == 'splitData':
            self.generate_split_data_code()
        elif label == 'remove_duplicates':
            self.generate_remove_duplicate_code()
        elif label == 'dropRow':
            self.generate_drop_row_code()
        elif label == 'dropColumn':
            self.generate_drop_column_code()
        elif label == 'integrate':
            self.generate_integrate_inconsistent_data_code()
        elif label == 'encode':
            self.generate_encoding_code()
        elif label == 'exclude_columns':
            self.generate_exclude_columns_code()
        elif label == 'delete_outliers':
            self.generate_delete_outliers_code()

    def generate_load_code(self):
        filepath = self.operand_stack.pop()
        self.code_stack.append(f"import pandas as pd")
        self.code_stack.append(f"import numpy as np")
        self.code_stack.append(f"data = pd.read_csv({filepath})")

    def generate_remove_rows_missing_code(self):
        column = self.operand_stack.pop()
        self.code_stack.append(f"\n# remove missing rows")
        self.code_stack.append(f"""data = data.dropna(subset=['{column}'])
data.reset_index(drop=True, inplace=True)""")

    def generate_fill_missing_code(self):
        method = self.operand_stack.pop()
        column = self.operand_stack.pop()
        if method == "mean":
            self.code_stack.append(f"\n# fill missing with mean")
            self.code_stack.append(f"data['{column}'] = data['{column}'].fillna(round(data['{column}'].mean(), 2))")
        elif method == "median":
            self.code_stack.append(f"\n# fill missing with median")
            self.code_stack.append(f"data['{column}'] = data['{column}'].fillna(round(data['{column}'].median(), 2))")
        elif method == "mode":
            self.code_stack.append(f"\n# fill missing with mode")
            self.code_stack.append(f"data['{column}'] = data['{column}'].fillna(round(data['{column}'].mode()[0], 2)")

    def generate_normalize_code(self):
        max_val = self.operand_stack.pop()
        min_val = self.operand_stack.pop()
        column = self.operand_stack.pop()
        self.code_stack.append(f"\n# normalize column")
        self.code_stack.append(f"data['{column}'] = (data['{column}'] - data['{column}'].min()) / (data['{column}'].max() - data['{column}'].min()) * ({max_val} - {min_val}) + {min_val}")

    def generate_standardize_code(self):
        column = self.operand_stack.pop()
        self.code_stack.append(f"\n# standardize column")
        self.code_stack.append(f"data['{column}'] = (data['{column}'] - data['{column}'].mean()) / data['{column}'].std()")


    def generate_log_transform_code(self):
        column = self.operand_stack.pop()
        self.code_stack.append(f"\n# logarithm transform column")
        self.code_stack.append(f"data['{column}'] = np.log1p(data['{column}'])")


    def generate_auto_categorize_code(self):
        clusters = self.operand_stack.pop()
        column = self.operand_stack.pop()

        self.code_stack.append(f"\n# auto categorize column")
        self.code_stack.append(f"from sklearn.cluster import KMeans")
        self.code_stack.append("try:")
        self.code_stack.append(f"    kmeans = KMeans(n_clusters={clusters})")
        self.code_stack.append(f"    data['{column}'] = kmeans.fit_predict(data['{column}'].values.reshape(-1, 1))")
        self.code_stack.append("except:")
        self.code_stack.append(f"    print('Invalid Data!')")

    def generate_split_data_code(self):
        test_ratio = int(self.operand_stack.pop()) / 100
        train_ratio = int(self.operand_stack.pop()) / 100

        self.code_stack.append(f"\n# split data")
        self.code_stack.append(f"""train_data, test_data = np.split(data.sample(frac=1, random_state=42), [int(r * len(data)) for r in np.cumsum([{train_ratio}, {test_ratio}][:-1])])
train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)""")

    def generate_remove_duplicate_code(self):
        self.code_stack.append(f"\n# remove duplicate")
        self.code_stack.append("data = data.drop_duplicates()")

    def generate_drop_row_code(self):
        drop_list = []
        while len(self.operand_stack):
            drop_list.append(int(self.operand_stack.pop()))

        self.code_stack.append(f"\n# drop row")
        self.code_stack.append(f"data = data.drop({[number-1 for number in drop_list]})")

    def generate_drop_column_code(self):
        drop_list = []
        while len(self.operand_stack):
            drop_list.append(self.operand_stack.pop())

        self.code_stack.append(f"\n# drop column")
        self.code_stack.append(f"data = data.drop(columns={drop_list})")

    def generate_integrate_inconsistent_data_code(self):
        column_name = self.operand_stack.pop()
        consistent_value = self.operand_stack.pop()
        inconsistent_values = []
        while len(self.operand_stack):
            inconsistent_values.append(self.operand_stack.pop())

        self.code_stack.append(f"\n# integrate inconsistent")
        self.code_stack.append(f"data['{column_name}'] = data['{column_name}'].replace({inconsistent_values}, '{consistent_value}')")

    def generate_encoding_code(self):
        method = self.operand_stack.pop()
        other_params = []
        while len(self.operand_stack):
            other_params.append(self.operand_stack.pop())

        all_columns = False
        excluded_columns = []
        columns = []
        if not len(other_params):
            all_columns = True
        self.code_stack.append(f"\n# encode")
        if not all_columns:
            param = other_params[0]
            if param.startswith("exclude_columns"):
                excluded_columns = param.lstrip("exclude_columns([").rstrip("])")
                excluded_columns = list(map(lambda x: x.strip().strip("'"), excluded_columns.split(",")))

            else:
                columns = other_params.copy()

        if method == "one_hot":
            if all_columns:
                self.code_stack.append(f"data = pd.get_dummies(data)")
            elif len(excluded_columns):
                self.code_stack.append(f"columns_to_encode = [col for col in data.columns if col not in {excluded_columns}]")
                self.code_stack.append(f"data = pd.get_dummies(columns=columns_to_encode)")

            elif len(columns):
                self.code_stack.append(f"data = pd.get_dummies(columns={columns})")

    def generate_delete_outliers_code(self):
        self.code_stack.append(f"\n# delete outliers")
        method = self.operand_stack.pop()
        other_params = []
        while len(self.operand_stack):
            other_params.append(self.operand_stack.pop())

        all_columns = False
        excluded_columns = []
        columns = []
        if not len(other_params):
            all_columns = True

        if not all_columns:
            param = other_params[0]
            if param.startswith("exclude_columns"):
                excluded_columns = param.lstrip("exclude_columns([").rstrip("])")
                excluded_columns = list(map(lambda x: x.strip().strip("'"), excluded_columns.split(",")))

            else:
                columns = other_params.copy()

        if method == "IQR":
            if all_columns:
                self.code_stack.append("columns_to_delete_outlier = data.columns")
            elif len(excluded_columns):
                self.code_stack.append(f"columns_to_delete_outlier = [col for col in data.columns if col not in {excluded_columns}]")
            elif len(columns):
                self.code_stack.append(f"columns_to_delete_outlier = {columns}")

            self.code_stack.append("""
for col in columns_to_delete_outlier:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
            """)

    def generate_exclude_columns_code(self):
        excluded_columns = []
        while len(self.operand_stack):
            excluded_columns.append(self.operand_stack.pop())

        self.code_stack.append(f"\n# excluded columns")
        self.operand_stack.append(f"exclude_columns({excluded_columns})")
