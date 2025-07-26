import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="TikTok Trend Tracker", layout="wide")

hashtag_data = pd.read_csv("data/hashtag_trends_log.csv", parse_dates=["Time"])
audio_data = pd.read_csv("data/trending_audio.csv")

st.title("📈 TikTok Trend Dashboard")

st.header("📊 Hashtag Trend Over Time")
selected_tags = st.multiselect("Choose hashtags to compare:", hashtag_data["Hashtag"].unique(), default=hashtag_data["Hashtag"].unique()[:2])

if selected_tags:
    fig, ax = plt.subplots()
    for tag in selected_tags:
        tag_data = hashtag_data[hashtag_data["Hashtag"] == tag]
        ax.plot(tag_data["Time"], tag_data["Total Likes"], label=tag)
    ax.set_ylabel("Total Likes")
    ax.set_xlabel("Time")
    ax.legend()
    st.pyplot(fig)

st.header("🎵 Trending Audio Today")
st.dataframe(audio_data)