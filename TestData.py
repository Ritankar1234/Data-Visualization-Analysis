import pandas as pd 
import csv
df=pd.read_csv("TestData.csv")
mean=df.groupby("level")["attempt"].mean()
import plotly.graph_objects as go 
fig=go.Figure(go.Bar(x=mean, y=["level 1","level 2","level 3","level 4"], orientation="h"))
fig.show()
print(mean)

