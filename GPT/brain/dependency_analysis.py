import os
import subprocess
import re
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure the output directory exists
output_dir = os.path.join(os.path.dirname(__file__), '../output_files')
os.makedirs(output_dir, exist_ok=True)

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

def extract_imports(file_content):
    imports = re.findall(r'^\s*import\s+(\S+)|^\s*from\s+(\S+)', file_content, re.MULTILINE)
    return set(imp[0] or imp[1] for imp in imports)

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
    output_path = os.path.join(output_dir, requirements_file)
    with open(output_path, 'w') as f:
        for dependency in dependencies:
            f.write(f"{dependency}\n")

def verify_dependencies(requirements_file="requirements.txt"):
    requirements_path = os.path.join(output_dir, requirements_file)
    with open(requirements_path, 'r') as f:
        dependencies = f.readlines()

    for dependency in dependencies:
        dependency = dependency.strip()
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'show', dependency])
            logging.info(f"Dependency {dependency} is installed.")
        except subprocess.CalledProcessError:
            logging.info(f"Dependency {dependency} is not installed. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])

if __name__ == "__main__":
    root_directory = os.getenv('ROOT_DIRECTORY')
    if not root_directory:
        logging.error("ROOT_DIRECTORY environment variable is not set.")
    else:
        dependencies = analyze_dependencies(root_directory)
        update_requirements(dependencies)
        verify_dependencies()
