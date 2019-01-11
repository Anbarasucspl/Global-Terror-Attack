import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class globalterror:
    def last10yrvictim(self,data,country,xval,yval):
        plt.figure(figsize=(15,7))
        country_name=data['country_txt'].unique()
        sns.barplot(x=data[xval].values,y=data[yval].values)
        plt.xticks(rotation=90)
        plt.xlabel('Year')
        plt.ylabel('Total No of Victims')
        plt.title('Terror victim Chart : ' + country_name)
        plt.show()
global_terr_data=pd.read_csv('D:\Python\gtd\globalterrorism.csv')
Terror_plot_year_wise=global_terr_data.groupby(['country_txt','iyear']).sum()
country_10yrvictim=[input('Enter the country name for details:')]
Country_wise_nkill=Terror_plot_year_wise['nkill'].reset_index().rename({'nkill':'Total_kills'},axis='columns')
Country_nkill=Country_wise_nkill[Country_wise_nkill['country_txt'].isin(country_10yrvictim)].sort_values(by='iyear',ascending=False)[:input('Enter number of years details you want to view(max47):')]
obj_globalterror=globalterror()
obj_globalterror.last10yrvictim(Country_nkill,country_10yrvictim,'iyear','Total_kills')
Terror_attack_type_wise=global_terr_data.groupby(['country_txt','attacktype1_txt']).count()
attact_type_count=Terror_attack_type_wise['iyear'].reset_index()
attack_type=attact_type_count[attact_type_count['country_txt'].isin(country_10yrvictim)]
obj_globalterror.last10yrvictim(attack_type,country_10yrvictim,'attacktype1_txt','iyear')
