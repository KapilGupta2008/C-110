import csv
import plotly.express as px
import pandas as pd
import pandas as pd

with open("class3.csv", newline='') as f:
    reader = csv.reader(f)
    file_data= list(reader)


file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    a= file_data[i][1]
    new_data.append(int(a))


sum=0
n=len(new_data)

for j in new_data:
    sum = sum+j
mean =sum/n



print(" mean is: "+ str(mean))



df = pd.read_csv("class3.csv")
fig = px.scatter(df, x="Roll No", y="Marks In Percentage")
fig.update_layout(shapes=[dict(
    type='line',
    y0= mean , y1=mean,
    x0=0, x1=n

)])
fig.update_yaxes(rangemode = "tozero")
fig.show()