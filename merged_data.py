
#import library
import pandas as pd
from datetime import date
from datetime import datetime
import glob
import os


# Some printed values have been put in note notation to prevent
#long compile time. For example printing na values has been 
#put in note notation

#all columns are not displayed use below to see all the columns
#pd.options.display.max_columns=None

#import the .csv filed
august2020=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\august2020_final.csv")
september2020=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\september2020_final.csv")
october2020=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\october2020_final.csv")
november2020=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\november2020_final.csv")
december2020=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\december2020_final.csv")
january2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\january2021_final.csv")
february2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\february2021_final.csv")
march2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\march2021_final.csv")
april2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\april2021_final.csv")
may2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\may2021_final.csv")
june2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\june2021_final.csv")
july2021=pd.read_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\final\\july2021_final.csv")

#merged data frame
merged=pd.concat([august2020,september2020,october2020,november2020,december2020,january2021,february2021,march2021,april2021,may2021,june2021,july2021],ignore_index=True)



#convert the data objects ended_at. started_at to a datetime
merged.started_at=pd.to_datetime(merged["started_at"],format='%m/%d/%Y %H:%M')
merged.ended_at=pd.to_datetime(merged["ended_at"],format='%m/%d/%Y %H:%M')
ride_length2=merged.ended_at-merged.started_at
merged["ride_length"]=ride_length2

#print the dataframe amd counts
#print(merged)
#print(merged.count())
#count and check for na values
#print(merged.isna().sum (axis=0))
#print(merged.isna().any (axis=0))
# count notna
#print(merged.notna().sum (axis=0))
#print(merged.notna().all (axis=0))

 #create a copy of the dataframe merged before getting
 #rid of the na values
merged_v2=merged.copy(deep=True)

#drop na values
merged_v2.dropna(axis =0,how="any",inplace=True)
#print(merged_v2.isna().sum (axis=0))
#print(merged_v2.isna().any (axis=0))

#print values_counts, info, and dataframe to test na drop
#print(merged_v2.value_counts())
#merged_v2.info()
#print(merged_v2)

#make sure there are no spaces in the objects
merged_v2.end_station_name=merged_v2.end_station_name.str.strip()
merged_v2.start_station_name=merged_v2.start_station_name.str.strip()
merged_v2.ride_id=merged_v2.ride_id.str.strip()
merged_v2.rideable_type=merged_v2.rideable_type.str.strip()
merged_v2.member_casual=merged_v2.member_casual.str.strip()


# filter out ride length that is 0 or negative 
#pull the values to look at
mask1=merged_v2.ride_length=="0 days 00:00:00"
test=merged_v2.loc[mask1]
#print(test)
# finalize the drop of the negative or 0 ride length
merged_v2.drop(merged_v2[merged_v2['ride_length'] == "0 days 00:00:00"].index,inplace=True)

# check values after drop the 0s and negatives
#print(merged_v2)
#print(merged_v2.info())
#print(merged_v2.tail())
#print(merged_v2.shape)

# set new columns related to month and time
#makes sorting easier
#day of the week spelled out
week_day=merged_v2.started_at.dt.day_name()
merged_v2["week_day"]=week_day
# month name spelled out 
month_name=merged_v2.started_at.dt.month_name()
merged_v2["month_name"]=month_name
# start time
time_1=merged_v2.started_at.dt.time
merged_v2["time_1"]=time_1
# emd time
time_2=merged_v2.ended_at.dt.time
merged_v2["time_2"]=time_2
#hour of start time 
time_hour=merged_v2.started_at.dt.hour
merged_v2["time_hour"]=time_hour
#hour of end time
time_hour2=merged_v2.ended_at.dt.hour
merged_v2["time_hour2"]=time_hour2
# quarter of the year
quarter=merged_v2.started_at.dt.quarter
merged_v2["quarter"]=quarter
# day of the month
day=merged_v2.started_at.dt.day
merged_v2["day_of_month"]=day
# year value 
year=merged_v2.started_at.dt.year
merged_v2["year"]=year
# test the new columns
#print(merged_v2)

# display season names based on month
merged_v2.loc[merged_v2['month_name']=="June",'season'] ='Summer'
merged_v2.loc[merged_v2['month_name']=="August",'season'] ='Summer'
merged_v2.loc[merged_v2['month_name']=="July",'season'] ='Summer'

merged_v2.loc[merged_v2['month_name']=="September",'season'] ='Fall'
merged_v2.loc[merged_v2['month_name']=="October",'season'] ='Fall'
merged_v2.loc[merged_v2['month_name']=="November",'season'] ='Fall'

merged_v2.loc[merged_v2['month_name']=="December",'season'] ='Winter'
merged_v2.loc[merged_v2['month_name']=="January",'season'] ='Winter'
merged_v2.loc[merged_v2['month_name']=="February",'season'] ='Winter'
merged_v2.loc[merged_v2['month_name']=="March",'season'] ='Winter'

