import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class globalterror:
    def bargraphplot(self,data,xval,yval,xlabel,ylabel):
        plt.figure(figsize=(15, 7))
        sns.barplot(x=data[xval].values,y=data[yval].values)
        plt.xticks(rotation=90)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title('Terror victim Chart')
        plt.show()
    def linegraphplot(self,datafrm,index_val):
        datafrm.set_index(index_val).plot(marker='o')
        plt.gcf().set_size_inches((15,7),forward=True)
        
        
global_terr_data=pd.read_csv('D:\Python\gtd\globalterrorism.csv')
obj_globalterror=globalterror()
Interested_country=[input('Enter the country name for details:')]
Terror_plot_year_wise=global_terr_data.groupby(['country_txt','iyear']).sum()
Terror_kills_global=Terror_plot_year_wise['nkill'].reset_index()
Terror_cnt_slct_conty=Terror_kills_global[Terror_kills_global['country_txt'].isin(Interested_country)].reset_index()
Terror_count_India=Terror_cnt_slct_conty[['iyear','nkill']]
obj_globalterror.linegraphplot(Terror_count_India,'iyear')
Terror_plot_global_year_wise=global_terr_data.groupby(['iyear']).sum()
Terror_kill_global=Terror_plot_global_year_wise['nkill'].reset_index()
Terror_count_global=Terror_kill_global[['iyear','nkill']]
obj_globalterror.linegraphplot(Terror_count_global,'iyear')
Terror_attack_type_wise=global_terr_data.groupby(['country_txt','attacktype1_txt']).count()
attact_type_count=Terror_attack_type_wise['iyear'].reset_index().rename({'iyear':'Total_count'}, axis='columns')
attack_type_slct_cnty=attact_type_count[attact_type_count['country_txt'].isin(Interested_country)]
obj_globalterror.bargraphplot(attack_type_slct_cnty,'attacktype1_txt','Total_count','Types of attack','victim numbers')
attack_type_cnt_global=attact_type_count.groupby(['attacktype1_txt']).sum().reset_index()
obj_globalterror.bargraphplot(attack_type_cnt_global,'attacktype1_txt','Total_count','Types of attack','victim numbers')
