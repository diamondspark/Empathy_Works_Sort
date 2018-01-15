import pandas as pd


def sort(col_name):
     return df.sort_values(col_name)

##df = pd.read_csv('./data/report.csv',encoding='utf-16')
df = pd.read_excel('/home/ubuntu/flaskapp/data/report.xlsx')
new_col_list= ['short','quiz','Phase_1','Phase_2','date','time',
             'user','email','age','gender','marital_status','sexual_orientation',
               'professional_designation','years_in_practice','emq','redo','%_difference','Unnamed']
df.columns= new_col_list
