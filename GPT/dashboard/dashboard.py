import tkinter as tk
from tkinter import ttk, messagebox
import os
import subprocess
import json

def run_integration():
    """
    Run the integration setup script.
    """
    try:
        subprocess.run(['python', 'setup/run_integration_setup.py'], check=True)
        messagebox.showinfo("Integration", "Integration setup completed successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Integration Error", f"Failed to run integration setup: {e}")

def switch_model(model_choice):
    """
    Switch between OpenAI API and Veronica model.
    
    Parameters:
    model_choice (str): The chosen model ("OpenAI" or "Veronica").
    """
    try:
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
        with open(config_path, 'w') as config_file:
            json.dump({"model": model_choice}, config_file)
        messagebox.showinfo("Model Switch", f"Switched to {model_choice} model")
    except Exception as e:
        messagebox.showerror("Model Switch Error", f"Failed to switch model: {e}")

def create_dashboard():
    """
    Create and display the Tkinter dashboard for the GPT integration.
    """
    root = tk.Tk()
    root.title("GPT Integration Dashboard")

    mainframe = ttk.Frame(root, padding="10 10 10 10")
    mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    model_label = ttk.Label(mainframe, text="Choose Model:")
    model_label.grid(column=1, row=1, sticky=tk.W)

    model_choice = tk.StringVar(value="OpenAI")
    models = ["OpenAI", "Veronica"]
    model_menu = ttk.OptionMenu(mainframe, model_choice, *models)
    model_menu.grid(column=2, row=1, sticky=(tk.W, tk.E))

    run_button = ttk.Button(mainframe, text="Run Integration", command=run_integration)
    run_button.grid(column=1, row=2, sticky=tk.W)

    switch_button = ttk.Button(mainframe, text="Switch Model", command=lambda: switch_model(model_choice.get()))
    switch_button.grid(column=2, row=2, sticky=tk.W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
