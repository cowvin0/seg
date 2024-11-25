import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from flask_caching import Cache

df = pd.read_csv(
    'relacionamento_clusters1.csv',
    dtype={
        'cod_carteira': str,
        'cod_coop': str
        }
    )\
    .sort_values('Grupos2')\
    .astype({'Grupos2': str})

numeric_columns = df.select_dtypes(include='number').columns

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.SPACELAB
    ],
    requests_pathname_prefix='/'
)

cache = Cache(
    app.server,
    config={
        'CACHE_TYPE': 'simple'
        }
    )

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='x-axis-dropdown',
            options=[
                {'label': col, 'value': col}
                for col in numeric_columns
            ],
            value='idade'
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
    html.Div([
        dcc.Dropdown(
            id='y-axis-dropdown',
            options=[
                {'label': col, 'value': col}
                for col in numeric_columns
            ],
            value='renda_mensal'
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id='scatter-plot'),
    dcc.Graph(id='bar-plot'),
    html.Div([
        dcc.Dropdown(
            id='box-plot-dropdown',
            options=[
                {'label': col, 'value': col}
                for col in numeric_columns
            ],
            value=numeric_columns[0]
            )
        ], style={'width': '48%', 'display': 'inline-block'}
    ),
    dcc.Graph(id='box-plot')
    ])


@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value')]
)
@cache.memoize(timeout=60)
def update_scatter_plot(x_col, y_col):
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color='Grupos2',
        opacity=.7,
        labels={
            x_col: x_col,
            y_col: y_col
        }
    )
    return fig

@app.callback(
    Output('bar-plot', 'figure'),
    Input('bar-plot', 'id')
)
@cache.memoize(timeout=60)
def update_bar_plot(_):
    proportion_df = df.groupby(['cod_coop', 'Grupos2']).size().reset_index(name='counts')
    total_counts = proportion_df.groupby('cod_coop')['counts'].transform('sum')
    proportion_df['proportion'] = proportion_df['counts'] / total_counts

    fig = px.bar(
        proportion_df,
        x='cod_coop',
        y='proportion',
        color='Grupos2',
        labels={
            'proportion': 'Proporção',
            'cod_coop': 'Código Coop'
        }
    )
    return fig

@app.callback(
    Output('box-plot', 'figure'),
    Input('box-plot-dropdown', 'value')
)
@cache.memoize(timeout=60)
def update_box_plot(selected_col):
    fig = px.box(
        df,
        color='Grupos2',
        y=selected_col,
        labels={
            selected_col: selected_col
        }
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
