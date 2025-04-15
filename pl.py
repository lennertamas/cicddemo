import bl
import streamlit as st

st.header('This is my demo app')
st.subheader('This is for demonstration the automated testing')

number = st.number_input("Give a number", 0)
if st.button('Calculate'):
    result = bl.isprime(number)
    if result:
        st.success('This is prime number')
    else:
        st.error('This is not prime')