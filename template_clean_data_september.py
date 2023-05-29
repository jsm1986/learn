
#import library
import pandas as pd
from datetime import date
from datetime import datetime
import glob
import os

pd.options.display.max_rows=50
pd.options.display.min_rows=50


# Some printed values have been put in note notation to prevent
#long compile time. For example printing na values has been 
#put in note notation

#all columns are not displayed use below to see all the columns
#pd.options.display.max_columns=None

#import the .csv filed
august2020=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\august2020_final.csv")
#september2020=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\september2020_final.csv")
#october2020=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\october2020_final.csv")
#november2020=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\november2020_final.csv")
#december2020=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\december2020_final.csv")
#january2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\january2021_final.csv")
#february2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\february2021_final.csv")
#march2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\march2021_final.csv")
#april2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\april2021_final.csv")
#may2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\may2021_final.csv")
#june2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\june2021_final.csv")
#july2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\july2021_final.csv")

#merged=pd.concat([august2020,september2020,october2020,november2020,december2020,january2021,february2021,march2021,april2021,may2021,june2021,july2021],ignore_index=True)



#convert the data objects ended_at. started_at to a datetime
august2020.started_at=pd.to_datetime(august2020["started_at"],format='%m/%d/%Y %H:%M')
august2020.ended_at=pd.to_datetime(august2020["ended_at"],format='%m/%d/%Y %H:%M')
ride_length2=august2020.ended_at-august2020.started_at
august2020["ride_length"]=ride_length2

#print the dataframe amd counts
#print(august2020)
#print(august2020.count())
#count and check for na values
#print(august2020.isna().sum (axis=0))
#print(august2020.isna().any (axis=0))
# count notna
#print(august2020.notna().sum (axis=0))
#print(august2020.notna().all (axis=0))

 #create a copy of the dataframe august2020 before getting
 #rid of the na values
august2020_v2=august2020.copy(deep=True)

#drop na values
august2020_v2.dropna(axis =0,how="any",inplace=True)
#print(august2020_v2.isna().sum (axis=0))
#print(august2020_v2.isna().any (axis=0))

#print values_counts, info, and dataframe to test na drop
#print(august2020_v2.value_counts())
#august2020_v2.info()
#print(august2020_v2)

#make sure there are no spaces in the objects
august2020_v2.end_station_name=august2020_v2.end_station_name.str.strip()
august2020_v2.start_station_name=august2020_v2.start_station_name.str.strip()
august2020_v2.ride_id=august2020_v2.ride_id.str.strip()
august2020_v2.rideable_type=august2020_v2.rideable_type.str.strip()
august2020_v2.member_casual=august2020_v2.member_casual.str.strip()


# filter out ride length that is 0 or negative 
#pull the values to look at
mask1=august2020_v2.ride_length=="0 days 00:00:00"
test=august2020_v2.loc[mask1]
#print(test)
# finalize the drop of the negative or 0 ride length
august2020_v2.drop(august2020_v2[august2020_v2['ride_length'] == "0 days 00:00:00"].index,inplace=True)

# check values after drop the 0s and negatives
#print(august2020_v2)
#print(august2020_v2.info())
#print(august2020_v2.tail())
#print(august2020_v2.shape)

# set new columns related to month and time
#makes sorting easier
#day of the week spelled out
week_day=august2020_v2.started_at.dt.day_name()
august2020_v2["week_day"]=week_day
# month name spelled out 
month_name=august2020_v2.started_at.dt.month_name()
august2020_v2["month_name"]=month_name
# start time
time_1=august2020_v2.started_at.dt.time
august2020_v2["time_1"]=time_1
# emd time
time_2=august2020_v2.ended_at.dt.time
august2020_v2["time_2"]=time_2
#hour of start time 
time_hour=august2020_v2.started_at.dt.hour
august2020_v2["time_hour"]=time_hour
#hour of end time
time_hour2=august2020_v2.ended_at.dt.hour
august2020_v2["time_hour2"]=time_hour2
# quarter of the year
quarter=august2020_v2.started_at.dt.quarter
august2020_v2["quarter"]=quarter
# day of the month
day=august2020_v2.started_at.dt.day
august2020_v2["day_of_month"]=day
# year value 
year=august2020_v2.started_at.dt.year
august2020_v2["year"]=year
# test the new columns
#print(august2020_v2)

