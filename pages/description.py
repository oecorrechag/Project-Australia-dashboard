from dash import html
import dash_bootstrap_components as dbc

from components.CallbacksDescription import Menu
from components.CallbacksDescription import Page1Graph1
from components.CallbacksDescription import Page1Graph2
from components.CallbacksDescription import MultipleTimeSeries


layout1 = html.Div([

    dbc.Row(children=[
        dbc.Col([
            Menu,
            html.Br(),
            Page1Graph1,
            html.Br(),
            Page1Graph2, 
        ], md=6),
        dbc.Col(MultipleTimeSeries, md=6),
    ]),
    
], style={"padding": "0px 20px 0px 100px"})
