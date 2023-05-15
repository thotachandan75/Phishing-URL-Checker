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
    if url == "":
        pass
    elif is_complete_url(url):
        result = model_implementation.main(url)
        if result == "Legetimate":
            st.success("The Entered website is a Legetimate website")
        else:
            st.warning("The Entered website is used for Phishing your data")
    else:
        st.warning("The Entered URL is incomplete/wrong, please check the format of the entered URL again")
    
    st.write("Spoofed websites are fake websites that are designed to mimic the appearance and functionality of a legitimate website. These websites are created by cybercriminals with the intention of stealing personal information, such as login credentials, credit card numbers, and other sensitive data from unsuspecting users.")
    st.write("Spoofed websites are often used in phishing attacks, where users receive emails or other messages that direct them to the fake website. The email or message may contain a link that appears to be legitimate, but actually leads to the fake website. Once the user visits the spoofed website, they are prompted to enter their login credentials or other personal information, which is then captured by the attackers.")
    st.write("To create a spoofed website, attackers may use techniques such as domain spoofing, where they register a domain name that is similar to the legitimate website's domain name, or they may use website cloning software to replicate the appearance and functionality of the legitimate website.")
    st.write("It's important to be cautious when entering personal information online and to always check the legitimacy of a website before entering any sensitive data. One way to do this is to look for the padlock icon in the browser's address bar, which indicates that the website is using a secure connection (HTTPS) and has a valid security certificate. Additionally, be wary of emails or messages that ask you to enter personal information or click on links, especially if they seem suspicious or out of the ordinary.")
    
    st.write('This Webapp is curriculum-based project, which is constructed as a part of "Engineering Project in '
         'Community Services" by the students of VIT Bhopal The Key contributors for the project are')
    st.write("The source code for the website is present in the below github link")
    github_link = '<a href="https://github.com/chandanthota75/Phishing-URL-Checker"' \
                  ' target="_blank" class="github_link" >Github Link</a>'
    st.markdown(github_link, unsafe_allow_html=True)
    st.write("Thank You for visiting our Web app, feel free to contact us")
