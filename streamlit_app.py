import pandas as pd
import plotly.express as px
import streamlit as st


st.title("Week 1 - Data and visualization")
st.markdown("Here we can see the dataframe created during this weeks project.")


dataframe = pd.read_csv(
    "WK1_Airbnb_Amsterdam_listings_proj_solution.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Meters from chosen location",
        "Location",
    ],
)


dataframe = dataframe[dataframe["Price"] <= 500]


dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)

dataframe["Price"] = "RON " + dataframe["Price"].round(2).astype(str)

dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "To visit", 0.0: "Airbnb listing"}
)


st.dataframe(dataframe)
st.markdown("Below is a map showing all the Airbnb listings with a red dot and the location we've chosen with a blue dot. Currency: RON (Romanian currency")


fig = px.scatter_mapbox(
    dataframe,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    zoom=11,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Meters from chosen location", "Location"],
    labels={"color": "Locations"},
)
fig.update_geos(center=dict(lat=dataframe.iloc[0][2], lon=dataframe.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")


st.plotly_chart(fig, use_container_width=True)
