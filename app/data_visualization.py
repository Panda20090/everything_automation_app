import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(file_path, title, output_file):
    df = pd.read_csv(file_path)
    plt.figure(figsize=(10, 8))
    df.plot(kind='bar')
    plt.title(title)
    plt.savefig(output_file)
    return output_file
