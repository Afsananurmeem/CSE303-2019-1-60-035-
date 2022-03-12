import pandas as pd

#%% data fream
df = pd.read_csv('weather.csv')
print(type(df))
print(df)

#%%
# first five record
print(df.head())

#%%
# last five record
print(df.tail())

#%%
# idea about deta only for numaric 
print(df.describe())



#%%

df.columns = ['outlook', 'temperature','humidity',
              'windy','play']
#%%
# series 

temp = df['temperature']
print(type(temp))

#%%
sum = 0
for value in temp:
    sum += value
    
print(sum)

#%%
df1 = df [['temperature','humidity']]

print(df1)



#%%
df2 = df.loc[0:9, ['temperature','humidity']]
print(df2)

#%%
df3 = df.iloc[0:10, [1,2] ]
print(df3)

#%% 
df4 = df.iloc[1::2, [0,1,3] ]
print(df4)

#%%
# all statistical mesudrement abot temp

print("Mean: ", df['temperature'].mean())

#%%

df.hist(column=['temperature'], bins = 10)

#%%

df.hist(column=['humidity'], bins = 5)

#%%
humidity = df[['humidity']]

print()

print("Mean: " ,humidity.mean())
print("Standard Deviation: ", humidity.std()) 
print("Variance: ", humidity.var())
print("Lower Quartile: ", humidity.quantile(0.25)) 
print("Median:", humidity.quantile (0.5)) 
print("Median: ",humidity.median())
print("Upper Quartile: ", humidity.quantile(0.75))
print("Skewness: ", humidity.skew())
print("Kurtosis: ", humidity.kurt())
print("Min: ", humidity.min()) 
print("Max: ", humidity.max())


#%%
list1 = [[1,1], [1,2], [2,3], [2,3],[2,4],
         [2,4],[3,4],[3,4],[4,5],[5,5]]

print(list1)

df_list1 = pd.DataFrame(list1, columns=['x','y'])
print(df_list1)

#%%

df_list1.hist(column=['x'], bins = 5)
























































