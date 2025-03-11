import streamlit as st

# Set Streamlit Page Config
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        body {background-color: #F5F7F8;}
        .stApp {background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);}
        h1 {color: #ff4b4b; text-align: center;}
        .stSelectbox, .stNumberInput, .stButton {background-color: #e0f7fa; border-radius: 10px;}
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>🔄  Unit Converter 🔄</h1>", unsafe_allow_html=True)

# Conversion dictionary
conversion_rates = {
    "km to miles": 0.621371,
    "miles to km": 1.60934,
    "kg to pounds": 2.20462,
    "pounds to kg": 0.453592,
    "meters to feet": 3.28084,
    "feet to meters": 0.3048
}

# User input section
st.subheader("📌 Enter Details Below:")
amount = st.number_input("🔢 Enter Value:", min_value=0.0, format="%.2f")

# Available units
units = ["km", "miles", "kg", "pounds", "meters", "feet"]

col1, col2 = st.columns(2)
with col1:
    unit_from = st.selectbox("📤 Convert From:", units)
with col2:
    filtered_units = [u for u in units if u != unit_from]  # Remove selected unit
    unit_to = st.selectbox("📥 Convert To:", filtered_units)

# Conversion logic
st.markdown("---")  # Adds a line separator

if st.button("🔄 Convert"):
    key = f"{unit_from} to {unit_to}"
    if key in conversion_rates:
        result = amount * conversion_rates[key]
        st.success(f"✅ **{amount} {unit_from}** = **{result:.2f} {unit_to}** 🎉")
    else:
        st.error("⚠️ Invalid conversion! Please select appropriate units.")

# Footer
st.markdown(
    "<br><hr><center>🚀 Made with ❤️ by <b>ZARTASH IMRAN </b></center>",
    unsafe_allow_html=True
)
