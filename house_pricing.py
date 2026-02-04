import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#data set
data={'sqft': [1500, 2000, 1200, 2500, 1800, 1350, 3000, 2200],
    'bedrooms': [3, 3, 2, 4, 3, 2, 5, 3],
    'age_of_house': [10, 5, 20, 1, 15, 12, 2, 8],
    'city': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi'],
    'price_in_lakhs': [150, 210, 110, 320, 175, 125, 400, 230]
}
df=pd.DataFrame(data)
df_final=pd.get_dummies(df,columns=['city'] )

X=df_final.drop('price_in_lakhs',axis=1) #features
y=df_final['price_in_lakhs']    #data

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=42)

#train
model=LinearRegression()
model.fit(X_train,y_train)

#lets predict for a 2100 sqft, 3 bedrooms, 4-year-old house in bangalore
new_house = pd.DataFrame([[2100, 3, 4, 1, 0, 0]], 
                         columns=['sqft', 'bedrooms', 'age_of_house', 'city_Bangalore', 'city_Delhi', 'city_Mumbai'])
predicted_price= model.predict(new_house)
print(f"predicted house price : ₹{predicted_price[0]:.2f} lakhs ")
