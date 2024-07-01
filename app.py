from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_json("C:/Users/student/Desktop/Plotly363/studentdashboard/pp3-4_2566_province.json")
app = Dash()

app.layout = [
    html.H1(children='GraduateStudent66', style={'textAlign':'center'}),
    dcc.Dropdown(df.schools_province.unique(), 'สงขลา', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.schools_province==value]
    return px.bar(dff, x='schools_province', y=['totalmale', 'totalfemale'], barmode='group', 
                 labels={'value': 'Number of Students', 'schools_province': 'Province'},
                 title=f'จำนวนนักเรียนระดับชั้นมัธยมศึกษาปีที่ 6 ที่จบปีการศึกษา 2566 {value}')

if __name__ == '__main__':
    app.run(debug=True)
