import sys
print(sys.version)

import pandas as pd

df = pd.read_csv(r'C:\Users\User01\Desktop\bonus_info.csv')

##Visualize the sum of vacation hours on a scatter chart and analyze bonus compared to vacation hours

import matplotlib.pyplot as plt

Average_hours = [55, 35, 33, 34, 27, 24, 23, 26, 39, 38, 53, 37, 36, 29]
Bonus = [0, 75, 500, 985, 2000, 2500, 3500, 3550, 3900, 4100, 5000, 5150, 5650, 6700]

plt.scatter(Average_hours, Bonus)

xlab = 'Annual leave [in Hours]'
ylab = 'Bonus [in GPD]'
title = 'Comparing bonus and annual leave'

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

plt.show()

##Visualize the sum of total revenue on a bar chart and analyze growth revenue

%matplotlib inline

plt.style.use('ggplot')country = ['USA','Canada','Australia','GB','France','Germany']

revenue = [70829863, 18398929, 11814376, 8574048,8119749,5479819]
colors = ['green', 'blue', 'purple', 'brown', 'teal','yellow']

plt.bar(country, revenue,color = colors)
plt.xlabel("Countries")
plt.ylabel(" Total Sales in 10 Millions")
plt.title("Countries total Revenue 2011-2014")
plt.savefig("Totals sales in millions.jpg")plt.show()

plt.show()


#Extract sql results from csv file.
df=pd.read_csv('job_vs_leave.csv')
df.head()

#Plot horizontal bar chart grading colors from light to dark to show higher intensity of person type against job tilte
plt.style.use('dark_background')
plt.title('JobTitle(PersonType) vs SickLeave(Hrs)' , color='royalblue', font='Georgia')
colors=('papayawhip','papayawhip','papayawhip','papayawhip','papayawhip','papayawhip',
        'papayawhip','papayawhip','papayawhip','papayawhip','papayawhip','papayawhip',
        'papayawhip','papayawhip', 'blanchedalmond', 'blanchedalmond','blanchedalmond',
        'blanchedalmond','tan', 'tan', 'tan', 'tan','burlywood', 'orange', 'darkorange',
        'goldenrod', 'darkgoldenrod' )
plt.barh(df.JobTitle, df.SickLeaveHours, color= colors)
plt.xlabel('AVERAGE SICK LEAVE HOURS TAKEN', color='royalblue', font='Georgia')plt.show()


#Extract sql results from csv file
df= pd.read_csv('US_regional_Sales.csv')
df.head()

# Plot bar chart to vizualize sales.
plt.style.use('ggplot')
plt.title('REGIONAL SALES IN THE US', color='royalblue')

colors= ['orange', 'orange','burlywood','darkorange', 'darkorange']

plt.bar(df.Region, df.Sales, color=colors)
plt.ylabel('SALES  IN MILLIONS', color='royalblue')
plt.xlabel('US REGIONS', color='royalblue')
plt.yticks([0.0, 2000000, 4000000, 6000000, 8000000, 10000000], ['0.0M', '2.0M', '4.0M', '6.0M', '8.0M', '10.0M'])

plt.show()


#Import relevant package
import seaborn as sns

#Display the first 5 row of information in the table
print(df.head())

# Show the relationship between the three variables
# (Number of employees, Size in Square Feet and Annual Revenue)
# example 1
# scatter plot
df.plot (x = 'NumberEmployees', y='SquareFeet',c='AnnualRevenue', kind= 'scatter',
           title= 'Relationship between Revenue, Number of employees and Business Size', colormap = 'Oranges')# Show the relationship between the three variables

# (Number of employees, Size in Square Feet and Annual Revenue)
# example 2
# scatter plot
sns.relplot(data=df, x="NumberEmployees", y="SquareFeet",
            hue="AnnualRevenue", height=7, aspect=2)# # Show the relationship between the three variables

# (Number of employees, Size in Square Feet and Annual Revenue)
# example 3
# scatter plot by revenue groupings
sns.relplot(data=df, x="NumberEmployees", y="SquareFeet",
            hue="AnnualRevenue", height=4, aspect=1,
            style="AnnualRevenue",col="AnnualRevenue", col_wrap = 3)
#diplay all 3 graphs
plt.show()

# table style pair correlations
#pair correlations (2 variables)
df_correlation = df.corr()
print(df_correlation)

# correlation between AnnualRevenue and Square
print(df['AnnualRevenue'].corr(df['SquareFeet']))

 # correlation between SquareFeet and NumberEmployees
print(df['SquareFeet'].corr(df['NumberEmployees']))

 # correlation between AnnualRevenue and NumberEmployees
print(df['AnnualRevenue'].corr(df['NumberEmployees']))