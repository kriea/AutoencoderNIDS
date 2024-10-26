import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from io import StringIO
import gzip

# Function to load dataset
def load_data(file_path):
    with gzip.open(file_path, 'rt') as f:
        df = pd.read_csv(f, header=None)
    return df

# Preprocess data
def preprocess_data(df):
    # Step 1: Filter 'normal.' labeled data
    normal_data = df[df[len(df.columns) - 1] == 'normal.'].copy()  # Assuming label is in the last column
    
    # Categorical columns
    categorical_features = [1, 2, 3]  # Protocol type, Service, Flag (0-based indexing)
    
    # Numerical columns (all other columns except the label)
    numerical_features = list(set(df.columns) - set(categorical_features) - {len(df.columns) - 1})
    
    # Step 2: Standardize numerical features
    scaler = StandardScaler()
    normal_data[numerical_features] = scaler.fit_transform(normal_data[numerical_features])
    
    # Step 3: One-hot encode categorical features
    encoder = OneHotEncoder(sparse=False)
    encoded_categorical = encoder.fit_transform(normal_data[categorical_features])
    
    # Step 4: Drop the label column for training
    normal_data = normal_data.drop(columns=[len(normal_data.columns) - 1])
    
    # Step 5: Combine processed numerical and encoded categorical data
    df_encoded_categorical = pd.DataFrame(encoded_categorical)
    df_processed = pd.concat([normal_data.reset_index(drop=True), df_encoded_categorical], axis=1)
    
    return df_processed

# Split data into train and test sets
def split_data(df, test_size=0.2):
    X_train, X_test = train_test_split(df, test_size=test_size, random_state=42)
    return X_train, X_test
