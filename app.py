import streamlit as st

st.write("Welcome !")

st.title("TDS Week-8 Assignment")
st.write("---")
st.header("Find the largest among the 3 given numbers")
with st.form(key="form1"):
    n1 = st.number_input("Enter the First Number :")
    n2 =st.number_input("Enter the Second Number :")
    n3 =st.number_input("Enter the Third Number :")
    button = st.form_submit_button("Find the maximum")
if button:
    st.success(f"The maximum number is {max([n1,n2,n3])} ")
    if n1==0 and n2 == 0 and n3 ==0:
        st.write("Instead of default, Try with some random values!")