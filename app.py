import dash
import dash_core_components as dcc
import dash_html_components as html
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import datetime

mill_to_min = 60000
postgreSQLTable = "CovidTableCH"
#see docker-compose file links
postgresql_conn_string = 'postgresql+psycopg2://postgres:postgres@pgsql/postgres'
query_select_data = 'select datum, sum(entries) from "{}" group by datum ORDER BY datum ASC'.format(postgreSQLTable)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    html.Div([
        html.H4('Corona virus Dashboard CH'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*mill_to_min, # in milliseconds
            n_intervals=0
        )
    ])
)

@app.callback(Output('live-update-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Last update on (in utc time): {}'.format(datetime.datetime.now()), style=style),
    ]

# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    alchemyEngine = create_engine(postgresql_conn_string, pool_recycle=3600)
    df_out = pd.read_sql_query(query_select_data, con=alchemyEngine)
    fig = px.line(df_out, x='datum', y='sum',
                  labels={
                     "datum": "Date of the test",
                     "sum": "Number of positive tests"
                 },
                title="Timeseries positive test in CH")
    return fig


if __name__ == '__main__':
  app.run_server(host='0.0.0.0', port=8080, debug=True)