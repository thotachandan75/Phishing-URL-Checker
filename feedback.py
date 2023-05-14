import streamlit as st
import pymongo


def form_function():
    with st.form(key="phishing_feedback"):
        ans1 = st.text_input("Name", placeholder="Enter your full name", key="q1")
        ans2 = st.number_input("Enter your Age", min_value=5, max_value=100, value=25, key="q2")
        ans3 = st.radio(
            "Do you think your workplace or educational institution does enough to educate "
            "employees or students about phishing scams?", ["Yes", "Maybe", "No"], index=1, key="q3")
        ans4 = st.radio("Have you been a victim of online fraud?", ["Yes", "No"], index=1, key="q4")
        ans5 = st.selectbox("How can individuals protect themselves against phishing attacks?",
                            ["Always clicking on links in emails from unknown senders",
                             "Ignoring warnings from web browsers about unsafe sites",
                             "Being cautious of unsolicited messages and verifying the source",
                             "Sharing personal information with every website visited"], index=0, key="q5")
        ans6 = st.text_area("What are some of the consequences of falling for a phishing scam?",
                            placeholder="Mention all which are applicable", key="q6")
        ans7 = st.radio("What are some tools or technologies that can help prevent phishing attacks? ",
                        ["Anti-phishing software", "Email filters", "Multi-factor authentication", "All of the above"],
                        index=0, key="q7")
        ans8 = st.radio(
            "Have you ever clicked on a link sent by someone unknown by phone calls/ sms that turned "
            "out to be a phishing scam?", ["Yes", "No"], index=1, key="q8")
        ans9 = st.slider("How would you rate our website?", min_value=1, max_value=5, value=3, key="q9")
        ans10 = st.text_area("Share your suggestions to improve our website?",
                             placeholder="Enter any comments", key="q10")
        submit = st.form_submit_button(label="Submit this form")
    return submit, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10


def form_callback(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
    if st.session_state.q1 == "" or len(st.session_state.q1) <= 3:
        st.warning("Please Fill your full name")
    else:
        st.success("Your Responses are recorded, Thank you for visiting our website")
        st.balloons()
        connection = pymongo.MongoClient(st.secrets["mongodb"]["url"])
        database = connection.get_database("WebsiteFeedback")
        table = database.UserFeedback

        response_data = {
            "S_No": (table.count_documents({}) + 1),
            "Question1": ans1,
            "Question2": ans2,
            "Question3": ans3,
            "Question4": ans4,
            "Question5": ans5,
            "Question6": ans6,
            "Question7": ans7,
            "Question8": ans8,
            "Question9": ans9,
            "Question10": ans10
        }
        table.insert_one(response_data)


def main():

    st.title("Feedback Form")

    sub, an1, an2, an3, an4, an5, an6, an7, an8, an9, an10 = form_function()
    if sub:
        form_callback(an1, an2, an3, an4, an5, an6, an7, an8, an9, an10)
