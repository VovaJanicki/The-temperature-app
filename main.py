import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")

days = st.slider("Forecast Days", max_value=1, min_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view ",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")
# def get_data(days):
#     dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
#     temperatures = [10, 11, 12]
#     temperatures = [days * i for i in temperatures]
#     return dates, temperatures
if place:
    try:

        # Get the temperature/sky data
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain":"images/rain.png", "Snow":"images/snow.png"}

            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_condition]
            print(sky_condition)
            st.image(image_paths, width=115)
    except KeyError:
        st.write("Does place is no exists.")
