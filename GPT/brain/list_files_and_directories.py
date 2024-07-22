import os
import json
import openai
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure the OpenAI API key is set via environment variable
openai.api_key = os.getenv('API_KEY')

def summarize_code(file_content):
    """
    Summarize the provided code content using OpenAI API.
    
    Parameters:
        file_content (str): The content of the code file.

    Returns:
        str: Summary of the code.
    """
    try:
        response = openai.Completion.create(
            model="gpt-4o-mini",
            prompt=f"Summarize the following code:\n\n{file_content}",
            temperature=0.5,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error summarizing code: {e}")
        return ""

def list_files_and_directories(root_directory):
    """
    List all files and directories within the root_directory.
    
    Parameters:
        root_directory (str): The root directory to search for files and directories.

    Returns:
        dict: A dictionary containing lists of files and directories.
    """
    files_and_dirs = {
        "files": [],
        "directories": []
    }

    for root, dirs, files in os.walk(root_directory):
        for name in files:
            files_and_dirs["files"].append({
                "path": os.path.join(root, name),
                "type": os.path.splitext(name)[1].lower()  # File extension
            })
        for name in dirs:
            files_and_dirs["directories"].append(os.path.join(root, name))

    return files_and_dirs

def save_file_list(root_directory, output_file="file_list.txt"):
    """
    Save a list of files and directories in the root directory to a JSON file.
    
    Parameters:
        root_directory (str): The root directory to list files and directories from.
        output_file (str): The name of the output file.
    """
    files_and_dirs = list_files_and_directories(root_directory)

    with open(output_file, 'w') as file:
        json.dump(files_and_dirs, file, indent=4)

    logging.info(f"File list saved to {output_file}")

    summarize_files(files_and_dirs)

def summarize_files(files_and_dirs):
    """
    Summarize the content of each file and log the summaries.
    
    Parameters:
        files_and_dirs (dict): A dictionary containing lists of files and directories.
    """
    log_file_path = "GPTlog.txt"
    with open(log_file_path, 'w') as log_file:
        for file in files_and_dirs["files"]:
            file_path = file["path"]
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    summary = summarize_code(content)
                    log_file.write(f"File: {file_path}\nSummary:\n{summary}\n\n")
            except Exception as e:
                logging.error(f"Error reading file {file_path}: {e}")

    logging.info(f"Summaries saved to {log_file_path}")

if __name__ == "__main__":
    root_directory = os.getenv('ROOT_DIRECTORY')
    if not root_directory:
        logging.error("ROOT_DIRECTORY environment variable is not set.")
    else:
        save_file_list(root_directory)
