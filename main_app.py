import streamlit as st
import home
import about_phishing
import url_model_analysis
import faqs
import feedback
import contact_us
import base64


def image_to_bytes(image_path):
    image_file = open(image_path, "rb")
    image_bytes = image_file.read()
    encoded_image = base64.b64encode(image_bytes).decode()
    return encoded_image


def main():
    st.set_page_config(
        page_title="Phishing URL Checker",
        page_icon=f"data:image/png;"
                  f"base64,{image_to_bytes('main/WebsiteImages/page_icon.png')}",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.sidebar.title("Phishing URL Checker")
    st.write("<script>window.scrollTo(0, 0);</script>", unsafe_allow_html=True)
    st.sidebar.subheader("")

    pages_list = ["Home", "About Phishing", "URL Model Analysis", "FAQS", "Feedback", "Contact US"]
    page = st.sidebar.radio("GO TO", pages_list)

    if page == "Home":
        home.main()
    elif page == "About Phishing":
        about_phishing.main()
    elif page == "URL Model Analysis":
        url_model_analysis.main()
    elif page == "FAQS":
        faqs.main()
    elif page == "Feedback":
        feedback.main()
    elif page == "Contact US":
        contact_us.main()

    st.sidebar.title("Thank You for visiting our Web app")
    st.sidebar.subheader("")
    st.sidebar.write("Please take a few minutes from your busy schedule and provide us your feedback.")
    st.sidebar.write("Your feedback is valuable to us. It helps us to improve our Web analysis app")


if __name__ == "__main__":
    main()
