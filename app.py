import streamlit as st

st.write("Welcome !")

st.title("TDS week 8 assignemnt")
st.write("---")
st.header("Finding the maximum number given in the three numbers.")

n1 = st.number_input("First Number :")
n2 =st.number_input("Second Number :")
n3 =st.number_input("Third Number :")
m = max([n1,n2,n3])
st.write(str(m))
st.write("The maximum number is ")