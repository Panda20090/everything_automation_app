import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_heatmap(file_path, title='Heatmap'):
    df = pd.read_csv(file_path)
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title(title)
    plt.show()

def create_histogram(file_path, column, title='Histogram'):
    df = pd.read_csv(file_path)
    plt.figure(figsize=(10, 8))
    sns.histplot(df[column], kde=True)
    plt.title(title)
    plt.show()

def create_pie_chart(file_path, column, title='Pie Chart'):
    df = pd.read_csv(file_path)
    plt.figure(figsize=(10, 8))
    df[column].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title(title)
    plt.ylabel('')
    plt.show()
