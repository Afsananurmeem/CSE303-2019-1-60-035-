

import pandas as pd
df = pd.read_csv('dataset_lab04.csv')
# df.info()
#%%
def Lab04_Task1_2019_1_60_035():
    print ('Number of rows: ', df.shape[0])
    print ('Number of columns: ', df.shape[1])



#%%
def Lab04_Task2_2019_1_60_035():
    print(df[['Time', 'Amount']].describe())
    

#%%
def Lab04_Task3_2019_1_60_035():
    #df.columns = ['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount','Class']
    at_least_two_columns = df[['Time','V5','V6','V7','V8','Amount']]
    print(at_least_two_columns)
    
    print("Mean: " ,at_least_two_columns.mean())
    print("")
    print("Median: ",at_least_two_columns.quantile(0.5)) 
    print("")
    print("Standard Deviation: ",at_least_two_columns.std()) 
    print("")
    print("Variance: ",at_least_two_columns.var())
    print("")
    


#%%
def Lab04_Task4_2019_1_60_035():
    time_and_amount = df[['Time','Amount']]
    df.boxplot(column= ['Time','Amount'])    
    
    print("Lower Quartile: " ,time_and_amount.quantile(0.25))
    print("")
    print("Median: " ,time_and_amount.median())
    print("")
    print("Upper Quartile: " ,time_and_amount.quantile(0.75))
    print("")
    print("IQR: ",(time_and_amount.quantile(0.75))-(time_and_amount.quantile(0.25)))
    print("")
    print("Min: ",time_and_amount.min())
    print("")
    print("Max: ",time_and_amount.max())
    print("")
    
    #Tthere is no outliers for time, we can confirm by visualization
    # of boxplot also from the calculation
    
    # Also for amount there is no outliers. Though the visualization
    # is not good enough, we have confirm it by calculation





#%%
def Lab04_Task5_2019_1_60_035():
    df[['Time']].hist(column = ['Time'], bins = 8, color='y')
    
    df[['Amount']].hist(column = ['Amount'], bins = 80, color='y')   
    
    time_and_amount = df[['Time','Amount']]
    print("Skewness: " ,time_and_amount.skew())
    print("")
    print("Kurtosis: " ,time_and_amount.kurt())
    print("")
    
    



#%%
def Lab04_Task6_2019_1_60_035():
    cl0 = (len(df[df['Class']==0])*100)/len(df['Class'])
    cl1 = (len(df[df['Class']==1])*100)/len(df['Class'])
    
    print("Percentage of class value 0 : %.2f "%(cl0))
    print("Percentage of class value 1 : %.2f "%(cl1))    




#%%
def Lab04_Task7_2019_1_60_035():
    
    cl0 = df[df['Class']==0]
    cl1 = df[df['Class']==1]
    
    cl0.hist(column = ['Class'], bins = 3, color='y')
    cl1.hist(column = ['Class'], bins = 5, color='y')



#%%

def Lab04_Task8_2019_1_60_035():
    
    cl0 = (len(df[df['Class']==0])*100)/len(df['Class'])
    cl1 = (len(df[df['Class']==1])*100)/len(df['Class'])
    
    bar_chart = pd.DataFrame({'Classes':['Class 0', 'Class 1'], 'Percentage':[cl0, cl1]})
    ax = bar_chart.plot.bar(x='Classes', y='Percentage', rot=0)





#%%

def Lab04_Task9_2019_1_60_035():
    df[['V5']].hist(column = ['V5'], bins = 150, color='g')
    #It is positive skew
    df[['V16']].hist(column = ['V16'], bins = 60, color='g')
    #It is negative skew
    df[['V2']].hist(column = ['V2'], bins = 150, color='g')
    #It is leptokurtic
    df[['V26']].hist(column = ['V26'], bins = 60, color='g')
    #It is platykurtic
    




#%%

def Lab04_Task10_2019_1_60_035():
    correlation= df.corr(method='pearson')
    
    positive_correlation = correlation[correlation > 0]
    print(positive_correlation)
    print("")
    
    highest_positive_correlation = positive_correlation.unstack().sort_values()
    print(highest_positive_correlation)
    print("")
    print(highest_positive_correlation[0])



    



#%%

def Lab04_Task11_2019_1_60_035():
    correlation= df.corr(method='pearson')
    
    positive_correlation = correlation[correlation > 0]
    positive_correlation.plot.scatter(x=['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount','Class'],
                                      y=['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount','Class'])





#%%

def Lab04_Task12_2019_1_60_035():
    correlation= df.corr(method='pearson')
    
    negative_correlation = correlation[correlation < 0]
    print(negative_correlation)
    print("")
    
    highest_negative_correlation = negative_correlation.unstack().sort_values()
    print(highest_negative_correlation)
    print("")
    print(highest_negative_correlation[0])




#%%

def Lab04_Task13_2019_1_60_035():
    correlation= df.corr(method='pearson')
    
    negative_correlation = correlation[correlation < 0]
    negative_correlation.plot.scatter(x=['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount','Class'],
                                      y=['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount','Class'])






#%%

def Lab04_Task14_2019_1_60_035():
    df.boxplot(column= ['Amount']) 
    


#%%

def Lab04_Task15_2019_1_60_035():
    #time_and_amount = df[['Time','Amount']]
    #df.boxplot(column= ['Time','Amount'])    
    
    amount_0 = df[df['Amount']==0]
    amount_1 = df[df['Amount']==1]
    
    
    amount_0.boxplot(column= 'Amount' )
    amount_1.boxplot(column= 'Amount' )
    
    #Here we can see that for both class = 0 and class = 1 the mean, median, max, Q1, Q3 all are same
    



#%% Calling the functions


Lab04_Task1_2019_1_60_035()
Lab04_Task2_2019_1_60_035()
Lab04_Task3_2019_1_60_035()
Lab04_Task4_2019_1_60_035()
Lab04_Task5_2019_1_60_035()
Lab04_Task6_2019_1_60_035()
Lab04_Task7_2019_1_60_035()
Lab04_Task8_2019_1_60_035()
Lab04_Task9_2019_1_60_035()
Lab04_Task10_2019_1_60_035()
Lab04_Task11_2019_1_60_035()
Lab04_Task12_2019_1_60_035()
Lab04_Task13_2019_1_60_035()
Lab04_Task14_2019_1_60_035()
Lab04_Task15_2019_1_60_035()























































