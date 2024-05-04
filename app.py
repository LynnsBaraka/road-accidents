import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

# Load the trained KNN model
KNN_pipeline = joblib.load("KNN_gridsearch.joblib")

# Define options for dropdowns based on dataset info
options_flatHill = ['Flat', 'Hill']
options_holiday = ['Yes', 'No']
options_light = ['Daylight', 'Darkness: Lighted', 'Darkness: Not lighted', 'Dusk', 'Dawn', 'Unknown']
options_pedestrian = ['Yes', 'No']
options_roadCharacter = ['Straight', 'Curve', 'Roundabout', 'Unknown']
options_roadSurface = ['Dry', 'Wet', 'Snow', 'Ice', 'Sand/Mud/Dirt/Oil/Gravel', 'Other', 'Unknown']
options_streetLight = ['Lighted', 'Not Lighted', 'Unknown']
options_trafficControl = ['Traffic signal', 'Stop sign', 'Yield sign', 'No control', 'Other', 'Unknown']
options_weatherA = ['Clear', 'Rain', 'Sleet/Hail/Freezing Rain', 'Snow', 'Fog/Smog/Smoke', 'Severe Crosswinds',
                    'Blowing Sand, Soil, Dirt', 'Other', 'Unknown']
options_vehiclesInvolved = ['One vehicle', 'Two vehicles', 'Three vehicles', 'Four vehicles', 'Five or more vehicles']

# Main function for Streamlit app
def main():
    st.title("Road Accident Severity Prediction App 🚗💥")

    # Sidebar with user inputs
    st.sidebar.header("Enter Accident Details:")
    
    fatalCount = st.sidebar.number_input("Fatal Count", value=0)
    flatHill = st.sidebar.selectbox("Flat or Hill:", options_flatHill)  # Use the list directly
    holiday = st.sidebar.selectbox("Holiday:", options_holiday)
    light = st.sidebar.selectbox("Light Condition:", options_light)
    minorInjuryCount = st.sidebar.number_input("Minor Injury Count", value=0)
    pedestrian = st.sidebar.selectbox("Pedestrian Involved:", options_pedestrian)
    roadCharacter = st.sidebar.selectbox("Road Character:", options_roadCharacter)
    roadSurface = st.sidebar.selectbox("Road Surface:", options_roadSurface)
    seriousInjuryCount = st.sidebar.number_input("Serious Injury Count", value=0)
    speedLimit = st.sidebar.number_input("Speed Limit", value=30)
    streetLight = st.sidebar.selectbox("Street Light:", options_streetLight)
    trafficControl = st.sidebar.selectbox("Traffic Control:", options_trafficControl)
    weatherA = st.sidebar.selectbox("Weather:", options_weatherA)
    obstaclesHit = st.sidebar.number_input("Obstacles Hit", value=0)
    vehiclesInvolved = st.sidebar.selectbox("Vehicles Involved:", options_vehiclesInvolved)

    # Prediction button
    if st.sidebar.button("Predict Severity"):
        # Create a DataFrame with user inputs
        input_data = pd.DataFrame({
            
            'fatalCount': [fatalCount],
            'flatHill': [options_flatHill.index(flatHill)],  # Use the index of the selected option
            'holiday': [options_holiday.index(holiday)],
            'light': [options_light.index(light)],
            'minorInjuryCount': [minorInjuryCount],
            'pedestrian': [options_pedestrian.index(pedestrian)],
            'roadCharacter': [options_roadCharacter.index(roadCharacter)],
            'roadSurface': [options_roadSurface.index(roadSurface)],
            'seriousInjuryCount': [seriousInjuryCount],
            'speedLimit': [speedLimit],
            'streetLight': [options_streetLight.index(streetLight)],
            'trafficControl': [options_trafficControl.index(trafficControl)],
            'weatherA': [options_weatherA.index(weatherA)],
            'obstaclesHit': [obstaclesHit],
            'vehiclesInvolved': [options_vehiclesInvolved.index(vehiclesInvolved)]
        })

        # Make prediction
        prediction = KNN_pipeline.predict(input_data)[0]

        # Display prediction result
        st.subheader("Prediction:")
        st.write(f"The predicted accident severity is: {prediction}")

# Run the main function
if __name__ == '__main__':
    main()
