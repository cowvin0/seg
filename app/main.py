import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB],
    requests_pathname_prefix='/'
)

app.layout = html.Div()

if __name__ == "__main__":
    app.run_server(debug=True)