merged_v2.loc[merged_v2['month_name']=="April",'season'] ='Spring'
merged_v2.loc[merged_v2['month_name']=="May",'season'] ='Spring'
merged_v2.loc[merged_v2['month_name']=="June",'season'] ='Spring'



# display time of dat  names based on start time hour
merged_v2.loc[merged_v2['time_hour']==5,'time_of_day'] ='Morning'
merged_v2.loc[merged_v2['time_hour']==6,'time_of_day'] ='Morning'
merged_v2.loc[merged_v2['time_hour']==7,'time_of_day'] ='Morning'
merged_v2.loc[merged_v2['time_hour']==8,'time_of_day'] ='Morning'
merged_v2.loc[merged_v2['time_hour']==9,'time_of_day'] ='Morning'
merged_v2.loc[merged_v2['time_hour']==10,'time_of_day'] ='Morning'
merged_v2.loc[merged_v2['time_hour']==11,'time_of_day'] ='Morning'
merged_v2.loc[merged_v2['time_hour']==12,'time_of_day'] ='Afternoon'
merged_v2.loc[merged_v2['time_hour']==13,'time_of_day'] ='Afternoon'
merged_v2.loc[merged_v2['time_hour']==14,'time_of_day'] ='Afternoon'
merged_v2.loc[merged_v2['time_hour']==15,'time_of_day'] ='Afternoon'
merged_v2.loc[merged_v2['time_hour']==16,'time_of_day'] ='Evening'
merged_v2.loc[merged_v2['time_hour']==17,'time_of_day'] ='Evening'
merged_v2.loc[merged_v2['time_hour']==18,'time_of_day'] ='Evening'
merged_v2.loc[merged_v2['time_hour']==19,'time_of_day'] ='Evening'
merged_v2.loc[merged_v2['time_hour']==20,'time_of_day'] ='Night'
merged_v2.loc[merged_v2['time_hour']==21,'time_of_day'] ='Night'
merged_v2.loc[merged_v2['time_hour']==22,'time_of_day'] ='Night'
merged_v2.loc[merged_v2['time_hour']==23,'time_of_day'] ='Night'
merged_v2.loc[merged_v2['time_hour']==24,'time_of_day'] ='Night'
merged_v2.loc[merged_v2['time_hour']==1,'time_of_day'] ='Night'
merged_v2.loc[merged_v2['time_hour']==2,'time_of_day'] ='Night'
merged_v2.loc[merged_v2['time_hour']==3,'time_of_day'] ='Night'
merged_v2.loc[merged_v2['time_hour']==4,'time_of_day'] ='Night'
merged_v2.loc[merged_v2['time_hour']==0,'time_of_day'] ='Night'
#see all columns
#print(merged_v2.info())

# create copy of data frame before drop unused columns
merged_v3=merged_v2.copy(deep=True)
merged_v3.drop(labels=['start_lat','start_lng','end_lat','end_lng','ride_id','quarter','end_station_id','start_station_id'],axis=1,inplace=True)
#merged_v3.reset_index(inplace=True)


#checked duplicate sum
#print(merged_v3.duplicated(keep = "first").sum)
#print(merged_v3[merged_v3.duplicated(keep = False)])

# detect outliers
print(merged_v3.describe())
outlier_max=merged_v3.ride_length>="1 days 00:27:00"
outlier_min=merged_v3.ride_length<"0 days 00:00:00"
max=merged_v3.loc[outlier_max]

index_drop1= merged_v3[(merged_v3['ride_length']>="1 days 00:00:00")].index
merged_v3.drop(index_drop1,inplace=True)



min=merged_v3.loc[outlier_min]
print(min)


index_drop2= merged_v3[(merged_v3['ride_length']<"0 days 00:00:00")].index
merged_v3.drop(index_drop2,inplace=True)



index_drop3= merged_v3[(merged_v3['time_hour2']<merged_v3.time_hour)].index
merged_v3.drop(index_drop3,inplace=True)

index_drop4= merged_v3[(merged_v3['time_2']<merged_v3.time_1)].index
merged_v3.drop(index_drop4,inplace=True)
merged_v3.reset_index(inplace=True,drop=True)
#merged_v2.reset_index(inplace=True,drop=True)
#merged_v3.reset_index(inplace=True,drop=True)



#print the final output
print(merged_v3)
print(merged_v3.info())
print(merged_v3.describe())



# below is the code to import results to a excel file

#merged_v3.to_csv("C:\\Users\\Jesse\\Desktop\\google_data_project\\tables_join\\merged_join2.csv",index=False)

# beginning the amalysis 

print(merged_v3.agg({"ride_length":"mean"}))
print(merged_v3.agg({"ride_length":"max"}))
print(merged_v3.agg({"ride_length":"min"}))
print(merged_v3.week_day.value_counts())
print(merged_v3.member_casual.value_counts())
print(merged_v3.time_hour.value_counts())
print(merged_v3.time_of_day.value_counts())
print(merged_v3.day_of_month.value_counts())
print(merged_v3.season.value_counts())
print(merged_v3.year.value_counts())
print(merged_v3.rideable_type.value_counts())