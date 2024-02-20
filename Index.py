import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Define o layout do aplicativo
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Exemplo de Dashboard com Dash"),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Opção 1', 'value': '1'},
            {'label': 'Opção 2', 'value': '2'},
            {'label': 'Opção 3', 'value': '3'},
        ],
        value='1',
        clearable=False
    ),
    dcc.Graph(id='graph')
])

# Define a função para atualizar o gráfico
@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_figure(selected_value):
    if selected_value == '1':
        y_values = [1, 2, 3]
    elif selected_value == '2':
        y_values = [4, 5, 6]
    else:
        y_values = [7, 8, 9]

    return {
        'data': [{
            'x': [1, 2, 3],
            'y': y_values
        }],
        'layout': {
            'title': 'Gráfico Interativo',
            'xaxis': {
                'title': 'X'
            },
            'yaxis': {
                'title': 'Y'
            }
        }
    }

# Inicia o aplicativo
if __name__ == '__main__':
    app.run_server(debug=False)
