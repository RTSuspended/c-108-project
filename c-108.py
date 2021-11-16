import pandas as pd
import csv
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
MobileBrand=df["Mobile Brand"].tolist()
#print(MobileBrand)
fig=ff.create_distplot([MobileBrand],["Mobile Brand"],show_hist=False)
fig.show()