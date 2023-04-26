import streamlit as st
import streamlit_analytics
from streamlit_elements import elements, html

from utils.constants import SECTIONS

st.set_page_config(page_title="GetSmart", page_icon=":snake:")

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
# st.video(
#     "https://platform.thinkific.com/videoproxy/v1/play/c80no3h69ueleahijou0",
#     format="video/mp4",
# )
