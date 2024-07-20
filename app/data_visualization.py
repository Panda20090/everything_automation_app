import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(file_path, title, output_file):
    data = pd.read_csv(file_path)
    fig, ax = plt.subplots()
    data.plot(ax=ax)
    ax.set_title(title)
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    plt.savefig(output_file)
    return output_file
