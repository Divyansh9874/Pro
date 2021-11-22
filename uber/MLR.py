import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data=pd.read_csv('taxi.csv')

data_x=data.iloc[:,0:-1].values#dependent variable,used iloc to access group of row and column by integer podition value..
data_y=data.iloc[:,-1].values#independent variable


x_train,x_test,y_train,y_test=train_test_split(data_x,data_y,test_size=0.3,random_state=0)#here we split data for training and testing

#applying MLR.
reg=LinearRegression()#regressor
reg.fit(x_train,y_train)#trained data

#print("Train score:",reg.score(x_train,y_train))
#print("Test score:",reg.score(x_test,y_test))

pickle.dump(reg,open('taxi.pkl','wb'))#ML model is ready in serialize form.

model=pickle.load(open('taxi.pkl','rb'))#read binary for loading.
#print(model.predict([[80,1770000,6000,85]]))
