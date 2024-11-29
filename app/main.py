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

if __name__ == "__main__":
    app.run_server(debug=True)
