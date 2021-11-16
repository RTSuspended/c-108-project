import pandas as pd
import csv
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
AvgRating=df["Avg Rating"].tolist()
#print(AvgRating)
fig=ff.create_distplot([AvgRating],["Avg Rating"],show_hist=True)
fig.show()