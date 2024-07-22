from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import json

# Load data
df = pd.read_json("pp3-4_2566_province.json")

# Initialize the app
app = Dash()

# Load GeoJSON of Thailand
with open('thailand.json') as f:
    thailand_geojson = json.load(f)

# Define the layout of the app
app.layout = html.Div([
    html.H1(children='GraduateStudent66', style={'textAlign': 'center', 'color': 'white'}),
    
    html.Div([
        html.Div([
            dcc.Dropdown(df.schools_province.unique(), 'Songkhla', id='dropdown-selection'),
            dcc.Graph(id='graph-content'),
        ], style={'grid-area': 'left', 'color': 'black'}),
        
        dcc.Graph(id='map-content', style={'grid-area': 'right','height': '100vh', 'width': '100%'})  # Updated style for map
    ], style={
        'display': 'grid',
        'grid-template-areas': '''
            'left right'
        ''',
        'grid-template-columns': '2fr 4fr',
        'grid-template-rows': 'auto',
        'gap': '10px',
        'padding': '10px'
    })
], style={'background': '#121212', 'margin': '0', 'padding': '0', 'height': '100vh', 'color': 'white'})

# Callback to update bar graph
@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.schools_province == value]
    fig = px.bar(dff, x='schools_province', y=['totalmale', 'totalfemale'], barmode='group',
                 labels={'value': 'Number of Students', 'schools_province': 'Province'},
                 title=f'จำนวนนักเรียนระดับชั้นมัธยมศึกษาปีที่ 6 ที่จบปีการศึกษา 2566 {value}')
    
    fig.update_layout(
        plot_bgcolor='#1e1e1e',
        paper_bgcolor='#121212',
        font_color='white',
        margin=dict(l=0, r=0, t=30, b=0)  # Remove margins
    )
    
    return fig

# Callback to update map
@callback(
    Output('map-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_map(_):
    fig = px.choropleth(
        df,
        geojson=thailand_geojson,
        locations='schools_province',
        featureidkey="properties.name",
        color='totalstd',
        color_continuous_scale="Reds",
        scope="asia",
        hover_data={'schools_province': True, 'totalmale': True, 'totalfemale': True, 'pp3year': True, 'level': True}
    )
    
    # Update layout of the map
    fig.update_geos(
        fitbounds="locations",
        visible=False,
        bgcolor='#121212'  # Set background color of map
    )
    fig.update_layout(
        title="Choropleth Map of Thailand",
        title_font_color='white',
        paper_bgcolor='#121212',
        plot_bgcolor='#1e1e1e',
        font_color='white',
        margin=dict(l=0, r=0, t=30, b=0)  # Remove margins
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
