import streamlit as st
import model_implementation
import pickle
import tensorflow as tf
import numpy as np


def main():
    page_markdown = open("general_style.css", "r").read()
    st.markdown(f"<style>{page_markdown}</style>", unsafe_allow_html=True)
    
    st.title("Home")

    url = st.text_input("Please Enter the Website URL in the below text box")
    result = model_implementation.main(url)
    st.write(result)

    st.write("The source code for the website is present in the below github link")
    github_link = '<a href="https://github.com/chandanthota75/Phishing-URL-Checker"' \
                  ' target="_blank" class="github_link" >Github Link</a>'
    st.markdown(github_link, unsafe_allow_html=True)
    st.write("Thank You for visiting our Web app, feel free to contact us")
