# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:39:53 2022

@author: matsuzaki taisei
"""

data_csv_path = './Data/MyPandas/data.csv'
import pandas as pd
import streamlit as st
import datetime
import japanize_matplotlib
import matplotlib.pyplot as plt

df_excel_schedule = pd.read_excel("python_pandas.xlsx")

def TablePlot(df,outputPath,w,h):
    fig, ax = plt.subplots(figsize=(w,h))
    ax.axis('off')
    ax.table(cellText=df.values,
             colLabels=df.columns,
             loc='center',
             bbox=[0,0,1,1],)
    plt.savefig(outputPath)


print (df_excel_schedule)

priority = st.radio(
    "優先順位",
    ('なし', '高い', '普通','低い', 'やらなくてもいい'))

date = st.date_input(
    "日程を選択してください",
    datetime.date(2022, 12, 1))

stime = st.time_input(
    '開始時間を指定してください',
    datetime.time(1, 00),key=1)

ftime =st.time_input(
    '終了時間を指定してください', 
    datetime.time(1, 00),key=2)

memo = st.selectbox(
    'どんな予定ですか?',
    ('選択してください', '仕事', '旅','アルバイト', '部活動', '学校', '娯楽'))

txt = st.text_area('メモ', '''memo:　''')

confirm = st.selectbox(
    '未確定/確定',
    ('未確定', '確定'))


df1 = pd.DataFrame({'優先順位': [], '日付': [],
                    '開始時刻': [],'終了時刻': [],
                    'メモ': [],'未確定/確定':[]}, index=[])

df2 = pd.DataFrame({'優先順位': [priority], '日付': [date],
                    '開始時刻': [stime],'終了時刻': [ftime],
                    'メモ': [memo+':'+txt] ,'未確定/確定':['確定']}, index=[' '])


df = df1.append(df2)

print(df)

st.table(df)

TablePlot(df,"test2.png",10,10)

with open("test2.png", "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=file,
        file_name="test2.png",
        mime="image/png"
    )













    
    
    
    
    
    
    
    
    
    
    
    
    
    
    