# -*- coding: utf-8 -*-
"""preprocessforex.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sn8sqwNdbKaL92KTPeFR1zBg4C9BwVHz
"""

import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/Modified_Multi_DQN/main/datasets/daxHour.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/Modified_Multi_DQN/main/datasets/daxDay.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/Modified_Multi_DQN/main/datasets/daxWeek.csv')
# df4 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/Modified_Multi_DQN/main/datasets/sp500Hour.csv')
# df5 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/Modified_Multi_DQN/main/datasets/sp500Day.csv')
# df6 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/Modified_Multi_DQN/main/datasets/sp500Week.csv')
# dfcomb  = pd.concat([df1,df2,df3,df4,df5], axis=0)
# dfcomb.drop(dfcomb.columns[5], axis=1, inplace=True)
print(df1)
# dfcomb.columns=['Date','Open','High','Low','Close','todrop']

#df2 = pd.read_csv('daxDay.csv')

# df1 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/HourEURUSD2017.csv')
# df2 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/HourEURUSD2018.csv')
# df3 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/HourEURUSD2019.csv')
# df4 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/HourEURUSD2020.csv')
# df5 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/HourEURUSD2021.csv')

# dfcomb  = pd.concat([df1,df2,df3,df4,df5], axis=0)
# dfcomb.drop(dfcomb.columns[5], axis=1, inplace=True)
# print(dfcomb)


# df6 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/DayEURUSD2017.csv')
# df7 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/DayEURUSD2018.csv')
# df8 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/DayEURUSD2019.csv')
# df9 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/DayEURUSD2020.csv')
# df10 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/DayEURUSD2021.csv')

# dfcomb2  = pd.concat([df6,df7,df8,df9,df10], axis=0)
# dfcomb2.drop(dfcomb2.columns[5], axis=1, inplace=True)
# print(dfcomb2)

# df11 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/WeekEURUSD2017.csv')
# df12 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/WeekEURUSD2018.csv')
# df13 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/WeekEURUSD2019.csv')
# df14 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/WeekEURUSD2020.csv')
# df15 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/WeekEURUSD2021.csv')

# dfcomb3  = pd.concat([df11,df12,df13,df14,df15], axis=0)
# dfcomb3.drop(dfcomb3.columns[5], axis=1, inplace=True)
# print(dfcomb3)

# dfcomb["Date"] = pd.to_datetime(dfcomb["Date"])
# dfcomb = dfcomb.set_index('Date')
# dfcomb.index

# dfcomb = dfcomb.drop_duplicates()

# df0 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/MinuteEURUSD2016.csv',sep=',',names=colnames)
# df0.drop(df0.columns[5], axis=1, inplace=True)
# df0["Date"] = pd.to_datetime(df0["Date"])
# df0 = df0.set_index('Date')
# df0 = df0.drop_duplicates()
# df0.index

# dfcomb  = pd.concat([df0,dfcomb], axis=0)
# dfcomb

# df_hour = dfcomb.asfreq('H', method = 'ffill')
# df_hour.head()
# df_hour.to_csv('/content/drive/MyDrive/Forex_Data/EURUSD_2021/Hour.csv')

# df_day = dfcomb.asfreq('D', method = 'ffill')
# df_day.head()
# df_day.to_csv('/content/drive/MyDrive/Forex_Data/EURUSD_2021/Day.csv')

# df_week = dfcomb.asfreq('W', method = 'ffill')
# df_week.head()
# df_week.to_csv('/content/drive/MyDrive/Forex_Data/EURUSD_2021/Week.csv')

# def fun(dffun):  
#   Date=[]
#   Time=[]
#   for dt in dffun.index:
#     dt=str(dt)
#     d=dt[5:7]+'/'+dt[8:10]+'/'+dt[0:4]
#     t=dt[11:16]
#     Date.append(d)
#     Time.append(t)
#   #dfcomb.drop(dfcomb.columns[0], axis=1, inplace=True)
#   dffun.insert(0, "Date",Date, True)
#   dffun.insert(1, "Time",Time, True)
#   dffun=dffun.reset_index(drop=True)
#   return dffun
# Date=[]
# Time=[]
# for dt in dfcomb2.iloc[:,0]:
#   dt=str(dt)
#   d=dt[4:6]+'/'+dt[6:8]+'/'+dt[0:4]
#   t=dt[9:11]+':'+dt[11:13]
#   Date.append(d)
#   Time.append(t)
# dfcomb2.drop(dfcomb2.columns[0], axis=1, inplace=True)
# dfcomb2.insert(0, "Date",Date, True)
# dfcomb2.insert(1, "Time",Time, True)
# print(dfcomb2)

