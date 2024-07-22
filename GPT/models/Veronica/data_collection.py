import os
import json

def collect_data(log_directory, output_file):
    """
    Collect data from log files and save it to a JSON file.

    Parameters:
        log_directory (str): Directory containing the log files.
        output_file (str): Path to the output JSON file.
    """
    data = []

    for root, _, files in os.walk(log_directory):
        for name in files:
            if name.endswith(".txt"):
                file_path = os.path.join(root, name)
                with open(file_path, 'r') as file:
                    content = file.read()
                    data.append({"file": name, "content": content})

    with open(output_file, 'w') as out_file:
        json.dump(data, out_file, indent=4)

    print(f"Data collected and saved to {output_file}")

if __name__ == "__main__":
    log_directory = "../output_files"
    output_file = "training_data.json"
    collect_data(log_directory, output_file)
