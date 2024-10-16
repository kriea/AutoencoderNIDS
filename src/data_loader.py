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
    # Select relevant columns (based on KDD feature names)
    numerical_features = [0, 4, 5]  # Example numerical columns
    categorical_features = [1, 2, 3]  # Example categorical columns
    
    # Scale numerical features
    scaler = StandardScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    # One-hot encode categorical features
    encoder = OneHotEncoder(sparse=False)
    encoded_features = encoder.fit_transform(df[categorical_features])
    
    # Combine processed numerical and encoded features
    df_encoded = pd.DataFrame(encoded_features)
    df_processed = pd.concat([df.drop(categorical_features, axis=1), df_encoded], axis=1)
    
    return df_processed

# Split data into train and test sets
def split_data(df, test_size=0.2):
    X_train, X_test = train_test_split(df, test_size=test_size, random_state=42)
    return X_train, X_test
