import os
import json
import openai

openai.api_key = 'your-api-key'

def summarize_code(file_content):
    response = openai.Completion.create(
        model="gpt-4o-mini",
        prompt=f"Summarize the following code:\n\n{file_content}",
        temperature=0.5,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def list_files_and_directories(root_directory):
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

def chunk_file(file_path, chunk_size=5000):
    with open(file_path, 'r') as file:
        content = file.read()
        for i in range(0, len(content), chunk_size):
            yield content[i:i + chunk_size]

def save_file_list(root_directory, output_file="file_list.txt"):
    files_and_dirs = list_files_and_directories(root_directory)

    with open(output_file, 'w') as file:
        json.dump(files_and_dirs, file, indent=4)

    print(f"File list saved to {output_file}")

    # Open each file and summarize
    with open("GPTlog.txt", 'w') as log_file:
        for file in files_and_dirs["files"]:
            file_path = file["path"]
            if os.path.getsize(file_path) > 5000:
                chunk_number = 1
                for chunk in chunk_file(file_path):
                    chunk_path = f"iteration/{os.path.basename(file_path)}.chunk{chunk_number}"
                    with open(chunk_path, 'w') as chunk_file:
                        chunk_file.write(chunk)
                    summary = summarize_code(chunk)
                    log_file.write(f"File: {chunk_path}\nSummary:\n{summary}\n\n")
                    chunk_number += 1
            else:
                with open(file_path, 'r') as f:
                    content = f.read()
                    summary = summarize_code(content)
                    log_file.write(f"File: {file_path}\nSummary:\n{summary}\n\n")

# Example usage
root_directory = "C:\\Users\\GunPr\\OneDrive\\Documents\\GitHub\\everything_automation_app"  # Change this to your project directory
save_file_list(root_directory)
