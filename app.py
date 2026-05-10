import streamlit as st

# Header
st.title("Mechanical Unit Converter and Material Density Checker")

# Student Info
st.write("Name: Muhammad Shahbaz Malik")
st.write("Roll Number: 25-ME-155")

st.markdown("---")

# Unit Converter Section
st.header("Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Force", "Pressure", "Temperature"]
)

value = st.number_input("Enter Value")

if conversion_type == "Length":
    unit = st.selectbox("Convert", ["mm to cm", "cm to m", "m to mm"])
    if unit == "mm to cm":
        result = value / 10
    elif unit == "cm to m":
        result = value / 100
    else:
        result = value * 1000

elif conversion_type == "Force":
    unit = st.selectbox("Convert", ["N to kN", "kN to N"])
    if unit == "N to kN":
        result = value / 1000
    else:
        result = value * 1000

elif conversion_type == "Pressure":
    unit = st.selectbox("Convert", ["Pa to kPa", "kPa to MPa"])
    if unit == "Pa to kPa":
        result = value / 1000
    else:
        result = value / 1000

elif conversion_type == "Temperature":
    unit = st.selectbox("Convert", ["C to F", "F to C"])
    if unit == "C to F":
        result = (value * 9/5) + 32
    else:
        result = (value - 32) * 5/9

st.success(f"Converted Value: {result}")

st.markdown("---")

# Material Density Checker Section
st.header("Material Density Checker")

materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Iron": 7874
}

material = st.selectbox("Select Material", list(materials.keys()))

st.info(f"Density of {material}: {materials[material]} kg/m³")
