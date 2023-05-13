import dash
import plotly.express as px
import pandas as pd 
from dash import dcc,html
from dash.dependencies import Input,Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1('Diot UIS'),
        html.Img(src='assets/images/logo.png')
    ], className = 'banner'),
    html.Div([
        html.Div(
            children=[
                html.Ul(
                    children=[
                        html.Li(html.A("Inicio", href="#")),
                        html.Li(html.A("Opción 1", href="#")),
                        html.Li(html.A("Opción 2", href="#")),
                        html.Li(html.A("Opción 3", href="#")),
                    ]
                )
            ]
        ),
    ], className = 'sidebar'),
    
    html.Div([
        html.Div([
            dcc.Graph(id = 'my_graph', figure = {})
        ], className = 'create_container2 eight columns'),
        html.Div([
            dcc.Graph(id = 'my_graph', figure = {})
        ], className = 'create_container2 eight columns'),
    ], className = 'row flex-display'),
])

if __name__ == ('__main__'):
    app.run_server(debug=True)