import os
import json

def read_json(file_path):
    """
    Read a JSON file and return its contents.

    Parameters:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Contents of the JSON file.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    """
    Save data to a JSON file.

    Parameters:
        data (dict): Data to save.
        file_path (str): Path to the JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def create_directory(dir_path):
    """
    Create a directory if it doesn't exist.

    Parameters:
        dir_path (str): Path to the directory.
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
