import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def enhanced_visualization(file_path, chart_type='line', title='Enhanced Visualization'):
    df = pd.read_csv(file_path)
    
    if chart_type == 'line':
        fig = px.line(df, title=title)
    elif chart_type == 'bar':
        fig = px.bar(df, title=title)
    elif chart_type == 'scatter':
        fig = px.scatter(df, title=title)
    else:
        fig = px.line(df, title=title)  # Default to line chart

    # Add annotations
    fig.update_layout(
        annotations=[
            go.layout.Annotation(
                text="This is an annotation",
                x=df.index[len(df)//2],  # Example position
                y=df.iloc[len(df)//2][1],  # Example position
                showarrow=True,
                arrowhead=2
            )
        ]
    )
    return fig
