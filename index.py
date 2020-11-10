import dash
import dash_html_components as html
import dash_table
from dash.dependencies import Output, Input, State

records = [{'produto': '1559-LOC?O HIDRATANTE LA VIDA', 'vlvenda': 158432.45, 'qtvenda': 10707.0, 'vllucro': 82052.68}, {'produto': '1788-LOC?O HIDRATANTE LA LUNA', 'vlvenda': 128389.8, 'qtvenda': 9300.0, 'vllucro': 65448.91}, {'produto': '2226-DEO COLONIA KISS 100ML LATA', 'vlvenda': 97283.56, 'qtvenda': 3595.0, 'vllucro': 20736.74}, {'produto': '2127-LOC?O HIDRATANTE KISS', 'vlvenda': 78700.25, 'qtvenda': 5504.0, 'vllucro': 43699.92}, {'produto': '2539-DEO COLONIA NAH HELLO HELLO LATA', 'vlvenda': 53128.46, 'qtvenda': 1626.0, 'vllucro': 20949.33}, {'produto': '2201-DEO COLONIA BEE 100ML', 'vlvenda': 48054.54, 'qtvenda': 2051.0, 'vllucro': 18640.04}, {'produto': '2224-DEO COLONIA PINGUCHO 100ML', 'vlvenda': 32752.05, 'qtvenda': 1421.0, 'vllucro': 14712.61}, {'produto': '1110-LOC?O HIDRATANTE DREAM 240 ML ', 'vlvenda': 30508.45, 'qtvenda': 2096.0, 'vllucro': 17166.85}, {'produto': '2310-DEO COLONIA CICI MEL', 'vlvenda': 28159.29, 'qtvenda': 1195.0, 'vllucro': 10395.01}, {'produto': '2222-DEO COLONIA  RINO 100ML', 'vlvenda': 27651.82, 'qtvenda': 1194.0, 'vllucro': 12587.1},{'produto': '1559-LOC?O HIDRATANTE LA VIDA', 'vlvenda': 158432.45, 'qtvenda': 10707.0, 'vllucro': 82052.68}, {'produto': '1788-LOC?O HIDRATANTE LA LUNA', 'vlvenda': 128389.8, 'qtvenda': 9300.0, 'vllucro': 65448.91}, {'produto': '2226-DEO COLONIA KISS 100ML LATA', 'vlvenda': 97283.56, 'qtvenda': 3595.0, 'vllucro': 20736.74}, {'produto': '2127-LOC?O HIDRATANTE KISS', 'vlvenda': 78700.25, 'qtvenda': 5504.0, 'vllucro': 43699.92}, {'produto': '2539-DEO COLONIA NAH HELLO HELLO LATA', 'vlvenda': 53128.46, 'qtvenda': 1626.0, 'vllucro': 20949.33}, {'produto': '2201-DEO COLONIA BEE 100ML', 'vlvenda': 48054.54, 'qtvenda': 2051.0, 'vllucro': 18640.04}, {'produto': '2224-DEO COLONIA PINGUCHO 100ML', 'vlvenda': 32752.05, 'qtvenda': 1421.0, 'vllucro': 14712.61}, {'produto': '1110-LOC?O HIDRATANTE DREAM 240 ML ', 'vlvenda': 30508.45, 'qtvenda': 2096.0, 'vllucro': 17166.85}, {'produto': '2310-DEO COLONIA CICI MEL', 'vlvenda': 28159.29, 'qtvenda': 1195.0, 'vllucro': 10395.01}, {'produto': '2222-DEO COLONIA  RINO 100ML', 'vlvenda': 27651.82, 'qtvenda': 1194.0, 'vllucro': 12587.1}]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3("Tests area"),
    html.Div([
        dash_table.DataTable(
            id="table",
            columns=[
                {
                    'name': i,
                    'id': i,
                    'type': 'numeric' if i in ('vlvenda', 'vllucro', 'qtvenda' ) else 'text',
                    'deletable': False,
                    'selectable': False,
                    'hideable': False,
                } for i in [ 'produto', 'qtvenda', 'vlvenda', 'vllucro' ]
            ],
            style_header=dict(backgroundColor="#399fb5", color="white", fontWeight="bold", textTransform="uppercase"),
            filter_action="custom",
            sort_action="custom",
            sort_mode="multi",
            virtualization=False,
            page_action="custom",
        ),
    ], style=dict(width="600px", height="380px", margin="0 auto")),
    html.Div(id="input-bobo")
], style=dict(margin="0 auto"))

@app.callback(
    Output("table", "data"),
    [
        Input("input-bobo", "children"),
        Input("table", "page_size")
    ]
)
def populate_table(*args):
    [ _, page_size ] = args
    print("Comming to populate table")
    print("page_size:", page_size)
    return records

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=3001)