import streamlit as st
from urllib.parse import urlparse
import model_implementation
import pickle
import tensorflow as tf
import numpy as np


def is_complete_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme and parsed_url.netloc:
        return True
    else:
        return False

    
def main():
    page_markdown = open("general_style.css", "r").read()
    st.markdown(f"<style>{page_markdown}</style>", unsafe_allow_html=True)
    
    st.title("Home")
    
    url = st.text_input("Please enter complete URL of the website to check its legitimacy")
    if url != "":
        pass
    elif is_complete_url(url):
        result = model_implementation.main(url)
        if result == "Legetimate":
            st.success("The Entered website is a Legetimate website")
        else:
            st.warning("The Entered website is used for Phishing your data")
    else:
        st.warning("The Entered URL is incomplete/wrong, please check the format of the entered URL again")

    st.write("The source code for the website is present in the below github link")
    github_link = '<a href="https://github.com/chandanthota75/Phishing-URL-Checker"' \
                  ' target="_blank" class="github_link" >Github Link</a>'
    st.markdown(github_link, unsafe_allow_html=True)
    st.write("Thank You for visiting our Web app, feel free to contact us")
