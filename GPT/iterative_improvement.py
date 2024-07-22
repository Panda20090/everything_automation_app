import os
import openai
import subprocess
import re

openai.api_key = 'your-api-key'

def summarize_code(file_content):
    response = openai.Completion.create(
        model="gpt-4o-mini",
        prompt=f"Summarize the following code:\n\n{file_content}",
        temperature=0.5,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def verify_code(file_content):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-0125",
        prompt=f"Verify the following code and its dependencies:\n\n{file_content}",
        temperature=0.5,
        max_tokens=200
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

    # Open each file, summarize, verify and log results
    with open("GPTlog.txt", 'w') as log_file, open("corrections_list.txt", 'w') as corrections_file:
        corrections_file.write("Corrections:\n")
        for file in files_and_dirs["files"]:
            file_path = file["path"]
            if os.path.getsize(file_path) > 5000:
                chunk_number = 1
                for chunk in chunk_file(file_path):
                    chunk_path = f"iteration/{os.path.basename(file_path)}.chunk{chunk_number}"
                    with open(chunk_path, 'w') as chunk_file:
                        chunk_file.write(chunk)
                    summary = summarize_code(chunk)
                    verification = verify_code(chunk)
                    log_file.write(f"File: {chunk_path}\nSummary:\n{summary}\n\nVerification:\n{verification}\n\n")
                    if "Failed" in verification:
                        corrections_file.write(f"{chunk_path} needs correction.\n")
                    chunk_number += 1
            else:
                with open(file_path, 'r') as f:
                    content = f.read()
                    summary = summarize_code(content)
                    verification = verify_code(content)
                    log_file.write(f"File: {file_path}\nSummary:\n{summary}\n\nVerification:\n{verification}\n\n")
                    if "Failed" in verification:
                        corrections_file.write(f"{file_path} needs correction.\n")

def extract_imports(file_content):
    imports = re.findall(r'^\s*import\s+(\S+)|^\s*from\s+(\S+)', file_content, re.MULTILINE)
    return set(import[0] or import[1] for import in imports)

def analyze_dependencies(root_directory):
    files_and_dirs = list_files_and_directories(root_directory)
    dependencies = set()

    for file in files_and_dirs["files"]:
        file_path = file["path"]
        if file["type"] == '.py':  # Only analyze Python files
            with open(file_path, 'r') as f:
                content = f.read()
                imports = extract_imports(content)
                dependencies.update(imports)

    return dependencies

def update_requirements(dependencies, requirements_file="requirements.txt"):
    with open(requirements_file, 'w') as f:
        for dependency in dependencies:
            f.write(f"{dependency}\n")

def verify_dependencies(requirements_file="requirements.txt"):
    with open(requirements_file, 'r') as f:
        dependencies = f.readlines()

    for dependency in dependencies:
        dependency = dependency.strip()
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'show', dependency])
            print(f"Dependency {dependency} is installed.")
        except subprocess.CalledProcessError:
            print(f"Dependency {dependency} is not installed. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])

def update_status_and_logs(root_directory):
    files_and_dirs = list_files_and_directories(root_directory)

    with open("current_status.txt", 'w') as status_file, open("test.txt", 'w') as test_file:
        for file in files_and_dirs["files"]:
            file_path = file["path"]
            with open(file_path, 'r') as f:
                content = f.read()
                verification = verify_code(content)
                status_file.write(f"File: {file_path}\nStatus: {'Verified' if 'Verified' in verification else 'Failed'}\n\n")
                test_file.write(f"Test: {file_path}\nResult: {'Pass' if 'Verified' in verification else 'Fail'}\n\n")

def compare_with_scope(scope_file="project_scope.txt"):
    with open(scope_file, 'r') as file:
        scope_content = file.read()

    with open("comparison.txt", 'w') as comparison_file:
        comparison_file.write("Comparisons:\n")
        comparison_file.write(f"Scope:\n{scope_content}\n\n")
        # Add comparison logic here

def create_corrections(corrections_file="corrections_list.txt"):
    with open(corrections_file, 'r') as file:
        corrections = file.readlines()

    for correction in corrections:
        # Implement correction logic here
        pass

# Example usage
root_directory = "C:\\Users\\GunPr\\OneDrive\\Documents\\GitHub\\everything_automation_app"  # Change this to your project directory
save_file_list(root_directory)
dependencies = analyze_dependencies(root_directory)
update_requirements(dependencies)
verify_dependencies()
update_status_and_logs(root_directory)
compare_with_scope()
create_corrections()
