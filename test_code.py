import streamlit as st
option = st.selectbox('Pick one:',('a','b','c'))
st.write('You selected: ', option)
