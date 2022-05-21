
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output

df = pd.read_csv("./lab3-datasets/black-friday/BlackFriday.csv",encoding = 'ISO-8859-1')

app = Dash(__name__)

#年龄分布
male=df[df.Gender=="M"]
female=df[df.Gender=="F"]
age_range = np.sort(df["Age"].unique())

age_distribution=pd.DataFrame({
    "Gender":["M"]*len(age_range)+["F"]*len(age_range),
    "AgeRange":age_range.tolist()*2,
    "AgeCount":[male[male.Age==item].shape[0] for item in age_range]+[female[female.Age==item].shape[0] for item in age_range]
})
# print(age_distribution)
age_distribution_chart=px.bar(age_distribution,x="AgeRange",y="AgeCount",color="Gender",barmode="group",title="Gender Distribution with Age")

app.layout = html.Div(children=[
    html.Div(children=["Black Friday"],style={"fontSize":"45px"}),
    html.Div(children=[
        dcc.Graph(id="age_distribution_chart", figure=age_distribution_chart),
        html.Div(children=[
            dcc.Graph(id="occupation_with_age_chart"),
            dcc.Graph(id="purchase_with_age_city_chart")
            ],style={"display":"flex","flexDirection":"column"})
        ],style={"display":"flex"}),
    ],style={"display":"flex","flexDirection":"column","alignItems":"center"})

@app.callback(
    Output("occupation_with_age_chart","figure"),
    Input("age_distribution_chart","hoverData")
)
def occupy_with_age(hoverDataAge):
    #各个年龄的职业分布
    occupations = np.sort(df["Occupation"].unique())
    
    try:
        cur_age=hoverDataAge["points"][0]["x"]
    except:
        cur_age="0-17"
        
    occupation_with_age=pd.DataFrame({
        "Occupations":occupations,
        "OccupationCount":[df[(df.Age==cur_age)&(df.Occupation==item)].shape[0] for item in occupations]
    })
    occupation_with_age_chart = px.pie(occupation_with_age,values="OccupationCount",names="Occupations",title="Occupation with Age")
    return occupation_with_age_chart

@app.callback(
    Output("purchase_with_age_city_chart","figure"),
    Input("age_distribution_chart","hoverData")
)
def purchase_with_gender_marital_city(hoverDataAge):
    try:
        cur_age=hoverDataAge["points"][0]["x"]
    except:
        cur_age="0-17"

    purchase_with_age_city_distribution = df[df.Age==cur_age]
    #print(purchase_with_age_city_distribution)
    age_distribution_chart = px.sunburst(purchase_with_age_city_distribution,path=["Gender","Marital_Status","City_Category"],values="Purchase",title="Purchase with Gender Marital City")

    return age_distribution_chart


if __name__ == "__main__":
    app.run_server(debug=True)
    pass
