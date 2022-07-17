# If you prefer to run the code online instead of on your computer click:
# https://github.com/Coding-with-Adam/Dash-by-Plotly#execute-code-in-browser

from dash import Dash, dcc, Output, Input, dash_table  # pip install dash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd 
import json                       # pip install pandas
city_list={
    'New York City':[
        '../nyc-precinct-wise-dataset.csv',
        '../first-phase/New York/New York Police Precincts.geojson',
        '../new-york-city.json'
    ],
    'Washington DC':[
        '../wdc-precinct-wise-dataset.csv',
        '../first-phase/Washington DC/WashingtonDC-precinct.geojson',
        '../washington-city.json',
    ],
    'Seattle': [
        '../seattle-precinct-wise-dataset.csv',
        '../first-phase/Seattle/Seattle-prcinct.geojson',
        '../seattle.json'
    ]
}
file=None

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
mytitle = dcc.Markdown(children='')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=["New York City", "Washington DC", "Seattle", "Boston"],
                        value='New York City',  # initial value displayed when page first loads
                        clearable=False)
age = dcc.Input(placeholder='Enter Age',
                type='number',value=None)
# Customize your own Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([dropdown], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([mygraph], width=12)
    ]),
    dbc.Row([
        dbc.Col([age], width=3)
    ], justify='center')
], fluid=True)

def helper1(file):
    if file != None:
        return file
    fileArr=[
        './crimes/arson.csv', 
        './crimes/assault.csv',
        './crimes/fraud.csv',
        './crimes/gun-violence.csv',
        './crimes/harrassment.csv',
        './crimes/motor-vehicle-accidents.csv',
        './crimes/murder.csv',
        './crimes/robbery.csv',
        './crimes/sex-crime.csv',
        './crimes/drug-overdose-victims.csv',
        './crimes/Missing-Persons.csv',
        './crimes/Human-Trafficking.csv'
    ]
    file=[]
    for path in fileArr:
        file.append(pd.read_csv(path))
    return file

# Callback allows components to interact
def driver(city,age):
    
    global file
    file=helper1(file)
 
    crime_data = pd.read_csv(city_list[city][0])
    crime_data = crime_data.iloc[:, 1:]
    crimes = crime_data.columns
    li = []

    for df in file:
        for _, row in df.iterrows():
            key = row.keys()[0]
            if key in crimes:
                if age >= row['low'] and age <= row['up']:
                    if key == 'Robbery':
                        li.append({'Theft': row['Points']})
                        crime_data['Theft'] = crime_data['Theft']*row['Points']
                    li.append({key: row['Points']})
                    crime_data[key] = crime_data[key]*row['Points']
                    # print(crime_data.head(1))
                    break
            else:
                break
    if 'Others' in crimes:
        crime_data['Others'] = crime_data['Others']*2.5
        li.append({'Others': 2.5})
    if 'Public Nuisance' in crimes:
        crime_data['Public Nuisance'] = crime_data['Public Nuisance']*2.5
        li.append({'Public Nuisance': 2.5})
    # print(li)
    li1 = []
    crime_data = crime_data.fillna(0)
    for index, row in crime_data.iterrows():
        li1.append(sum([float(x) for x in row[2:].values]))
    crime_data['total'] = li1
    return crime_data,li


@app.callback(
    Output(mygraph, 'figure'),
    Output(mytitle, 'children'),
    Input(dropdown, 'value'),
    Input(age, 'value')
)

def update_graph(city, age):  # function arguments come from the component property of the Input
    if age==None:
        age=18
    crime_data,points=driver(city,age)
    print(city)
    print(type(city))
    data=json.load(open(city_list[city][2]))
    lat=data['latitude']
    long=data['longitude']
    precincts=json.load(open(city_list[city][1],'r'))
    # https://plotly.com/python/choropleth-maps/
   
    fig=px.choropleth_mapbox(crime_data,locations='precinct',featureidkey="properties.precinct",geojson=precincts,color='total',color_continuous_scale='ylorrd')
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(mapbox_style="carto-positron", 
                  mapbox_zoom=9.5,
                  mapbox_center={"lat": lat, "lon": long},
                  margin={"r":0,"t":0,"l":0,"b":0},
                  uirevision='constant')
    # returned objects are assigned to the component property of the Output
    return fig, '# '+city

# Run app
if __name__ == '__main__':
    app.run_server(debug=True, port=8054)
