import pandas as pd

def export_to_csv(df, file_path):
    df.to_csv(file_path, index=False)
    return file_path

def export_to_excel(df, file_path):
    df.to_excel(file_path, index=False)
    return file_path

def export_to_json(df, file_path):
    df.to_json(file_path, orient='records', lines=True)
    return file_path
