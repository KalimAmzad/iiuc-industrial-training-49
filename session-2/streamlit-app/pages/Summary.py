import streamlit as st
import requests
from utils import get_news_list, get_summary

# def app():
st.title("Summary Page")

news_list = get_news_list()
news_titles = {news['title']: news for news in news_list}
selected_title = st.selectbox("Select News Title", list(news_titles.keys()))

if selected_title:
    news = news_titles[selected_title]
    st.write(news['id'])
    st.write(news['title'])
    st.write(news['body'])
    st.write(f"Link: {news['link']}")
    st.write(f"Date: {news['datetime']}")
    st.write(f"Category: {news['category']}")
    st.write(f"Reporter: {news['reporter']}")
    st.write(f"Publisher: {news['publisher']}")

    if st.button("Generate Summary", type='primary'):
        summary = get_summary(news['id'])
        st.write("Summary:")
        st.write(summary['summary_text'])
