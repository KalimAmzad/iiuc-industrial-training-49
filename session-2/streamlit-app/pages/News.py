import streamlit as st
from utils import get_news_list, get_news_by_id, scrape_news

st.title("News Page")

option = st.selectbox(
    "Choose an action",
    ["All News", "News by ID", "Scrape News"]
)

if option == "All News":
    limit = 10
    if 'skip' not in st.session_state:
        st.session_state.skip = 0

    news_list = get_news_list(skip=st.session_state.skip, limit=limit)
    st.write(f"Displaying {len(news_list)} news articles")

    col1, col2 = st.columns(2)
    half = len(news_list) // 2

    for i, news in enumerate(news_list):
        with (col1 if i < half else col2):
            with st.expander(news['title']):
                st.markdown(f"{news['body']}")
                st.code(news['link'], language='text')
                st.markdown(f"**Date:** {news['datetime']}")
                st.caption(f"**Category:** {news['category']['name']} - {news['category']['description']}")
                st.caption(f"**Reporter:** {news['reporter']['name']} ({news['reporter']['email']})")
                st.caption(f"**Publisher:** {news['publisher']['name']} ({news['publisher']['email']})")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous"):
            if st.session_state.skip >= limit:
                st.session_state.skip -= limit
                st.experimental_rerun()
    with col3:
        if st.button("Next"):
            st.session_state.skip += limit
            st.experimental_rerun()

elif option == "News by ID":
    news_id = st.number_input("Enter News ID", min_value=1, step=1)
    if st.button("Get News"):
        news = get_news_by_id(news_id)
        if news:
            st.balloons()
            st.markdown(f"**Title:** {news['title']}")
            st.markdown(f"**Body:** {news['body']}")
            st.code(news['link'], language='text')
            st.markdown(f"**Date:** {news['datetime']}")
            st.caption(f"**Category:** {news['category']['name']} - {news['category']['description']}")
            st.caption(f"**Reporter:** {news['reporter']['name']} ({news['reporter']['email']})")
            st.caption(f"**Publisher:** {news['publisher']['name']} ({news['publisher']['email']})")
        else:
            st.error("News not found")

elif option == "Scrape News":
    urls = st.text_area("Enter URLs (comma-separated)")
    if st.button("Scrape"):
        url_list = [url.strip() for url in urls.split(",")]
        scraped_news = scrape_news(url_list)
        st.success("News scraping initiated")

        col1, col2 = st.columns(2)
        half = len(scraped_news) // 2

        for i, news in enumerate(scraped_news):
            with (col1 if i < half else col2):
                with st.expander(news['title']):
                    st.markdown(f"**Body:** {news['body']}")
                    st.code(news['link'], language='text')
                    st.markdown(f"**Date:** {news['datetime']}")
                    st.caption(f"**Category:** {news['category']['name']} - {news['category']['description']}")
                    st.caption(f"**Reporter:** {news['reporter']['name']} ({news['reporter']['email']})")
                    st.caption(f"**Publisher:** {news['publisher']['name']} ({news['publisher']['email']})")
