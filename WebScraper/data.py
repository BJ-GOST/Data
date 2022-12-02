#you can install all the requirements with pip install -r requirements.txt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize


#This is code to extract a table from wikipedia showing United States presidential election results for Minnesota
#the read_html method returns a number of tables

Total_tables = pd.read_html('https://en.wikipedia.org/wiki/Minnesota')
print(f'dataframes: {len(Total_tables)}') #the result is 31 which is quite a lot of tables to deal with



#to obtain an exact table the match argument is used with the read_html function as below

exact_table = pd.read_html('https://en.wikipedia.org/wiki/Minnesota', match='United States presidential election results for Minnesota')
#print(f'dataframes: {len(exact_table)}') #the match argument returns a list of dataframes with one item that can be accessed as below

table =exact_table[0]
#print(table.info)# to get an overview of the dataframes information; and now to perform a numerical analysis of the data in the table it is important to convert the data into float 


#converting the table data for analysis
Republican_numbers = table['Republican'].replace({'%':''}, regex=True).astype('float')
Democratic_numbers = table['Democratic'].replace({'%':''}, regex=True).astype('float')
Third_party_numbers = table['Third party'].replace({'%':''}, regex=True).astype('float')


#grouping the data from the table with columns for year, number of voters per party and their respective percentages
Republicans = Republican_numbers['No.']
Democrats = Democratic_numbers['No.']
Thirds = Third_party_numbers['No.']
Years = table['Year']

republican_data = []
democrat_data = []
thirds_data = []
years  = []


#converting the data into one dimensional arrays that can be used to create a dataframe
for i in range(0,40):
    if i in republican_data:
        pass
    else:
        republican_data.append(Republicans[i])


for i in range(0, 40):
    if i in democrat_data:
        pass
    else:
        democrat_data.append(Democrats[i])


for i in range(0, 40):
    if i in thirds_data:
        pass
    else:
        thirds_data.append(Thirds[i])



#creating a new dataframe
df = pd.DataFrame({
    'Republicans': republican_data,
    'Democrats': democrat_data,
    'Third Party': thirds_data, 
})


#adding the years column to the new dataframe
new_df = (pd.concat([df, Years], 
                   axis = 1))


# df.concat(Years)
print(new_df)


# plotting various graphs

#a curve graph of Republican votes through the years
y = new_df['Republicans'].values.tolist()[0:39]
x = new_df['Year'].values.tolist()[0:39]

plt.plot(x, y)
plt.title("Curve Graph showing Republican voters between 1860 and 2020")
plt.ylabel("Republican voters")
plt.xlabel("Years")
plt.show()




#a piechart showing total voters for each group in 2020
groups = ['Republicans', 'Democrats', 'Thirds']
REPUBLICANS = new_df.at[0, 'Republicans']
DEMOCRATS = new_df.at[0, 'Democrats']
THIRDS = new_df.at[0, 'Third Party']

slices = [REPUBLICANS, DEMOCRATS, THIRDS]
  

colors = ['r', 'y', 'g']
  
plt.pie(slices, labels = groups, colors=colors, 
        startangle=90, shadow = True, explode = (0, 0, 0.1),
        radius = 1.2, autopct = '%1.1f%%')
  
plt.legend()
  
plt.show()




#a barchart showing voters for various groups in the year 2020
left = [1, 2, 3]
height = [REPUBLICANS, DEMOCRATS, THIRDS]
labels = ['Republicans', 'Democrats', 'Third Party', ]

plt.bar(left, height, tick_label = labels,
        width = 0.8, color = ['red', 'green', 'blue'])
  
plt.xlabel('Parties')
plt.ylabel('Numbers')

plt.title('Number of voters per party in Minnesota 2020')
plt.show()