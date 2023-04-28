import streamlit as st
import streamlit_authenticator as stauth
import yaml
from streamlit_elements import elements, html
from yaml.loader import SafeLoader

from utils.utils import *

st.set_page_config(page_title="GetSmart", page_icon=":snake:")

# hashed_passwords = stauth.Hasher(['admin']).generate()
# print(hashed_passwords)
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    authenticator.logout("Logout", "main")
    st.write(f"Welcome *{name}*")
    st.header("Welcome to the Python Certification App")

    st.write(
        "This app is designed to help you prepare for Python certification exams, including PCEP and PCAP. Use the sidebar to navigate between pages and select the topics you want to study."
    )

    # Add the first video
    with elements("video1"):
        html.iframe(
            src="https://platform.thinkific.com/videoproxy/v1/play/c80no3h69ueleahijou0",
            width="710",
            height="400",
        )
elif authentication_status is False:
    st.error("Username/password is incorrect")
    


elif authentication_status is None:
    # st.warning('Please enter your username and password')
    create_new_user()

    create_new_username()

    create_new_password()

# st.video(
#     "https://platform.thinkific.com/videoproxy/v1/play/c80no3h69ueleahijou0",
#     format="video/mp4",
# )
