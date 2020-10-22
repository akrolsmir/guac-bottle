import streamlit as st
import altair as alt
import pandas as pd


df = pd.DataFrame(
    {
        "index": [3, 4, 5, 6],
        "numbers": [10, 50, 30, 40],
    }
)
st.write(df)

st.write("Zooms horizontally")
scales = alt.selection_interval(bind="scales", encodings=["x"])
st.write(
    alt.Chart(df)
    .mark_bar()
    .encode(alt.Y("numbers"), alt.X("index"))
    .add_selection(scales)
)

st.write("Zooms vertically")
st.write(
    alt.Chart(df)
    .mark_bar()
    .encode(
        alt.Y("numbers"),
        alt.X("index", type="ordinal"),
    )
    .add_selection(scales)
    .interactive()
)
