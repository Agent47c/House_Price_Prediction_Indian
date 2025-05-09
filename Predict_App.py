import streamlit as st
import joblib
import numpy as np
model=joblib.load("Random_Forest.pkl")
st.title("India House Price Prediction")
st.write("This App Predict Price Of Houses In India With The Help Of Machine Learning")
st.write("Its Using Linear Regression Model For Predictions")
st.write("Input 'Number Of Bedrooms' , 'Number Of Bathrooms' , 'Living Area' , 'Condition Of The House' , 'Number Of Schools Nearby' For The Prediction")
st.divider()
Bedrooms=st.number_input('Number Of Bedrooms',min_value=0,value=0)
Bathrooms=st.number_input('Number Of Bathrooms',min_value=0,value=0)
Living_Area=st.number_input('Living Area (SqFt)',min_value=0,value=2000)
Cnd_house=st.number_input('Condition Of The House',min_value=0,max_value=5,value=3)
no_school=st.number_input('Number Of Schools Nearby',min_value=0,max_value=3,value=2)
st.divider()
predict_btn=st.button("Predict!")
if predict_btn:
    st.balloons()
    X=[[Bedrooms,Bathrooms,Living_Area,Cnd_house,no_school]]
    X_array=np.array(X)
    prediction=model.predict(X_array)
    predicted_price = round(prediction.item(),2)
    st.write(f"🏠 The Predicted Price Of The House Is: ₹{predicted_price:,.2f}")
    
else:
    st.write("Press The Button After Entering The Data Correctly")
    