# display season names based on month
august2020_v2.loc[august2020_v2['month_name']=="June",'season'] ='Summer'
august2020_v2.loc[august2020_v2['month_name']=="August",'season'] ='Summer'
august2020_v2.loc[august2020_v2['month_name']=="July",'season'] ='Summer'

august2020_v2.loc[august2020_v2['month_name']=="September",'season'] ='Fall'
august2020_v2.loc[august2020_v2['month_name']=="October",'season'] ='Fall'
august2020_v2.loc[august2020_v2['month_name']=="November",'season'] ='Fall'

august2020_v2.loc[august2020_v2['month_name']=="December",'season'] ='Winter'
august2020_v2.loc[august2020_v2['month_name']=="January",'season'] ='Winter'
august2020_v2.loc[august2020_v2['month_name']=="February",'season'] ='Winter'
august2020_v2.loc[august2020_v2['month_name']=="March",'season'] ='Winter'

august2020_v2.loc[august2020_v2['month_name']=="April",'season'] ='Spring'
august2020_v2.loc[august2020_v2['month_name']=="May",'season'] ='Spring'
august2020_v2.loc[august2020_v2['month_name']=="June",'season'] ='Spring'



# display time of dat  names based on start time hour
august2020_v2.loc[august2020_v2['time_hour']==5,'time_of_day'] ='Morning'
august2020_v2.loc[august2020_v2['time_hour']==6,'time_of_day'] ='Morning'
august2020_v2.loc[august2020_v2['time_hour']==7,'time_of_day'] ='Morning'
august2020_v2.loc[august2020_v2['time_hour']==8,'time_of_day'] ='Morning'
august2020_v2.loc[august2020_v2['time_hour']==9,'time_of_day'] ='Morning'
august2020_v2.loc[august2020_v2['time_hour']==10,'time_of_day'] ='Morning'
august2020_v2.loc[august2020_v2['time_hour']==11,'time_of_day'] ='Morning'
august2020_v2.loc[august2020_v2['time_hour']==12,'time_of_day'] ='Afternoon'
august2020_v2.loc[august2020_v2['time_hour']==13,'time_of_day'] ='Afternoon'
august2020_v2.loc[august2020_v2['time_hour']==14,'time_of_day'] ='Afternoon'
august2020_v2.loc[august2020_v2['time_hour']==15,'time_of_day'] ='Afternoon'
august2020_v2.loc[august2020_v2['time_hour']==16,'time_of_day'] ='Evening'
august2020_v2.loc[august2020_v2['time_hour']==17,'time_of_day'] ='Evening'
august2020_v2.loc[august2020_v2['time_hour']==18,'time_of_day'] ='Evening'
august2020_v2.loc[august2020_v2['time_hour']==19,'time_of_day'] ='Evening'
august2020_v2.loc[august2020_v2['time_hour']==20,'time_of_day'] ='Night'
august2020_v2.loc[august2020_v2['time_hour']==21,'time_of_day'] ='Night'
august2020_v2.loc[august2020_v2['time_hour']==22,'time_of_day'] ='Night'
august2020_v2.loc[august2020_v2['time_hour']==23,'time_of_day'] ='Night'
august2020_v2.loc[august2020_v2['time_hour']==24,'time_of_day'] ='Night'
august2020_v2.loc[august2020_v2['time_hour']==1,'time_of_day'] ='Night'
august2020_v2.loc[august2020_v2['time_hour']==2,'time_of_day'] ='Night'
august2020_v2.loc[august2020_v2['time_hour']==3,'time_of_day'] ='Night'
august2020_v2.loc[august2020_v2['time_hour']==4,'time_of_day'] ='Night'
august2020_v2.loc[august2020_v2['time_hour']==0,'time_of_day'] ='Night'
#see all columns
#print(august2020_v2.info())

# create copy of data frame before drop unused columns
august2020_v3=august2020_v2.copy(deep=True)
august2020_v3.drop(labels=['start_lat','start_lng','end_lat','end_lng','ride_id','quarter','end_station_id','start_station_id'],axis=1,inplace=True)


