import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv(r'Movies.csv')
df.head()     

info=df.info()
print(info)

shape=df.shape
print("Shape of the dataset is :",shape) 

size= df.size
print("Size of the dataset is :",size)

columns=df.columns
print("Columns  Names in the dataset are :",columns)

datatype=df.dtypes
print("Datatypes of the data are :",datatype)

duplicate=df.duplicated().sum()
print("Duplicate values are :",duplicate)


df=df.drop(['Directors'],axis=1)
print(df.columns)

null_values=df.isnull().sum()
print(null_values)

df['Runtime'] = df['Runtime'].fillna(30)
null_values=df.isnull().sum()
print(null_values)

df.dropna(how='any',inplace=True)
null_values=df.isnull().sum()
print(null_values)


country=(df['Country'] == 'United States').sum()
print("\nMovies from United States are :",country)

Genres=df[df['Genres'] == 'Action']
unique=(df['Runtime'] > 100).value_counts()
print("\n",unique)

result=df.groupby(['Genres']).agg({'Runtime' : ['max','min']})
print(result)

# Data Visualization

#pie chart

x=df['Runtime'].sort_values().head(10)
label=df['Title'].head(10)
myexplode=[0.1]*10
plt.pie(x,labels=label,startangle=45,counterclock='true',autopct='%1.1f%%',explode=myexplode
        ,wedgeprops= {"linewidth":4},center=(0,0))
plt.show()  

#Scatter Plot

y=df['Runtime'].head(20).sort_values()
x=df['Title'].head(20)
plt.scatter(x,y)
plt.ylabel('Runtime')
plt.xlabel('Movies')
plt.title('Runtime According To Title')
plt.xticks(rotation=90)
plt.show()

# Count Plot

x=df['Country'].head(30)
sns.countplot(x=x,data=df)
plt.xlabel('Country')
plt.xticks(rotation=90) 
plt.show()

# Bar graph

y=df['Runtime'].head(20)
x=df['Title'].head(20)
plt.title('Movies and Runtime')
plt.xlabel('Movies')
plt.ylabel('Runtime')
sns.barplot(x,y)
plt.xticks(rotation=90)
plt.show()

# Distribution Plot
sns.distplot(df['IMDb'])
plt.show()

# Histogram

plt.hist(df['Age'])
plt.xlabel('Age')
plt.ylabel('frequency')
plt.title('Frequency Of Age')
plt.show()  

df.to_excel("Project.xls")