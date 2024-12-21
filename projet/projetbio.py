#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 12:53:56 2024

@author: --
used tutorials : w3schools.com/python /// geeksforgeeks.org /// Stack Overflow
"""

import pandas as pd
import matplotlib.pyplot as plt


# open csv file and import into dataframe
datain = pd.read_csv('./input/data_medium.csv', sep=';') # read csv data files with separator ;



# Graph # 1
# line graph of number of bacteria per day and per mouse
###

# get list of mouse
lst=datain['mouse_ID'].unique()

# for each mouse in list, loop to plot
for id in lst:
        # filter dataframe to get datas from mouse ID and fecal with ABX
        df_fe_abx = datain[(datain['sample_type']=='fecal')&(datain['mouse_ID']==id)&(datain['treatment']=='ABX')] 
        
        # filter dataframe to get datas from mouse ID and fecal with placebo
        df_fe_pla = datain[(datain['sample_type']=='fecal')&(datain['mouse_ID']==id)&(datain['treatment']=='placebo')] 
        
        # plot datas abx in red, placebo in blue
        plt.plot(df_fe_abx['experimental_day'],df_fe_abx['counts_live_bacteria_per_wet_g'], color = 'r', linewidth = '0.5')
        plt.plot(df_fe_pla['experimental_day'],df_fe_pla['counts_live_bacteria_per_wet_g'], color = 'b', linewidth = '0.5')

# use logarithm vertical axis and add labels to axis
plt.yscale('log')
plt.xlabel('Day')
plt.ylabel('# bacteria (log scale)')

# plotting 2 dummy points to add labels to series
plt.plot([0],[0], color = 'r', linewidth = '0.5',label = 'ABX')
plt.plot(0,0, color = 'b', linewidth = '0.5',label = 'Placebo')
plt.legend()

# save line graph
plt.savefig('./images/graph_lines.png')

# save data used to plot
dataout=datain[datain['sample_type']=='fecal']
dataout.to_csv('./output/outfile_fec.csv',header=True,index=False, sep=';',columns=['mouse_ID','experimental_day','counts_live_bacteria_per_wet_g'])
    


# Graph # 2
# violin graph of # bocteria in Cecal samples
###

# prepare figure geometry for cecal : 1 row, 2 columns, share the same vertical size
figc, axc = plt.subplots(nrows=1, ncols=2,sharey = True) 


# violin cecal graph
# filter dataframe for cecal
df_cec_abx = datain[(datain['sample_type']=='cecal')&(datain['treatment']=='ABX')] 
df_cec_pla = datain[(datain['sample_type']=='cecal')&(datain['treatment']=='placebo')] 


# plot the data in first subplot
vp = axc[0].violinplot(df_cec_abx['counts_live_bacteria_per_wet_g'])
for body in vp['bodies']:
    body.set_facecolor('red') # access "bodies" parameter of graph to define color
    
# add title and use log scale
axc[0].set_title('ABX Cecal (log scale)')
axc[0].set_yscale('log')

# plot the data in second subplot
vp = axc[1].violinplot(df_cec_pla['counts_live_bacteria_per_wet_g'])
for body in vp['bodies']:
    body.set_facecolor('blue') # access "bodies" parameter of graph to define color
    
# add title and use log scale
axc[1].set_title('Placebo Cecal (log scale)')
axc[1].set_yscale('log')

# save graph
plt.savefig('./images/graph_cecal.png')



# Graph # 3
# violin graph of # bocteria in Ileal samples
###

# prepare figure geometry for cecal : 1 row, 2 columns, share the same vertical size
figi, axi = plt.subplots(nrows=1, ncols=2,sharey = True) 


# violin cecal graph
# filter dataframe for cecal
df_ile_abx = datain[(datain['sample_type']=='ileal')&(datain['treatment']=='ABX')] 
df_ile_pla = datain[(datain['sample_type']=='ileal')&(datain['treatment']=='placebo')] 


# plot the data in first subplot
vp = axi[0].violinplot(df_ile_abx['counts_live_bacteria_per_wet_g'])
for body in vp['bodies']:
    body.set_facecolor('red') # access "bodies" parameter of graph to define color
    
# add title and use log scale
axi[0].set_title('ABX Ileal (log scale)')
axi[0].set_yscale('log')

# plot the data in second subplot
vp = axi[1].violinplot(df_ile_pla['counts_live_bacteria_per_wet_g'])
for body in vp['bodies']:
    body.set_facecolor('blue') # access "bodies" parameter of graph to define color
    
# add title and use log scale
axi[1].set_title('Placebo ileal (log scale)')
axi[1].set_yscale('log')

# save graph
plt.savefig('./images/graph_ileal.png')

# save datas
dataout=datain[(datain['sample_type']=='cecal')|(datain['sample_type']=='ileal')]
dataout.to_csv('./output/outfile_ile_cec.csv',header=True,index=False, sep=';',columns=['mouse_ID','sample_type','counts_live_bacteria_per_wet_g'])
