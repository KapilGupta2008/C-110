import pandas as pd
import plotly.express as px 
import csv 






df = pd.read_csv("t.v.csv")
fig=px.scatter(df, x="Size of TV", y="Average time spent watching TV in a week")
fig.show()


