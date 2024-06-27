class DataCleanerCodeGenerator:
    def __init__(self):
        self.non_operands = ['load', 'removeRowsMissing', 'fillMissing',
                             'normalize', 'standardize', 'logTransform',
                             'autoCategorize', 'splitData', 'program'] #add grammar rule
        self.operand_stack = []
        self.code_stack = []

    def is_operand(self, item):
        if item in self.non_operands:
            return False
        else:
            return True

    def generate_code(self, traversal):
        for node in traversal:
            label = node['label']
            if not self.is_operand(label):
                self.generate_code_based_on_non_operand(label)
            else:
                self.operand_stack.append(label)

        result = ''
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
        # add rule function

    def generate_load_code(self):
        filepath = self.operand_stack.pop()
        self.code_stack.append(f"import pandas as pd")
        self.code_stack.append(f"import numpy as np")
        self.code_stack.append(f"data = pd.read_csv({filepath})")

    def generate_remove_rows_missing_code(self):
        column = self.operand_stack.pop()
        self.code_stack.append(f"data = data.dropna(subset=['{column}'])")

    def generate_fill_missing_code(self):
        method = self.operand_stack.pop()
        column = self.operand_stack.pop()
        if method == "mean":
            self.code_stack.append(f"data['{column}'] = data['{column}'].fillna(data['{column}'].mean())")
        elif method == "median":
            self.code_stack.append(f"data['{column}'] = data['{column}'].fillna(data['{column}'].median())")
        elif method == "mode":
            self.code_stack.append(f"data['{column}'] = data['{column}'].fillna(data['{column}'].mode()[0])")

    def generate_normalize_code(self):
        max_val = self.operand_stack.pop()
        min_val = self.operand_stack.pop()
        column = self.operand_stack.pop()
        self.code_stack.append(f"data['{column}'] = (data['{column}'] - data['{column}'].min()) / (data['{column}'].max() - data['{column}'].min()) * ({max_val} - {min_val}) + {min_val}")

    def generate_standardize_code(self):
        column = self.operand_stack.pop()
        self.code_stack.append(f"data['{column}'] = (data['{column}'] - data['{column}'].mean()) / data['{column}'].std()")


    def generate_log_transform_code(self):
        column = self.operand_stack.pop()
        self.code_stack.append(f"data['{column}'] = np.log1p(data['{column}'])")


    def generate_auto_categorize_code(self):
        clusters = self.operand_stack.pop()
        column = self.operand_stack.pop()
        self.code_stack.append(f"from sklearn.cluster import KMeans")
        self.code_stack.append(f"kmeans = KMeans(n_clusters={clusters})")
        self.code_stack.append(f"data['{column}'] = kmeans.fit_predict(data['{column}'].values.reshape(-1, 1))")

    def generate_split_data_code(self):
        train_ratio = self.operand_stack.pop()
        validate_ratio = self.operand_stack.pop()
        test_ratio = self.operand_stack.pop()

        self.code_stack.append(f"train_data, validate_data, test_data = np.split(data.sample(frac=1, random_state=42), [int({train_ratio}*len(data)), int(({train_ratio}+{validate_ratio})*len(data))])")
