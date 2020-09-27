# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

df=pd.read_csv('OldFaithful.csv')


app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id='OldFaithful',
        figure={
            'data': [
                go.Scatter(
                    x = df['X'],
                    y = df['Y'],
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout': go.Layout(
                title = 'Oldfaithful Scatterplot',
                xaxis = {'title': 'Duration (min)'},
                yaxis = {'title': 'Interval (min)'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0")

