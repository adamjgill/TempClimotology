"""
Program written to be able to look at the temperature trends on the summit
using matplotlib.

The goal is to use a joyplot to see if there has been a shift in the temperature.
"""

import pandas as pd
import matplotlib.pyplot as plt

#reading in the CSV file in order to be able to start to use it and modifiy it though the program
init_df = pd.read_csv("b16_hourly_temp.csv") #init_df is for the initial dataframe

#Drop any NULL values from Dataframe
init_df.dropna()

init_df['date'] = pd.to_datetime(init_df['date']) #converting the date time row into a date time string

#Splitting the Dataframe into individual dataframes by month
JanuaryAll  = init_df[init_df['date'].dt.month == 1]
FebruaryAll = init_df[init_df['date'].dt.month == 2]
MarchAll    = init_df[init_df['date'].dt.month == 3]
AprilAll    = init_df[init_df['date'].dt.month == 4]
MayAll      = init_df[init_df['date'].dt.month == 5]
JuneAll     = init_df[init_df['date'].dt.month == 6]
JulyAll     = init_df[init_df['date'].dt.month == 7]
AugustAll   = init_df[init_df['date'].dt.month == 8]
SeptemberAll= init_df[init_df['date'].dt.month == 9]
OctoberAll  = init_df[init_df['date'].dt.month == 10]
NovemberAll = init_df[init_df['date'].dt.month == 11]
DecemberAll = init_df[init_df['date'].dt.month == 12]

#Create def in order to count the number of instances in a dataset
def count_values(dataframe):
    filtered = dataframe['temperature'].value_counts().sort_index()
    return filtered

#filtering the data
JanTemps = count_values(JanuaryAll)
FebTemps = count_values(FebruaryAll)
MarTemps = count_values(MarchAll)
AprTemps = count_values(AprilAll)
MayTemps = count_values(MayAll)
JunTemps = count_values(JuneAll)
JulTemps = count_values(JulyAll)
AugTemps = count_values(AugustAll)
SepTemps = count_values(SeptemberAll)
OctTemps = count_values(OctoberAll)
NovTemps = count_values(NovemberAll)
DecTemps = count_values(DecemberAll)

a = 1.0 #alpha so I dont have to type it all the time

#The plot
#f, (ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12) = plt.subplots(12,sharex=True,sharey=True)
f, (ax1,ax7) = plt.subplots(2,sharex=True,sharey=True)
ax1.fill_between(JanTemps.index, JanTemps, color='#ff0000', alpha=a, label="January")
ax1.set_title("Temperature Distrubution of Hourly Obs since 1935 in Each Month")
ax1.axvline(x=32, color='black', alpha=a)
ax1.axvline(x=0, color='black', alpha=a)
ax1.legend()
"""ax2.fill_between(FebTemps.index, FebTemps, color='#ff5400', alpha=a, label="February")
ax2.axvline(x=32, color='black', alpha=a)
ax2.axvline(x=0, color='black', alpha=a)
ax2.legend()
ax3.fill_between(MarTemps.index, MarTemps, color='#ff9000', alpha=a, label="March")
ax3.axvline(x=32, color='black', alpha=a)
ax3.axvline(x=0, color='black', alpha=a)
ax3.legend()
ax4.fill_between(AprTemps.index, AprTemps, color='#ffc700', alpha=a, label="April")
ax4.axvline(x=32, color='black', alpha=a)
ax4.axvline(x=0, color='black', alpha=a)
ax4.legend()
ax5.fill_between(MayTemps.index, MayTemps, color='#fffa00', alpha=a, label="May")
ax5.axvline(x=32, color='black', alpha=a)
ax5.axvline(x=0, color='black', alpha=a)
ax5.legend()
ax6.fill_between(JunTemps.index, JunTemps, color='#bfff00', alpha=a, label="June")
ax6.axvline(x=32, color='black', alpha=a)
ax6.axvline(x=0, color='black', alpha=a)
ax6.legend()"""
ax7.fill_between(JulTemps.index, JulTemps, color='#7fff00', alpha=a, label="July")
ax7.axvline(x=32, color='black', alpha=a)
ax7.axvline(x=0, color='black', alpha=a)
ax7.legend()
"""ax8.fill_between(AugTemps.index, AugTemps, color='#32ff00', alpha=a, label="August")
ax8.axvline(x=32, color='black', alpha=a)
ax8.axvline(x=0, color='black', alpha=a)
ax8.legend()
ax9.fill_between(SepTemps.index, SepTemps, color='#00ff50', alpha=a, label="September")
ax9.axvline(x=32, color='black', alpha=a)
ax9.axvline(x=0, color='black', alpha=a)
ax9.legend()
ax10.fill_between(OctTemps.index, OctTemps, color='#00ffbb', alpha=a, label="October")
ax10.axvline(x=32, color='black', alpha=a)
ax10.axvline(x=0, color='black', alpha=a)
ax10.legend()
ax11.fill_between(NovTemps.index, NovTemps, color='#00ddff', alpha=a, label="November")
ax11.axvline(x=32, color='black', alpha=a)
ax11.axvline(x=0, color='black', alpha=a)
ax11.legend()
ax12.fill_between(DecTemps.index, DecTemps, color='#0099ff', alpha=a, label="December")
ax12.set_xlabel("Observed Temperature in Fahrenheit")
ax12.legend()
ax12.axvline(x=32, color='black', alpha=a)
ax12.axvline(x=0, color='black', alpha=a)"""
f.subplots_adjust(hspace=0)
f.text(0.06, 0.5, "Number of Occurences", ha='center', va='center', rotation='vertical')
plt.xlim(-47,72)
plt.ylim(0,4500)
#f.set_ylabel("Number of Occurences")
plt.show()