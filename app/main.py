import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from flask_caching import Cache

df = pd.read_csv(
    'relacionamento_clusters.csv',
    dtype={
        'cod_carteira': str,
        'Grupos': str,
        'cod_coop': str
        }
    )

numeric_columns = df.select_dtypes(include='number').columns

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB],
    requests_pathname_prefix='/'
)

cache = Cache(app.server, config={
    'CACHE_TYPE': 'simple'
})

app.layout = html.Div([
    html.Div([
        html.Label('Selecione a coluna para o eixo X:'),
        dcc.Dropdown(
            id='x-axis-dropdown',
            options=[{'label': col, 'value': col} for col in numeric_columns],
            value='idade'
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label('Selecione a coluna para o eixo Y:'),
        dcc.Dropdown(
            id='y-axis-dropdown',
            options=[{'label': col, 'value': col} for col in numeric_columns],
            value='renda_mensal'
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='scatter-plot'),
    dcc.Graph(id='bar-plot')
])

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value')]
)
@cache.memoize(timeout=60)
def update_scatter_plot(x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, 
                     title=f'Scatter Plot de {x_col} vs {y_col}',
                     color='Grupos',
                     opacity=.7,
                     labels={x_col: x_col, y_col: y_col})
    return fig

@app.callback(
    Output('bar-plot', 'figure'),
    Input('bar-plot', 'id')
)
def update_bar_plot(_):
    proportion_df = df.groupby(['cod_coop', 'Grupos']).size().reset_index(name='counts')
    total_counts = proportion_df.groupby('cod_coop')['counts'].transform('sum')
    proportion_df['proportion'] = proportion_df['counts'] / total_counts

    fig = px.bar(proportion_df, x='cod_coop', y='proportion', color='Grupos',
                 title='Proporção de Grupos em cada cod_coop',
                 labels={'proportion': 'Proporção', 'cod_coop': 'Código Coop'})
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)






#import pandas as pd
#import dash
#import dash_bootstrap_components as dbc
#from dash import dcc
#from dash import html
#from dash.dependencies import Input, Output
#import plotly.express as px
#
#df = pd.read_csv(
#    'relacionamento_clusters.csv',
#    dtype={'cod_carteira': str, 'Grupos': str}
#    )
#
#numeric_columns = df.select_dtypes(include='number').columns
#
#app = dash.Dash(
#    __name__,
#    external_stylesheets=[dbc.themes.SPACELAB],
#    requests_pathname_prefix='/'
#)
#
#app.layout = html.Div([
#    html.Div([
#        dcc.Dropdown(
#            id='x-axis-dropdown',
#            options=[
#                {'label': col, 'value': col} for col in numeric_columns
#            ],
#            value='idade'
#        )
#    ], style={'width': '48%', 'display': 'inline-block'}),
#
#    html.Div([
#        dcc.Dropdown(
#            id='y-axis-dropdown',
#            options=[
#                {'label': col, 'value': col} for col in numeric_columns
#            ],
#            value='renda_mensal'
#        )
#    ], style={'width': '48%', 'display': 'inline-block'}),
#    dcc.Graph(id='scatter-plot')
#])
#
#@app.callback(
#    Output('scatter-plot', 'figure'),
#    [Input('x-axis-dropdown', 'value'),
#     Input('y-axis-dropdown', 'value')]
#)
#def update_scatter_plot(x_col, y_col):
#    fig = px.scatter(
#        df, x=x_col, y=y_col,
#        title=f'Scatter Plot de {x_col} vs {y_col}',
#        color='Grupos', opacity=.7,
#        labels={x_col: x_col, y_col: y_col}
#    )
#    return fig
#
#if __name__ == "__main__":
#    app.run_server(debug=True)





#import pandas as pd
#import dash
#import dash_bootstrap_components as dbc
#from dash import dcc
#from dash import html
#from dash.dependencies import Input, Output
#import plotly.express as px
#from flask_caching import Cache
#
#df = pd.read_csv('relacionamento_clusters.csv', dtype={
#    'cod_carteira': str,
#    'Grupos': str,
#    'cod_coop': str}
#    )
#numeric_columns = df.select_dtypes(include='number').columns
#
#app = dash.Dash(
#    __name__,
#    external_stylesheets=[dbc.themes.SPACELAB],
#    requests_pathname_prefix='/'
#)
#
#cache = Cache(app.server, config={
#    'CACHE_TYPE': 'simple'
#})
#
#app.layout = html.Div([
#    html.Div([
#        dcc.Dropdown(
#            id='x-axis-dropdown',
#            options=[{'label': col, 'value': col} for col in numeric_columns],
#            value='idade'
#        )
#    ], style={'width': '48%', 'display': 'inline-block'}),
#
#    html.Div([
#        dcc.Dropdown(
#            id='y-axis-dropdown',
#            options=[{'label': col, 'value': col} for col in numeric_columns],
#            value='renda_mensal'
#        )
#    ], style={'width': '48%', 'display': 'inline-block'}),
#
#    dcc.Graph(id='scatter-plot')
#])
#
#@app.callback(
#    Output('scatter-plot', 'figure'),
#    [Input('x-axis-dropdown', 'value'),
#     Input('y-axis-dropdown', 'value')]
#)
#@cache.memoize(timeout=60)
#def update_scatter_plot(x_col, y_col):
#    fig = px.scatter(df, x=x_col, y=y_col,
#                     color='Grupos', opacity=.6,
#                     labels={x_col: x_col, y_col: y_col})
#    return fig
#
#if __name__ == "__main__":
#    app.run_server(debug=True)