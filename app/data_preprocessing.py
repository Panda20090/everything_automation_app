import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(file_path, target_column):
    df = pd.read_csv(file_path)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Encode categorical variables
    X = pd.get_dummies(X)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Encode target variable if it's categorical
    if y.dtype == 'object':
        encoder = LabelEncoder()
        y = encoder.fit_transform(y)

    preprocessed_file = 'data/preprocessed_data.csv'
    pd.DataFrame(X_scaled, columns=X.columns).to_csv(preprocessed_file, index=False)
    pd.DataFrame(y, columns=[target_column]).to_csv(preprocessed_file, mode='a', header=True, index=False)

    return preprocessed_file
