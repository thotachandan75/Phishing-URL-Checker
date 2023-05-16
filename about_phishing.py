import streamlit as st
import main_app


def main():
    page_markdown = open("general_style.css", "r").read()
    st.markdown(f"<style>{page_markdown}</style>", unsafe_allow_html=True)

    st.title("About Phishing")
    columns = st.columns(2)
    with columns[0]:
        st.write("Phishing is a type of online scam in which cyber criminals use fraudulent emails, text,"
                 " messages, or websites to trick people into providing sensitive information such as"
                 " passwords, credit card numbers, and other Personal or financial information. Phishing"
                 " attacks are typically carried out via email, social media, instant messaging, or through"
                 " fake websites that are designed to look like legitimate ones.")
    with columns[1]:
        st.image(f"data:image/png;base64,{main_app.image_to_bytes('about_phishing/phishing.png')}")

    st.write("Phishing attacks typically involve impersonating a legitimate company, organisation, or"
             " individual in order to gain the trust of the victim. The attacker may use a variety of"
             " techniques to accomplish this, including creating fake websites that look identical to"
             " legitimate ones, or sending emails that appear to be from a trusted source.")
    st.write("Once the victim has been lured into providing their personal or financial information,"
             " the attacker can use it for a variety of malicious purposes, including identity theft,"
             " fraud, or unauthorised access to sensitive accounts.")

    st.header("Some common methods of phishing")
    columns = st.columns(2)
    with columns[1]:
        st.write("")
        st.write("Email Phishing: - This is the most common type of phishing attack, where attackers"
                 " send fraudulent emails to victims that appear to come from a trusted source, such as"
                 " a bank, social media platform, or online retailer. The emails usually include a link"
                 " that directs the victim to a fake website that looks like a legitimate one, where they"
                 " are asked to enter their personal information. The email may also include an attachment"
                 " that, if downloaded, can install malware on the victim’s computer.")
    with columns[0]:
        st.image(f"data:image/png;base64,{main_app.image_to_bytes('about_phishing/email.png')}")

    st.write("Smishing: - Smishing is a phishing attack that is carried out via SMS or text messages. The"
             " attackers will send a message with a link that leads to a fake website designed to steal"
             " personal information. The message may also the victim to reply with sensitive information"
             " or a call a phone number, which can connect them to a fraudulent call center. ")
    st.write("Spear Phishing: - Spear phishing is a more targeted type of phishing attack. Instead of"
             " sending out mass emails, attackers gather information about a specific individual or organization"
             " and create a personalized email that appears to be from a trusted source. The email may include"
             " information that appears to be specific to the victim, such as their job title or recent"
             " activities. The goal of spear phishing is to increase the likelihood that the victim will click "
             "on the link or attachment, or provide personal information.")
    st.write("Vishing: - Vishing is phishing attack carried out over the phone. The attackers will call the"
             " victim and pretend to be a representative from a legitimate organization, such as a bank, in"
             " order to obtain sensitive information. They may use techniques such as Caller ID spoofing to make"
             " it appear that the call is coming from a legitimate source.")

    columns = st.columns(2)
    with columns[0]:
        st.write("It’s important to note that these methods of phishing can overlap and be used in"
                 " combination. For example, a spear phishing attack may include a link to a fake website,"
                 " or a vishing attack may be followed up with an email containing a link or attachment.")
        st.write("To protect yourself from phishing attacks, it’s important to be cautious and take steps"
                 " to verify the source of any communication that asks for personal information. Be wary"
                 " of messages that create a sense of urgency or use threatening language, and always be "
                 "sceptical of unexpected messages that ask for personal information or request that you "
                 "take immediate action.")
    with columns[1]:
        st.write("")
        st.image(f"data:image/png;base64,{main_app.image_to_bytes('about_phishing/news.png')}")

    st.header("Anti - Phishing")
    st.write("Anti-phishing refers to the set of measures and techniques designed to prevent or mitigate the damage "
             "caused by phishing attacks. Here are some common techniques involved in anti-phishing")
    columns = st.columns(2)
    with columns[0]:
        st.image(f"data:image/png;base64,{main_app.image_to_bytes('about_phishing/safety.png')}")
    with columns[1]:
        st.write("Use Anti-Phishing Software: - Anti-phishing software can help detect and block phishing"
                 " attacks. Many web browsers and email providers include built-in anti-phishing tools."
                 " Additionally, there are third-party software solutions available that can provide "
                 "additional protection.")
        st.write("Implement Email Filters: - Email filters can help block phishing emails from reaching"
                 " your inbox. Most email providers offer customizable filters that allow you to block"
                 " emails based on certain criteria, such as sender address, subject line, or keywords.")
        st.write("Keep Software Updated: - Keeping your operating system, web browser, and other software"
                 " up-to-date with the latest security patches can help protect against known vulnerabilities"
                 " that can be exploited in phishing attacks.")
    st.write("Verify the Source: - Before clicking on any links or downloading any attachments, verify the"
             " source. Check the email address, URL, or phone number to make sure it is legitimate. If you are"
             " unsure, contact the organization directly to confirm the request.")
    st.write("Be Cautious with Personal Information: - Be wary of any request for personal information, "
             "particularly if it is unexpected or from an unfamiliar source. Do not provide any personal"
             " information unless you are certain it is necessary and legitimate.")
    st.write("Educate Yourself: - Learn how to recognize phishing attacks and stay up-to-date on the latest"
             " tactics used by attackers. Share this knowledge with friends, family, and colleagues to help"
             " protect them from phishing scams as well.")
    st.write("By following these security measures, you can help protect yourself from falling victim to"
             " a phishing attack. Remember to always be cautious and verify the source of any communication"
             " that asks for personal information.")

    st.header("Software Solutions to prevent phishing attacks")
    st.write("Email Filters: - Many email providers offer built-in filters that can help identify and"
             " block phishing emails. These filters use a variety of techniques, such as scanning for"
             " suspicious URLs or attachments, analysing the content of the email, and checking and"
             " sender’s reputation. ")
    st.write("Anti-Virus Software: - Anti-virus software can help protect against phishing attacks by identifying"
             " and blocking malicious software that may be used in a phishing campaign. Anti-virus software can"
             " also detect and remove malware from a user’s computer, which can help prevent further damage from"
             " a successful phishing attack.")
    st.write("Web Filters: - Web filters are designed to block access to malicious websites and other online"
             " threats. These filters use a variety of techniques, such as analysing the content of a website"
             " and checking its reputation, to identify and block potential threats.")
    st.write("Browser Extensions: - There are several browser extensions available that can help protect"
             " against phishing attacks. These extensions can block known phishing websites, warn users"
             " about suspicious websites, and provide other security features. ")
    st.write("Password Managers: - Password managers can help protect against phishing attacks by storing and "
             "encrypting passwords and other sensitive information. Password managers can also generate "
             "strong, unique passwords for each website, which can help prevent attackers from using stolen"
             " passwords to access other accounts. ")
