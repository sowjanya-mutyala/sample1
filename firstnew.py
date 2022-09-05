import streamlit as st
st.header('ramachandra college of engineering')
a=st.number_input('Enter any value')
if st.button('HIT ME'):
  st.success(f'Your Lucky Number is {a}')
 
