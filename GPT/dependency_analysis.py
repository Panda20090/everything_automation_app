import os
import re
import subprocess

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

# Example usage
verify_dependencies()


# Example usage
root_directory = "C:\\Users\\GunPr\\OneDrive\\Documents\\GitHub\\everything_automation_app"  # Change this to your project directory
dependencies = analyze_dependencies(root_directory)
update_requirements(dependencies)
