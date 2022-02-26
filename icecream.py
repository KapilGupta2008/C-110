import plotly.express as px
import csv
import pandas as pd
import numpy as np

def graph(data_path):
    with open(data_path) as f:
        df = pd.read_csv(f)
        fig = px.scatter(df,x="Temperature", y="Ice-cream Sales")
        fig.show()

def getDataSource(data_path):
    icecream = []
    temperature = []
    with open(data_path) as f:
        new_list = csv.DictReader(f)
        for i in new_list:
            temperature.append(float(i["Temperature"]))
            icecream.append(float(i["Ice-cream Sales"]))

    return {"ice" : icecream, "temp": temperature}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["ice"], datasource["temp"])
    print("Correlation between Temperature vs Ice Cream Sales :- ",correlation[0,1])

def setup():
    file  = "icecream.csv"

    datasource = getDataSource(file)
    findCorrelation(datasource)
    graph(file)

setup()




