import streamlit as st
from click import option

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", max_value=1, min_value=5,
                 help="Select the number of forecasted days")
st.subheader(f"{option} for the next {days} days in {place}")
