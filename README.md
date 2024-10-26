# Deep Autoencoder-based Intrusion Detection System

This repository contains an implementation of an autoencoder-based approach for intrusion detection using the KDD Cup 1999 dataset. The main goal is to train an autoencoder model to learn the patterns of normal network traffic, and subsequently use it to detect anomalous traffic indicative of potential intrusions.

### Overview

The approach and implementation presented here are inspired by the research paper "A Deep Auto-encoder Based Approach for Intrusion Detection System" by Fahimeh Farahnakian and Jukka Heikkonen (2018). The original work proposes using a deep autoencoder to identify anomalies in network traffic, which forms the basis of this project.

- **Research Paper**: [A Deep Auto-encoder Based Approach for Intrusion Detection System](https://www.researchgate.net/publication/324469395_A_deep_auto-encoder_based_approach_for_intrusion_detection_system)

### Dataset

This project uses the **KDD Cup 1999 dataset** to train and evaluate the model. Specifically, the `kddcup.data_10_percent.gz` file, which is a 10% subset of the full dataset, is utilized for training and testing purposes.

- **Data files**:
  - `kddcup.data_10_percent.gz`: Training and testing data subset.
  - `kddcup.names`: Feature names.

### Project Structure

```
autoencoder_kdd/
│
├── data/                   # Directory for storing raw and processed data
│   ├── raw/                # Original dataset files
│   └── processed/          # Preprocessed data for training/testing
│
├── models/                 # Autoencoder model definition and saved models
├── notebooks/              # Jupyter notebooks for data exploration and experiments
├── utils/                  # Helper functions for data preprocessing and evaluation
├── main.py                 # Main script to run the full pipeline
├── requirements.txt        # Required libraries and dependencies
└── README.md               # Overview of the project (this file)
```

### Installation

To run this project, follow the steps below:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd autoencoder_kdd
   ```

2. **Set up a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

### Running the Project

1. **Preprocess the Dataset**:
   - Run the script to preprocess the KDD dataset.
   - This will normalize and one-hot encode features and save the processed data in the `data/processed/` directory.
   ```
   python data/splitDataset.py
   ```

2. **Train the Autoencoder**:
   - Use the preprocessed data to train the autoencoder model.
   ```
   python models/train_autoencoder.py
   ```

3. **Evaluate the Model**:
   - Run the model on test data to identify anomalous traffic based on reconstruction error.


