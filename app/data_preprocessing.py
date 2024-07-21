import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(file_path, target_column):
    df = pd.read_csv(file_path)
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    preprocessed_file = 'data/preprocessed_data.csv'
    pd.concat([X_train, y_train], axis=1).to_csv(preprocessed_file, index=False)
    return preprocessed_file
