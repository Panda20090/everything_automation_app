from flask import Flask, request, jsonify
import os
import json
import subprocess
import openai
import re
import sys
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure environment variables are set
openai.api_key = os.getenv('API_KEY')

# Ensure the output directory exists
output_dir = os.path.join(os.path.dirname(__file__), '../output_files')
os.makedirs(output_dir, exist_ok=True)

# Helper functions from existing scripts
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

def extract_imports(file_content):
    imports = re.findall(r'^\s*import\s+(\S+)|^\s*from\s+(\S+)', file_content, re.MULTILINE)
    return set(imp[0] or imp[1] for imp in imports)  # Renamed variable to imp

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

def run_tests():
    result = subprocess.run(['python', '-m', 'unittest', 'discover', 'tests'], capture_output=True, text=True)
    test_results_path = os.path.join(output_dir, "test_results.txt")
    with open(test_results_path, 'w') as file:
        file.write(result.stdout)
    return result.stdout

# API endpoints
@app.route('/summarize', methods=['POST'])
def summarize():
    content = request.json.get('content')
    if content:
        summary = summarize_code(content)
        return jsonify({"summary": summary})
    return jsonify({"error": "No content provided"}), 400

@app.route('/verify', methods=['POST'])
def verify():
    content = request.json.get('content')
    if content:
        verification = verify_code(content)
        return jsonify({"verification": verification})
    return jsonify({"error": "No content provided"}), 400

@app.route('/dependencies', methods=['GET'])
def dependencies():
    root_directory = os.getenv('ROOT_DIRECTORY')
    if root_directory:
        dependencies = analyze_dependencies(root_directory)
        return jsonify({"dependencies": list(dependencies)})
    return jsonify({"error": "Root directory not set"}), 400

@app.route('/update-requirements', methods=['POST'])
def update_requirements_endpoint():
    dependencies = request.json.get('dependencies')
    if dependencies:
        update_requirements(set(dependencies))
        return jsonify({"message": "Requirements updated"})
    return jsonify({"error": "No dependencies provided"}), 400

@app.route('/verify-dependencies', methods=['POST'])
def verify_dependencies_endpoint():
    try:
        verify_dependencies()
        return jsonify({"message": "Dependencies verified and installed"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/run-tests', methods=['POST'])
def run_tests_endpoint():
    test_results = run_tests()
    return jsonify({"test_results": test_results})

if __name__ == '__main__':
    app.run(debug=True)
