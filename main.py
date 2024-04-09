import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")  # add a ? icon as a help widget

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

# we have to make sure the place is entered, or we will get an error
if place:
    try:
        # get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            # create temperature line graph plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            # watch out of the data structure of filtered_data, we can use debugger to identify it easily
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]

            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]

            # create sky image
            st.image(image_paths, width=115)
    except KeyError:
        st.error("That place does not exist")
