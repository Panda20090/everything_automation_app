from dash import dcc, html
import dash
import pandas as pd
import plotly.express as px

def create_dashboard():
    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.H1("Data Automation Dashboard"),
        dcc.Tabs(id="tabs", children=[
            dcc.Tab(label='Google Trends Data', children=[
                html.Div([
                    dcc.Graph(id='google-trends-graph')
                ])
            ]),
            dcc.Tab(label='Twitter Data', children=[
                html.Div([
                    dcc.Graph(id='twitter-graph')
                ])
            ])
        ])
    ])

    @app.callback(
        dash.dependencies.Output('google-trends-graph', 'figure'),
        [dash.dependencies.Input('tabs', 'value')]
    )
    def update_google_trends_graph(tab):
        df = pd.read_csv('data/cleaned_google_trends_data.csv')
        fig = px.line(df, x='date', y='normalized_value', title='Google Trends Data')
        return fig

    @app.callback(
        dash.dependencies.Output('twitter-graph', 'figure'),
        [dash.dependencies.Input('tabs', 'value')]
    )
    def update_twitter_graph(tab):
        df = pd.read_csv('data/cleaned_twitter_data.csv')
        fig = px.line(df, x='created_at', y='text', title='Twitter Data')
        return fig

    app.run_server(debug=True)

if __name__ == '__main__':
    create_dashboard()
