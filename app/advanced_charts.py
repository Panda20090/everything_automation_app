import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def create_heatmap(file_path, title='Heatmap'):
    df = pd.read_csv(file_path)
    fig = px.imshow(df.corr(), title=title)
    return fig

def create_histogram(file_path, column, title='Histogram'):
    df = pd.read_csv(file_path)
    fig = px.histogram(df, x=column, title=title)
    return fig

def create_pie_chart(file_path, column, title='Pie Chart'):
    df = pd.read_csv(file_path)
    fig = px.pie(df, names=column, title=title)
    return fig
