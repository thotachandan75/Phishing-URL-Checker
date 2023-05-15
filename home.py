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
    
    st.warning("Below model will only accept complete URL only. Please check the URL format before passing it to the URL input field below")
    
    url = st.text_input("Please enter complete URL of the website to check its legitimacy")
    if url == "":
        pass
    elif is_complete_url(url):
        result = model_implementation.main(url)
        if result == "Legetimate":
            st.success("The Entered website is a Legetimate website")
        else:
            st.warning('The Entered website is used for Phishing your data')
    else:
        st.warning("The Entered URL is incomplete/wrong, please check the format of the entered URL again")
        st.warning('A URL is a string of characters that provides a reference to a resource on the Internet. A complete URL consists of multiple components, including the scheme, the network location, and any additional path and query parameters.')
        st.warning('The scheme specifies the protocol used to access the resource on the server, and is usually followed by a colon and two forward slashes ("://").')
        st.warning('The network location specifies the domain name or IP address of the server where the resource is located, and is separated from the scheme by a forward slash ("/").')
        st.warning('To check whether a URL is complete or not, you need to ensure that it includes both the scheme and the network location. If either of these components is missing, the URL is not complete.')
        st.warning('A URL without a scheme (e.g., "www.example.com") is not complete because it is missing the scheme component.')
        st.warning('A URL without a network location (e.g., "https://") is not complete because it is missing the network location component.')
    
    st.write("Spoofed websites are fake websites that are designed to mimic the appearance and functionality of a legitimate website. These websites are created by cybercriminals with the intention of stealing personal information, such as login credentials, credit card numbers, and other sensitive data from unsuspecting users.")
    st.write("Spoofed websites are often used in phishing attacks, where users receive emails or other messages that direct them to the fake website. The email or message may contain a link that appears to be legitimate, but actually leads to the fake website. Once the user visits the spoofed website, they are prompted to enter their login credentials or other personal information, which is then captured by the attackers.")
    st.write("To create a spoofed website, attackers may use techniques such as domain spoofing, where they register a domain name that is similar to the legitimate website's domain name, or they may use website cloning software to replicate the appearance and functionality of the legitimate website.")
    st.write("It's important to be cautious when entering personal information online and to always check the legitimacy of a website before entering any sensitive data. One way to do this is to look for the padlock icon in the browser's address bar, which indicates that the website is using a secure connection (HTTPS) and has a valid security certificate. Additionally, be wary of emails or messages that ask you to enter personal information or click on links, especially if they seem suspicious or out of the ordinary.")
    
    st.subheader('This Webapp is curriculum-based project, which is constructed as a part of "Engineering Project in Community Services" by the students of VIT Bhopal.')
    st.write("The source code for the website is present in the below github link")
    github_link = '<a href="https://github.com/chandanthota75/Phishing-URL-Checker"' \
                  ' target="_blank" class="github_link" >Github Link</a>'
    st.markdown(github_link, unsafe_allow_html=True)
    st.write("Thank You for visiting our Web app, feel free to contact us")
