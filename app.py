import streamlit as st

st.set_page_config(page_title="Simple Calculator", layout="centered")

st.title("🧮 Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

operation = st.selectbox(
    "Select operation:",
    ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"]
)

# Calculate result
result = None

if st.button("Calculate"):
    if operation == "Add (+)":
        result = num1 + num2

    elif operation == "Subtract (-)":
        result = num1 - num2

    elif operation == "Multiply (×)":
        result = num1 * num2

    elif operation == "Divide (÷)":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"Result: **{result}**")
