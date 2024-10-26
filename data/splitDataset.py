import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

"""
This code preprocesses the KDD Cup 1999 dataset for machine learning tasks.

The main steps are:
1. Load the dataset from a compressed CSV file.
2. Separate the features and labels.
3. Extract the 'normal.' labeled instances as the normal data.
4. Preprocess the data by applying one-hot encoding to categorical features and min-max scaling to numerical features.

The preprocessor object created at the end can be used in a machine learning pipeline to transform the data before training a model.

"""


# Define column names based on kddcup.names (simplified for clarity)
column_names = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 
    'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 
    'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 
    'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 
    'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 
    'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 
    'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label'
]
#0,tcp,http,SF,181,5450,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,8,8,0.00,0.00,0.00,0.00,1.00,0.00,0.00,9,9,1.00,0.00,0.11,0.00,0.00,0.00,0.00,0.00,normal.
# Above is an example of a line from the dataset

# Load the data
data = pd.read_csv("data/raw/kddcup.data_10_percent.gz", names=column_names)


#Separate features and labels
features = data.drop(columns=['label'])
labels = data['label']

#separate normal data
normal_data = features[labels == 'normal.']

#preprocessing: onehot encoding categorical, normalizing numerical
categorical_features = ['protocol_type', 'service', 'flag'] #these features are not numerical, rather text
numerical_features = normal_data.drop(columns=categorical_features).columns.to_list() #numerical only features

preprocessor = ColumnTransformer(
    transformers=[
        ('num', MinMaxScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ]
)


# Simplify to apply just the preprocessor first for testing
try:
    normal_data_preprocessed = preprocessor.fit_transform(normal_data)
    print("Preprocessing successful, output shape:", normal_data_preprocessed.shape)

    # If successful, you can proceed to use the full pipeline
    pipeline = Pipeline(steps=[('preprocessor', preprocessor)])
    normal_data_preprocessed_pipeline = pipeline.fit_transform(normal_data)
    print("Pipeline processing successful, output shape:", normal_data_preprocessed_pipeline.shape)

    # Save the processed data
    pd.DataFrame(normal_data_preprocessed_pipeline).to_csv("data/processed/train_normal_10_percent.csv", index=False)
except Exception as e:
    print("An error occurred during preprocessing:", str(e))