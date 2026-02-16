from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder(return_type='pandas')
countries = df["country"].drop_duplicates()


app = Dash(__name__) 
server = app.server

app.layout = html.Div([ 
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": c, "value": c} for c in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth") # And the graph itself has to have an ID
])


@app.callback( 
    Output("gdp-growth", "figure"),
    Input("country-dropdown", "value")
)

def update_graph(country):
    df_country = df[df["country"] == country]
    fig = px.line(
        df_country,
        x="year",
        y="gdpPercap",
        title=f"GDP per Capita — {country}"
    )
    return fig

if __name__ == "__main__": 
    app.run(debug=True)