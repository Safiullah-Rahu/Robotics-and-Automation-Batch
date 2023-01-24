import streamlit as st

st.header('st.button')

if st.button('Is it cold?'):
	st.write("Yep!")
	st.snow()
else:
	st.write('Goodbye')