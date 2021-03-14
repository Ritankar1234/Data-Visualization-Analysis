import pandas as pd 
import csv
df=pd.read_csv("TestData.csv")
import plotly.graph_objects as go 
studentDf=df.loc[df["student_id"]=="TRL_xsl"]
mean=studentDf.groupby("level")["attempt"].mean()
fig=go.Figure(go.Bar(x=mean, y=["level 1", "level 2", "level 3", "level 4"], orientation="h"))
print(mean)
fig.show()