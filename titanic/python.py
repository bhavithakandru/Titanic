import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
test = pd.read_csv('/Users/bhavithakandru/Desktop/NEU/work/titanic/test.csv')
train = pd.read_csv('/Users/bhavithakandru/Desktop/NEU/work/titanic/train.csv')
train.isnull().sum()
train['Age']=train['Age'].fillna(-0.5)
test['Age']=test['Age'].fillna(-0.5)
bins =[-1,0,5,10,18,24,35,60,np.inf]
labels = ['Unknown','Infant','Baby','Child','Teen','Young','Adult','Old']
train['Age_group']=pd.cut(train['Age'],bins=bins,labels=labels) 
test['Age_group']=pd.cut(test['Age'],bins=bins,labels=labels)
train['Age_group'].mean
combine = [test,train]
for i in combine:
    i['Title']=i.Name.str.extract(' ([A-Za-z]+)\.',expand=False)
    pd.crosstab(train['Name'],train['Sex'])
print(train['Title'].info())
for i in combine:
    i['Title']=i['Title'].replace(['Lady','Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Rare'])
    i['Title']=i['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
    i['Title']=i['Title'].replace('Mlle','Miss')
    i['Title']=i['Title'].replace('Ms','Miss')
    i['Title']=i['Title'].replace('Mme','Mrs')
    train[['Title','Survived']].groupby(['Title'],as_index=False).mean()
    