import random
import plotly.express as px
import plotly.figure_factory as ff
index=[]
result= []

for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result.append(dice1+dice2)
    index.append(i)

#fig = px.bar(x=result, y=index)
# fig.show()

fig = ff.create_distplot([result],["Result"])
fig.show()
