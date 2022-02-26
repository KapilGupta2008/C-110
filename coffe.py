import pandas as pd
import plotly.express as px 
import csv 
import numpy as np





df = pd.read_csv("coffe.csv")
fig=px.scatter(df, x="Coffee in ml", y="sleep in hours")
fig.show()