# dulicate  detection
#print(august2020_v3.duplicated(keep = "first"))
#print(august2020_v3.duplicated(keep = "first").sum)
#print(august2020_v3[august2020_v3.duplicated(keep = False)])

# detect outliers
#print(august2020_v3.describe())
outlier_max=august2020_v3.ride_length>="1 days 00:27:00"
outlier_min=august2020_v3.ride_length<"0 days 00:00:00"
max=august2020_v3.loc[outlier_max]
min=august2020_v3.loc[outlier_min]

index_drop1= august2020_v3[(august2020_v3['ride_length']>="1 days 00:00:00")].index
august2020_v3.drop(index_drop1,inplace=True)

index_drop2= august2020_v3[(august2020_v3['ride_length']<"0 days 00:00:00")].index
august2020_v3.drop(index_drop2,inplace=True)


index_drop3= august2020_v3[(august2020_v3['time_hour2']<august2020_v3.time_hour)].index
august2020_v3.drop(index_drop3,inplace=True)

index_drop4= august2020_v3[(august2020_v3['time_2']<august2020_v3.time_1)].index
august2020_v3.drop(index_drop4,inplace=True)


min=august2020_v3.loc[outlier_min]
#print(min)

#reset index
august2020_v3.reset_index(inplace=True,drop=True)



#print the final output
#print(august2020_v3.iloc[10:60])
#print(august2020_v3.info())
#print(august2020_v3.describe())
#print(august2020_v3.info())


# below is the code to import results to a excel file

#august2020_v3.to_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\tables_join\\december2020.csv",index=False)
#time_test= august2020_v3[(august2020_v3['started_at']=="8/12/20 11:56")]
#print(time_test)

# beginning the amalysis on large scale

#print(august2020_v3.agg({"ride_length":"mean"}))
#print(august2020_v3.agg({"ride_length":"max"}))
#print(august2020_v3.agg({"ride_length":"min"}))
#print(august2020_v3.week_day.value_counts())
#print(august2020_v3.member_casual.value_counts())
#print(august2020_v3.time_hour.value_counts())
#print(august2020_v3.time_of_day.value_counts())
#print(august2020_v3.day_of_month.value_counts())
#print(august2020_v3.season.value_counts())
#print(august2020_v3.year.value_counts())
#print(august2020_v3.rideable_type.value_counts())

# starting to split analysis into indiviual groups
august2020_v3.groupby("member_casual")
gbo=august2020_v3.groupby("member_casual")
gbo.groups

grouped_multiple = august2020_v3.groupby(['member_casual','week_day']).agg({'ride_length':['mean']})
grouped_multiple2 = august2020_v3.groupby(['member_casual','rideable_type']).agg({'ride_length':['mean']})
grouped_multiple3 = august2020_v3.groupby(['member_casual','time_of_day']).agg({'ride_length':['mean']})
grouped_multiple4 = august2020_v3.groupby(['member_casual','day_of_month']).agg({'ride_length':['mean']})
grouped_multiple5 = august2020_v3.groupby(['member_casual','season']).agg({'ride_length':['mean']})
grouped_multiple6 = august2020_v3.groupby(['member_casual','month_name']).agg({'ride_length':['mean']})
grouped_multiple7 = august2020_v3.groupby(['member_casual','time_hour']).agg({'ride_length':['mean']})
grouped_multiple8 = august2020_v3.groupby(['member_casual']).agg({'ride_length':['mean']})

#grouped_multiple =grouped_multiple.reset_index(drop=True)
print(grouped_multiple)
print(grouped_multiple2)
print(grouped_multiple3)
print(grouped_multiple4)
print(grouped_multiple5)
print(grouped_multiple6)
print(grouped_multiple7)
print(grouped_multiple8)
print(august2020_v3.agg({"ride_length":"mean"}))



grouped_count= august2020_v3.groupby(['member_casual','rideable_type']).agg({'ride_length':['count']})
grouped_count2= august2020_v3.groupby(['time_hour','rideable_type','member_casual']).agg({'ride_length':['count']})
print(grouped_count)
print(grouped_count2)

print(august2020_v3.agg({"ride_length":"mean"}))