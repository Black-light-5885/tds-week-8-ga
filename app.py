import streamlit as st

st.write("Welcome !")

st.title("TDS week 8 assignemnt")
st.write("---")
st.header("Finding the maximum number given in the three numbers.")
with st.form(key="form1"):
    n1 = st.number_input("Selct Your First Number :")
    n2 =st.number_input("Select Your Second Number :")
    n3 =st.number_input("Select your Third Number :")
    button = st.form_submit_button("Find the maximum")
if button:
    st.success(f"The maximum number is {max([n1,n2,n3])} ")