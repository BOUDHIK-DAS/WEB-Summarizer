import streamlit as st
import newspaper
import nltk

nltk.download('punkt_tab')

st.title('WEB--SUM')
url = st.text_input('', placeholder='paste URL and enter')

if url:
    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        
        authors = article.authors
        st.text('Authors: ' + ', '.join(authors) if authors else 'No authors found.')

        article.nlp()
        
        st.text('Keywords: ' + ', '.join(article.keywords) if article.keywords else 'No keywords found.')

        tab1, tab2 = st.tabs(['Full text', 'Summary'])
        
        with tab1:
            st.text(article.text)
        
        with tab2:
            st.text(article.summary if article.summary else 'No summary available.')

    except Exception as e:
        st.error(f"An error occurred: {e}")
