# Importing Streamlit for creating the web-based user interface
import streamlit as st

# Function to convert units
def convert_unit(value, unit_from, unit_to):
    
    # Dictionary to store conversion factors for different units
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,   # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,    # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000      # 1 kilogram = 1000 grams
    }
    
    # Creating a key based on the selected units (e.g., "meters_kilometers")
    key = f"{unit_from}_{unit_to}"
    
    # Checking if the key exists in the dictionary
    if key in conversions:
        conversion_factor = conversions[key]  # Get the conversion factor
        return value * conversion_factor  # Multiply input value by conversion factor
    else:
        return "Conversion not supported"  # Return this if the conversion is not available

# Setting the title of the Streamlit app
st.title("Unit Converter")

# Asking the user to input a numeric value for conversion
# min_value=1.0 ensures the value is at least 1, and step=1.0 allows incrementing in steps of 1
value = st.number_input("Enter the value to convert", min_value=1.0, step=1.0)

# Dropdown for selecting the unit to convert from
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])

# Dropdown for selecting the unit to convert to
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Button to perform the conversion
if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)  # Call the function with user inputs
    st.write(f"Converted value is: {result}")  # Display the result on the screen
