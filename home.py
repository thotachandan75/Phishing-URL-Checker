import streamlit as st
import model_implementation
import pickle
import tensorflow as tf
import numpy as np
# import warnings
#
# warnings.filterwarnings("ignore")


def main():
    style = """
    #MainMenu {
        visibility: hidden;
    }

    h1 {
        text-align: center;
    }
    
    h2 {
        text-align: center;
    }
    
    h3 {
        text-align: center;
    }

    footer {
        visibility: hidden;
    }
    """
    st.markdown(style, unsafe_allow_html=True)
    st.title("Home")

    url = st.text_input("Please enter the website URl", "https://www.google.com")
    result = model_implementation.main(url)
    st.write(result)

    st.write("The source code for the website is present in the below github link")
    github_link = '<a href="https://github.com/chandanthota75/Phishing_url_checker"' \
                  ' target="_blank" class="github_link" >Github Link</a>'
    st.markdown(github_link, unsafe_allow_html=True)
    st.subheader("Thank You for visiting our Web app, feel free to contact us")

if __name__ == "__main__":
    main()
