import numpy as np
import pickle
import streamlit as st
import os

# Load the pickled machine learning model
@st.cache_data  # Cache the model loading to improve performance
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Get the directory path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the model file
model_path = os.path.join(script_dir, 'trained_model.sav')

# Load the model using the cache function
loaded_model = load_model(model_path)

# Creating a function to predict the carbon emission
def predict_emission(input_data):
    # Reshape input_data for prediction
    input_data_reshaped = input_data.reshape(1, -1)  # Reshape to (1, 11)
    # Make predictions using the trained model
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def main():
    st.title("Carbon Emission Prediction Web App")
    
    Relative_carbon_intensity = st.number_input("Relative carbon intensity (tonnes CO2 / $1M USD revenue)")                                                  
    Total_financed_emissions_scope_1_2 = st.number_input("Total financed emissions scope 1 + 2 (tCO2e)")                          
    Total_financed_emissions_scope_1_2_3= st.number_input("Total financed emissions scope 1 + 2 + 3 (tCO2e)")
    Carbon_footprint_portfolio_coverage_by_market_value_weight = st.number_input("Carbon footprint portfolio coverage by market value weight")           
    Carbon_footprint_portfolio_coverage_by_number_of_disclosing_titles = st.number_input("Carbon footprint portfolio coverage by number of disclosing titles")
    Fossil_fuel_holdings_count= st.number_input("Fossil fuel holdings, count")                                         
    Fossil_fuel_holdings_weight= st.number_input("Fossil fuel holdings, weight")                                       
    Deforestation_risk_producer_count  = st.number_input("Deforestation-risk producer, count")                            
    Deforestation_risk_producer_weight  = st.number_input("Deforestation-risk producer, weight")                          
    Fund_net_assets =   st.number_input("Fund net assets")                                                          
    Percent_rated = st.number_input("Percent rated")

    Outcome = ''

    if st.button('Predict'):
        input_data = np.array([Relative_carbon_intensity, Total_financed_emissions_scope_1_2, Total_financed_emissions_scope_1_2_3, Carbon_footprint_portfolio_coverage_by_market_value_weight, Carbon_footprint_portfolio_coverage_by_number_of_disclosing_titles, Fossil_fuel_holdings_count, Fossil_fuel_holdings_weight, Deforestation_risk_producer_count, Deforestation_risk_producer_weight, Fund_net_assets, Percent_rated])
        
        prediction = predict_emission(input_data)
        Outcome = f'Predicted Emission: {prediction[0]:.2f} tons CO2e'
        st.success(Outcome)

if __name__ == '__main__':
    main()
