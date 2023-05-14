import streamlit as st
import streamlit.components.v1 as components


def main():
    columns = st.columns(2)
    with columns[0]:
        st.title("Frequently Asked Questions")
    with columns[1]:
        st.title("")
        st.write("Got a Question? We're here to answer! if you don't see your question here, drop us a line on our "
                 "Contact US Page")

    def read_file(filename):
        with open(filename, "r") as f:
            return f.read()

    st.header("")
    html_file = read_file("faqs/faqs.html")
    components.html(html_file, height=1000)
