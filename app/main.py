import pandas as pd
import dash
import dash_bootstrap_components as dbc
import plotly.express as px

from pages.navbar import navbar
from dash import dcc, html, Input, Output, State
from flask_caching import Cache

#df = pd.read_csv(
#    'relacionamento_clusters.csv',
#    dtype={
#        'desc_cnae': str,
#        'cod_cnae': str,
#        'cod_carteira': str,
#        'cod_coop': str,
#        'cad_pix': str,
#        'cod_central': str,
#        'ano_mes': str,
#        'num_conta_principal': str,
#        'cod_ua': str,
#        'num_cpf_cnpj': str,
#        }
#    )\
#    .sort_values('Grupos')\
#    .astype({'Grupos': str})
#
#df = df\
#    .astype(
#        {
#            col: str for col in
#            df.columns[df.columns.str.startswith('prod_')].tolist() +
#            df.columns[df.columns.str.startswith('flg_')].tolist() +
#            df.columns[df.columns.str.contains('fone')].tolist() +
#            df.columns[df.columns.str.contains('possui')].tolist() +
#            df.columns[df.columns.str.startswith('mobi_')].tolist() +
#            df.columns[df.columns.str.startswith('digital_')].tolist() +
#            df.columns[df.columns.str.startswith('ib_')].tolist()
#        }
#    )
#
#df_grupos = df\
#    .loc[:, ['Grupos'] +
#         df.columns[df.columns.str.startswith('prod_')].tolist()
#    ]\
#    .set_index('Grupos')\
#    .stack()\
#    .reset_index(name='possui')\
#    .astype({'possui': int})\
#    .rename(columns={'level_1': 'produto'})\
#    .groupby(['Grupos', 'produto'])\
#    .possui.sum()\
#    .reset_index(name='total_produto')
#
#numeric_columns = df.select_dtypes(include='number').columns

app = dash.Dash(
    __name__,
    title='Associados - CENTRAL NORDESTE',
    external_stylesheets=[
        dbc.themes.COSMO
    ],
    use_pages=True,
    update_title=False,
    suppress_callback_exceptions=True,
    requests_pathname_prefix='/'
)

app.layout = html.Div(
    [
        navbar(),
        dash.page_container
    ]
)

#cache = Cache(
#    app.server,
#    config={
#        'CACHE_TYPE': 'simple'
#        }
#    )

#SIC_LOGO = "./assets/sicredi-logo.png"
#
#navbar = dbc.Navbar(
#    dbc.Container(
#        [
#            html.A(
#                dbc.Row(
#                    [
#                        dbc.Col(html.Img(src=SIC_LOGO, height="30px")),
#                    ],
#                    align="left",
#                    className="g-0",
#                ),
#                href="https://www.sicredi.com.br",
#                style={"textDecoration": "none"},
#            ),
#            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
#            dbc.Collapse(
#                dbc.Nav(
#                    [
#                        dbc.NavLink("Sobre", href="/", active="exact"),
#                        dbc.NavLink("Conheça seus associados", href="/nova-pagina", active="exact"),
#                    ],
#                    className="ms-auto",
#                    navbar=True,
#                ),
#                id="navbar-collapse",
#                is_open=False,
#                navbar=True,
#            ),
#        ]
#    ),
#    color="secondary",
#    dark=True,
#)
#
#app.layout = html.Div([
#    html.Div([
#        dcc.Dropdown(
#            id='x-axis-dropdown',
#            options=[
#                {'label': col, 'value': col}
#                for col in numeric_columns
#            ],
#            value='idade'
#            )
#        ], style={'width': '48%', 'display': 'inline-block'}),
#    html.Div([
#        dcc.Dropdown(
#            id='y-axis-dropdown',
#            options=[
#                {'label': col, 'value': col}
#                for col in numeric_columns
#            ],
#            value='renda_mensal'
#            )
#        ], style={'width': '48%', 'display': 'inline-block'}),
#    dcc.Graph(id='scatter-plot'),
#    dcc.Graph(id='bar-plot'),
#    html.Div([
#        dcc.Dropdown(
#            id='box-plot-dropdown',
#            options=[
#                {'label': col, 'value': col}
#                for col in numeric_columns
#            ],
#            value=numeric_columns[0]
#            )
#        ], style={'width': '48%', 'display': 'inline-block'}
#    ),
#    dcc.Graph(id='box-plot'),
#    html.Div([
#        dcc.Dropdown(
#            id='group-dropdown',
#            options=[
#                {'label': f'Grupo {grupo}', 'value': grupo}
#                for grupo in df_grupos['Grupos'].unique()
#            ],
#            value=df_grupos['Grupos'].unique().tolist(),
#            multi=True
#        )
#    ], style={'width': '48%', 'display': 'inline-block'}),
#    dcc.Graph(id='total-products-bar-plot')
#    ])
#
#app.layout = [navbar, app.layout]
#
#
#@app.callback(
#    Output('scatter-plot', 'figure'),
#    [Input('x-axis-dropdown', 'value'),
#     Input('y-axis-dropdown', 'value')]
#)
#@cache.memoize(timeout=60)
#def update_scatter_plot(x_col, y_col):
#    fig = px.scatter(
#        df,
#        x=x_col,
#        y=y_col,
#        color='Grupos',
#        opacity=.7,
#        labels={
#            x_col: x_col,
#            y_col: y_col
#        }
#    )
#    return fig
#
#@app.callback(
#    Output('bar-plot', 'figure'),
#    Input('bar-plot', 'id')
#)
#@cache.memoize(timeout=60)
#def update_bar_plot(_):
#    proportion_df = df.groupby(['cod_coop', 'Grupos']).size().reset_index(name='counts')
#    total_counts = proportion_df.groupby('cod_coop')['counts'].transform('sum')
#    proportion_df['proportion'] = proportion_df['counts'] / total_counts
#
#    fig = px.bar(
#        proportion_df,
#        x='cod_coop',
#        y='proportion',
#        color='Grupos',
#        barmode='group',
#        labels={
#            'proportion': 'Proporção',
#            'cod_coop': 'Código Coop'
#        }
#    )
#    return fig
#
#@app.callback(
#    Output('box-plot', 'figure'),
#    Input('box-plot-dropdown', 'value')
#)
#@cache.memoize(timeout=60)
#def update_box_plot(selected_col):
#    fig = px.box(
#        df,
#        color='Grupos',
#        y=selected_col,
#        labels={
#            selected_col: selected_col
#        }
#    )
#    return fig
#
#@app.callback(
#    Output('total-products-bar-plot', 'figure'),
#    [Input('total-products-bar-plot', 'id'),
#     Input('group-dropdown', 'value')]
#)
#@cache.memoize(timeout=60)
#def update_total_products_bar_plot(_, selected_groups):
#    filtered_df = df_grupos[df_grupos['Grupos'].isin(selected_groups)]
#    fig = px.bar(
#        filtered_df,
#        x='Grupos',
#        y='total_produto',
#        color='produto',
#        labels={
#            'total_produto': 'Total de Produtos',
#            'Grupos': 'Grupos'
#        },
#        title='Total de Produtos por Grupo'
#    )
#    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
