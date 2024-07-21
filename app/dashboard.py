import dash
from dash import dcc, html
import dash_core_components as dcc
import dash_html_components as html

def create_dashboard():
    app = dash.Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(children='Dashboard'),

        html.Div(children='''
            Example dashboard for data visualization.
        '''),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'NYC'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ])

    app.run_server(debug=True)
