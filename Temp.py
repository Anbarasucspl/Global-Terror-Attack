import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
class globalterror:
    def bargraphplot(self,data,xval,yval,xlabel,ylabel,titlex):
        plt.figure(figsize=(15, 7))
        sns.barplot(x=data[xval].values,y=data[yval].values)
        plt.xticks(rotation=90)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(titlex)
        plt.savefig("D:\\Python\\gtd\\" + titlex + '.png', dpi=fig.dpi)
global_terr_data=pd.read_csv('D:\Python\gtd\globalterrorism.csv')
obj_globalterror=globalterror()
Terror_group_globally=global_terr_data.groupby(['gname'])
Terror_group_event=Terror_group_globally['eventid'].count().reset_index().sort_values(by='eventid',ascending=False)[0:input("Enter max number of terror groups on chart :")]
layout = go.Layout(barmode='stack', title='Number of Attacks for the Top 40 Groups By Attack from 1970 - 2017',
                  yaxis={'title':'Number of Attacks'})
fig = go.Figure(data=Terror_group_event, layout=layout)
print(Terror_group_event)
