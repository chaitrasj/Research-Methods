import matplotlib.pyplot as plt
import pandas as pd

######################## a-Scatter Plot ##############################

df = pd.read_excel(r'State_UT-wise Forest cover as per India State of Forest Report (ISFR) during 2015.xls')
df = df.to_numpy()

state = df[:,0]
geographical_area = df[:,1]
tot_forest_cover = df[:,2]
perc_geog_area = df[:,3]

fig = plt.figure(figsize=(30,8))
ax = plt.gca().xaxis
ax.grid(linewidth='1.5')

plt.scatter(state, geographical_area, color='b', label='Geographical Area')
plt.xticks(state, rotation='vertical', fontsize=12)
plt.xlabel('States/UTs', fontsize=18)
plt.ylabel('Area in square Kilometers', fontsize=18)

plt.scatter(state, tot_forest_cover, color='r', label='Forest Cover')
plt.legend(fontsize=15)
plt.title('Scatter Plot - State/UT-wise Forest cover as per India State of Forest Report (ISFR) during 2015', fontsize=18)
plt.show()
fig.savefig('a_Scatter_plot.png')

######################## a-Bar Plot ##############################

fig = plt.figure(figsize=(20,8))
plt.bar(state, perc_geog_area)
plt.xticks(state, rotation='vertical', fontsize=13)
plt.xlabel('States/UTs', fontsize=18)
plt.ylabel('Percentage of Forest cover', fontsize=18)
plt.title('Bar plot - State/UT-wise Percentage of Geographical area under Forest cover', fontsize=18)
plt.show()
fig.savefig('a_Bar_plot.png')


######################## b-Box Plot ##############################

df = pd.read_excel(r'All_India_Area_Weighted_Monthly_Seasonal_And_Annual_Rainfall.xls')
df = df.to_numpy()
year = df[:,0][::3]

fig = plt.figure(figsize=(20,8))
month = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']

plt.boxplot([df[:,1], df[:,2], df[:,3], df[:,4], df[:,5], df[:,6], df[:,7], df[:,8], df[:,9], df[:,10], df[:,11], df[:,12]], labels=month)
plt.xlabel('Month', fontsize=18)
plt.ylabel('Annual Rainfall in mm', fontsize=16)
plt.xticks(fontsize=15)
plt.yticks(fontsize=12)
plt.title('Box plot - All India Monthly Seasonal Rainfall', fontsize=20)
plt.show()
fig.savefig('b_Box_plot.png')

######################## b-Box Plot ##############################

df = pd.read_excel(r'All_India_Area_Weighted_Monthly_Seasonal_And_Annual_Rainfall.xls')
df = df.to_numpy()
year = df[:,0][::3]

fig = plt.figure(figsize=(20,8))
plt.plot(year, df[:,1][::3], marker='o', color='b', label='Jan')
plt.plot(year, df[:,4][::3], marker='o', color='g', label='April')
plt.plot(year, df[:,7][::3], marker='o', color='r', label='July')
plt.plot(year, df[:,10][::3], marker='o', label='Oct')
plt.ylabel('Annual Rainfall in mm', fontsize=16)
plt.xlabel('Year', fontsize=15)
plt.xticks(year, rotation='vertical', fontsize=13)
plt.title('Line plot - All India Yearly Seasonal Rainfall', fontsize=18)
plt.legend(fontsize=15)
plt.show()
fig.savefig('c_Line_plot.png')
