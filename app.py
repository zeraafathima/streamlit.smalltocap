import streamlit as st 
st.header('small to capital application')
st.image('images.jfif')
st.write('This is a application to change lowercase to uppercase letters')
y=st.text_input(label='enter the sentence')
x=st.button('change')
if x:
    y=y.upper()
    st.subheader(y)