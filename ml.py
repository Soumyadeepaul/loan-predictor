import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import pickle
def mode_fill(null):
    mode = df[null].mode()
    df[null] = df[null].replace(np.nan, mode[0])


def mean_fill(null):
    mean = df[null].mean()
    df[null] = df[null].replace(np.nan, mean)


df=pd.read_csv('loan_data set.csv')
df=df.drop('Loan_ID',axis=1)


nan = ['Gender', 'Married', 'Dependents', 'Self_Employed']
for i in nan:
    mode_fill(i)


nan = ['LoanAmount', 'Loan_Amount_Term', 'Credit_History']
for i in nan:
    mean_fill(i)

df["Gender"].replace({'Female':1,'Male':0},inplace=True)
df["Married"].replace({'Yes':1,'No':0},inplace=True)
df["Dependents"].replace({'3+':'3'},inplace=True)
df["Dependents"]=df["Dependents"].astype("int")
df['Education']=df["Education"].replace({"Graduate":1,"Not Graduate":0})
df["Self_Employed"].replace({'Yes':1,'No':0},inplace=True)
df["Property_Area"].replace({'Urban':2, 'Rural':0, 'Semiurban':1},inplace=True)

df['Loan_Amount_Term']=df['Loan_Amount_Term']/30
df["Loan_Amount_Term"].replace({0.4:0.5,1.2:1,2.0:2,2.8:3,4.0:4,6.0:6,8.0:8,10.0:10,11.4:11,12.0:12,16.0:16},inplace=True)

y=df['Loan_Status']


X=df[['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

k=10
neigh=KNeighborsClassifier(n_neighbors=k).fit(X_train,y_train)
pickle.dump(neigh,open("model.pkl",'wb'))
