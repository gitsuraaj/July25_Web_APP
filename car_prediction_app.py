import pandas as pd
import streamlit as st
import pickle

cars_df = pd.read_csv("./cars24-car-price.csv")

st.write(
    """
     # Cars24 Used Car Price Prediction
    """
)
st.dataframe(cars_df.head())

## Encoding Categorical features - use the same encodings you have used while training your data
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}


# User Inputs

col1, col2, col3 = st.columns(3)

year_value = col1.number_input("Enter the year of manufacture", 1980, 2023, step=1, value=2020)
seller_type_value = col1.selectbox("Select the seller type",["Dealer", "Individual", "Trustmark Dealer"])
kilometer_value = col1.number_input("Enter the kilometers driven", 0, 1000000, step=1000, value=120000)

fuel_type_value = col2.selectbox("Select the fuel type",["Diesel", "Petrol", "CNG", "LPG", "Electric"])
transmission_type_value = col2.selectbox("Select the transmission type",["Manual", "Automatic"])
mileage_value = col2.number_input("Enter the mileage (in kmpl)", 0, 100, step=1, value=15)

engine_value = col3.slider("Set the Engine Power", 500, 5000, step=100)
power_value = col3.number_input("Enter the power (in bhp)", 0, 500, step=5, value=100)
seats_value = col3.selectbox("Enter the number of seats",[4,5,7,9,11])



#encoding user inputs (only categorical features)

fuel_type_encoded = encode_dict['fuel_type'][fuel_type_value]
transmission_type_encoded = encode_dict['transmission_type'][transmission_type_value]
encoded_seller_type = encode_dict["seller_type"][seller_type_value]


def model_pred(year_value, seller_type_value, kilometer_value, fuel_type_encoded, transmission_type_encoded, 
                           mileage_value, engine_value, power_value ,seats_value):
    with open("car_pred", 'rb') as file:
        reg_model = pickle.load(file)
        input_features = [[year_value, seller_type_value, kilometer_value, fuel_type_encoded, transmission_type_encoded, 
                           mileage_value, engine_value, power_value ,seats_value]]

        return reg_model.predict(input_features)


# a button to call my model and send all the encoded data in the right format and sequence

if st.button("Predict Price"):
    price= model_pred(year_value, encoded_seller_type, kilometer_value, fuel_type_encoded, transmission_type_encoded, 
                           mileage_value, engine_value, power_value ,seats_value)
    st.text (price)
    #first task to get data from user and encode it using the dictionary


