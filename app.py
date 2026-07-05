import streamlit as st
import pandas as pd

with st.sidebar:                 # a control panel on the left
    theme = st.radio("Theme", ["Light", "Dark"])


if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["Name", "Age", "Flavor"])
    
name   = st.text_input("Name")
age    = st.slider("Age", 0, 100, 25)
agree  = st.checkbox("I accept the terms")
flavor = st.selectbox("Pick one", ["Vanilla", "Mango", "Mint"])

if st.button("Submit"):
    new_row = {
        "Name": name,
        "Age": age,
        "Flavor": flavor
    }
    st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([new_row])], ignore_index=True)
st.dataframe(st.session_state.df)