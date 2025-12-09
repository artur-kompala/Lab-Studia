import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

df = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='continent-dropdown',
        options=[{'label': c, 'value': c} for c in df['continent'].unique()],
        value='Asia',
        clearable=False
    ),
    dcc.Slider(
        id='year-slider',
        min=int(df['year'].min()),
        max=int(df['year'].max()),
        step=5,
        value=int(df['year'].min()),
        marks={int(y): str(y) for y in df['year'].unique()}
    ),
    dcc.Graph(id='gdp-graph'),
    dcc.Graph(id='lifeexp-graph')
])

@app.callback(
    Output('gdp-graph', 'figure'),
    Output('lifeexp-graph', 'figure'),
    Input('continent-dropdown', 'value'),
    Input('year-slider', 'value')
)
def update_graphs(selected_continent, selected_year):
    year = int(selected_year)
    filtered_df = df[(df['continent'] == selected_continent) & (df['year'] == year)]

    if filtered_df.empty:
        empty_fig = go.Figure()
        empty_fig.update_layout(title="Brak danych")
        return empty_fig, empty_fig

    fig_gdp = px.bar(filtered_df, x="country", y="gdpPercap",
                     title=f"GDP per Capita ({year}) — {selected_continent}")
    fig_lifeexp = px.bar(filtered_df, x="country", y="lifeExp",
                         title=f"Długość życia ({year}) — {selected_continent}")
    return fig_gdp, fig_lifeexp

if __name__ == '__main__':
    app.run(debug=True)
