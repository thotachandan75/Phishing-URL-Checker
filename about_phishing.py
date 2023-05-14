import streamlit as st


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
    
    st.title("About Phishing")

    st.write("Phishing is a type of online scam in which cyber criminals use fraudulent emails, text, messages, "
             "or websites to trick people into providing sensitive information such as passwords, credit card "
             "numbers, and other Personal or financial information. Phishing attacks are typically carried out via "
             "email, social media, instant messaging, or through fake websites that are designed to look like "
             "legitimate ones.")
    st.write("Phishing attacks typically involve impersonating a legitimate company, organisation, or individual in "
             "order to gain the trust of the victim. The attacker may use a variety of techniques to accomplish this, "
             "including creating fake websites that look identical to legitimate ones, or sending emails that appear "
             "to be from a trusted source.")
    st.write("Once the victim has been lured into providing their personal or financial information, the attacker can "
             "use it for a variety of malicious purposes, including identity theft, fraud, or unauthorised access to "
             "sensitive accounts.")

    st.header("Some common methods of phishing")
    st.subheader("Email Phishing")
    st.write("This is the most common type of phishing attack, where attackers send fraudulent emails to victims that "
             "appear to come from a trusted source, such as a bank, social media platform, or online retailer. The "
             "emails usually include a link that directs the victim to a fake website that looks like a legitimate "
             "one, where they are asked to enter their personal information. The email may also include an attachment "
             "that, if downloaded, can install malware on the victim’s computer.")

    st.subheader("Smishing")
    st.write("Smishing is a phishing attack that is carried out via SMS or text messages. The attackers will send a "
             "message with a link that leads to a fake website designed to steal personal information. The message "
             "may also the victim to reply with sensitive information or a call a phone number, which can connect "
             "them to a fraudulent call center. ")

    st.subheader("Spear Phishing")
    st.write("Spear phishing is a more targeted type of phishing attack. Instead of sending out mass emails, "
             "attackers gather information about a specific individual or organization and create a personalized "
             "email that appears to be from a trusted source. The email may include information that appears to be "
             "specific to the victim, such as their job title or recent activities. The goal of spear phishing is to "
             "increase the likelihood that the victim will click on the link or attachment, or provide personal "
             "information. ")

    st.subheader("Vishing")
    st.write("Vishing is phishing attack carried out over the phone. The attackers will call the victim and pretend "
             "to be a representative from a legitimate organization, such as a bank, in order to obtain sensitive "
             "information. They may use techniques such as Caller ID spoofing to make it appear that the call is "
             "coming from a legitimate source. ")

    st.write("It’s important to note that these methods of phishing can overlap and be used in combination. For "
             "example, a spear phishing attack may include a link to a fake website, or a vishing attack may be "
             "followed up with an email containing a link or attachment.")
    st.write("To protect yourself from phishing attacks, it’s important to be cautious and take steps to verify the "
             "source of any communication that asks for personal information. Be wary of messages that create a sense "
             "of urgency or use threatening language, and always be sceptical of unexpected messages that ask for "
             "personal information or request that you take immediate action.")

    st.header("Anti - Phishing")
    st.write("Anti-phishing refers to the set of measures and techniques designed to prevent or mitigate the damage "
             "caused by phishing attacks. Here are some common techniques involved in anti-phishing: - ")
    st.subheader("Use Anti-Phishing Software")
    st.write("Anti-phishing software can help detect and block phishing attacks. Many web browsers and email "
             "providers include built-in anti-phishing tools. Additionally, there are third-party software solutions "
             "available that can provide additional protection.")

    st.subheader("Implement Email Filters")
    st.write("Email filters can help block phishing emails from reaching your inbox. Most email providers offer "
             "customizable filters that allow you to block emails based on certain criteria, such as sender address, "
             "subject line, or keywords.")

    st.subheader("Keep Software Updated: ")
    st.write("Keeping your operating system, web browser, and other software up-to-date with the latest security "
             "patches can help protect against known vulnerabilities that can be exploited in phishing attacks.")

    st.subheader("Verify the Source")
    st.write("Before clicking on any links or downloading any attachments, verify the source. Check the email "
             "address, URL, or phone number to make sure it is legitimate. If you are unsure, contact the "
             "organization directly to confirm the request.")

    st.subheader("Be Cautious with Personal Information")
    st.write("Be wary of any request for personal information, particularly if it is unexpected or from an unfamiliar "
             "source. Do not provide any personal information unless you are certain it is necessary and legitimate.")

    st.subheader("Educate Yourself")
    st.write("Learn how to recognize phishing attacks and stay up-to-date on the latest tactics used by attackers. "
             "Share this knowledge with friends, family, and colleagues to help protect them from phishing scams as "
             "well.")
    st.write("By following these security measures, you can help protect yourself from falling victim to a phishing "
             "attack. Remember to always be cautious and verify the source of any communication that asks for "
             "personal information.")

    st.header("Software Solutions to prevent phishing attacks")
    st.subheader("Email Filters")
    st.write("Many email providers offer built-in filters that can help identify and block phishing emails. These "
             "filters use a variety of techniques, such as scanning for suspicious URLs or attachments, analysing the "
             "content of the email, and checking and sender’s reputation. ")

    st.subheader("Anti-Virus Software")
    st.write("Anti-virus software can help protect against phishing attacks by identifying and blocking malicious "
             "software that may be used in a phishing campaign. Anti-virus software can also detect and remove "
             "malware from a user’s computer, which can help prevent further damage from a successful phishing attack.")

    st.subheader("Web Filters")
    st.write("Web filters are designed to block access to malicious websites and other online threats. These filters "
             "use a variety of techniques, such as analysing the content of a website and checking its reputation, "
             "to identify and block potential threats.")

    st.subheader("Browser Extensions")
    st.write("There are several browser extensions available that can help protect against phishing attacks. These "
             "extensions can block known phishing websites, warn users about suspicious websites, and provide other "
             "security features. ")

    st.subheader("Password Managers")
    st.write("Password managers can help protect against phishing attacks by storing and encrypting passwords and "
             "other sensitive information. Password managers can also generate strong, unique passwords for each "
             "website, which can help prevent attackers from using stolen passwords to access other accounts. ")