# Date=[]
# Time=[]
# for dt in dfcomb3.iloc[:,0]:
#   dt=str(dt)
#   d=dt[4:6]+'/'+dt[6:8]+'/'+dt[0:4]
#   t=dt[9:11]+':'+dt[11:13]
#   Date.append(d)
#   Time.append(t)
# dfcomb3.drop(dfcomb3.columns[0], axis=1, inplace=True)
# dfcomb3.insert(0, "Date",Date, True)
# dfcomb3.insert(1, "Time",Time, True)
# print(dfcomb3)
# df_hour=fun(df_hour)
# df_day=fun(df_day)
# df_week=fun(df_week)

# volume1=[0]*len(df_hour)
# volume2=[0]*len(df_day)
# volume3=[0]*len(df_week)
# print(len(df_day))
# df_hour.insert(6, "Volume",volume1, True)
# df_day.insert(6, "Volume",volume2, True)
# df_week.insert(6, "Volume",volume3, True)
# df_hour.to_csv("sp500Hour.csv",index=False)
# df_day.to_csv("sp500Day.csv",index=False)
# df_week.to_csv("sp500Week.csv",index=False)
# print(df_hour)
# print(df_week)

ma = list()
ema = list()
ma2 = list()
ema2 = list()
ma3 = list()
ema3 = list()

highval = df1['High'].values
highval2 = df2['High'].values
highval3 = df3['High'].values

sum = 0
for i in range(len(highval)):
  sum = sum + highval[i]
  ma.append(sum/(i+1))

dfma = pd.DataFrame(ma,columns=['ma'])
dfma.reset_index(inplace=True, drop=True)
df1.reset_index(inplace=True, drop=True) 
df1 = pd.concat([df1,dfma],axis=1)


sum2 = 0
for i in range(len(highval2)):
  sum2 = sum2 + highval2[i]
  ma2.append(sum2/(i+1))

dfma2 = pd.DataFrame(ma2,columns=['ma'])
dfma2.reset_index(inplace=True, drop=True)
df2.reset_index(inplace=True, drop=True)  
df2 = pd.concat([df2,dfma2],axis=1)

sum3 = 0
for i in range(len(highval3)):
  sum3 = sum3 + highval3[i]
  ma3.append(sum3/(i+1))

dfma3 = pd.DataFrame(ma3,columns=['ma'])
dfma3.reset_index(inplace=True, drop=True)
df3.reset_index(inplace=True, drop=True) 
df3 = pd.concat([df3,dfma3],axis=1)

for i in range(len(highval)):
  if(i == 0):
    ema.append(highval[i])
  ema.append((highval[i]*(2/(2+i))) + (ema[i-1]*(1-((2/(2+i))))))

dfema = pd.DataFrame(ema,columns=['ema'])
dfema.reset_index(inplace=True, drop=True)
df1.reset_index(inplace=True, drop=True) 
df1 = pd.concat([df1,dfema],axis=1)

for i in range(len(highval2)):
  if(i == 0):
    ema2.append(highval2[i])
  ema2.append((highval2[i]*(2/(2+i))) + (ema2[i-1]*(1-((2/(2+i))))))

dfema2 = pd.DataFrame(ema2,columns=['ema'])
dfema2.reset_index(inplace=True, drop=True)
df2.reset_index(inplace=True, drop=True) 
df2 = pd.concat([df2,dfema2],axis=1)

for i in range(len(highval3)):
  if(i == 0):
    ema3.append(highval3[i])
  ema3.append((highval3[i]*(2/(2+i))) + (ema3[i-1]*(1-((2/(2+i))))))


dfema3 = pd.DataFrame(ema3,columns=['ema'])
dfema3.reset_index(inplace=True, drop=True)
df3.reset_index(inplace=True, drop=True) 
df3 = pd.concat([df3,dfema3],axis=1)

# df0 = pd.read_csv('https://raw.githubusercontent.com/Sankalp2002/IML_datasets/main/MinuteEURUSD2016.csv',sep=',',names=colnames)
# df0.drop(df0.columns[5], axis=1, inplace=True)
# Date=[]
# Time=[]
# for dt in df0.iloc[:,0]:
#   dt=str(dt)
#   d=dt[5:7]+'/'+dt[8:10]+'/'+dt[0:4]
#   t=dt[11:16]
#   Date.append(d)
#   Time.append(t)
# df0.drop(dfcomb.columns[0], axis=1, inplace=True)
# df0.insert(0, "Date",Date, True)
# df0.insert(1, "Time",Time, True)
# dfcomb  = pd.concat([df0,dfcomb], axis=0)
# dfcomb

# dfcomb = dfcomb.iloc[:-1 , :]
# dfcomb.set_index('Date')
# dfcomb.to_csv("daxMinute.csv")

df1 = df1.iloc[:-1 , :]
df1.set_index('Date')
print(df1)
df1.to_csv("daxHour.csv",index=False)

df2 = df2.iloc[:-1 , :]
df2.set_index('Date')
print(df2)
df2.to_csv("daxDay.csv",index=False)

df3 = df3.iloc[:-1 , :]
df3.set_index('Date')
print(df3)
df3.to_csv("daxWeek.csv",index=False)
