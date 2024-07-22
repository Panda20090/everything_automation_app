import os
import json
import openai

openai.api_key = os.getenv('API_KEY')

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

def save_file_list(root_directory, output_file="file_list.txt"):
    files_and_dirs = list_files_and_directories(root_directory)

    with open(output_file, 'w') as file:
        json.dump(files_and_dirs, file, indent=4)

    print(f"File list saved to {output_file}")

    # Open each file and summarize
    with open("GPTlog.txt", 'w') as log_file:
        for file in files_and_dirs["files"]:
            file_path = file["path"]
            with open(file_path, 'r') as f:
                content = f.read()
                summary = summarize_code(content)
                log_file.write(f"File: {file_path}\nSummary:\n{summary}\n\n")

if __name__ == "__main__":
    root_directory = os.getenv('ROOT_DIRECTORY')
    save_file_list(root_directory)
