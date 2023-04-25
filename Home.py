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
# with elements("video1"):
#     html.iframe(
#         src="https://platform.thinkific.com/videoproxy/v1/play/c80no3h69ueleahijou0",
#         width="710",
#         height="400",

#     )
st.video(
    "https://platform.thinkific.com/videoproxy/v1/play/c80no3h69ueleahijou0",
    format="video/mp4",
)

with streamlit_analytics.track():
    st.text_input("Write something")
    st.button("Click me")


def pcep_page():
    st.header("PCEP Certification")
    options = [section for section in SECTIONS]
    selected_option = st.selectbox("Select a topic", options)
    if selected_option == "Intro To PCEP":
        st.write("This section provides an introduction to PCEP.")
        with elements("video2"):
            html.iframe(
                src="https://www.youtube.com/embed/8qG463VRPjI?wmode=opaque",
                width="732px",
                height="422px",
            )
    elif selected_option == "Numbering Systems":
        st.write(SECTIONS[selected_option]["description"])
        with st.expander(f"Intro to {selected_option}"):
            st.write(SECTIONS[selected_option]["intro_text"])
            with elements("numbers"):
                html.iframe(
                    width="640",
                    height="360",
                    src="https://www.youtube.com/embed/FFDMzbrEXaE?wmode=opaque",
                )
        with st.expander("Vocabulary Terms"):
            # st.write(
            #     "Here are some vocabulary terms that you should be familiar with before diving into PCEP."
            # )
            for vocab in SECTIONS[selected_option]["vocabulary_terms"]:
                st.write(f"*{vocab['term']}*: {vocab['definition']}")
        with st.expander("Study"):
            st.write(SECTIONS[selected_option]["study_resources"]["intro_text"])
            with elements("study"):
                html.iframe(
                    src="https://quizlet.com/662948012/learn/embed?i=489qnu&x=1jj1",
                    height="550",
                    width="100%",
                )
        with st.expander("Quiz"):
            st.write("Test your knowledge with this quiz on Numbering Systems.")
            # iterate over each question and display it to the user
            for i, question in enumerate(SECTIONS[selected_option]["quiz_questions"]):
                # display the question text
                # st.write(f"{i + 1}. {question['question']}")

                selected = st.radio(
                    f"{i + 1}. {question['question']}",
                    question["choices"],
                )
                # display the answer choices
                for j, choice in enumerate(question["choices"]):
                    global score

                    if selected == choice and j == question["correct_answer"]:
                        score += 1

            # add a submit button for the form
            if st.button("Submit", key=f"{selected_option} quiz"):
                # display final score
                st.write(
                    f"Final Score: {score} out of {len(SECTIONS[selected_option]['quiz_questions'])}"
                )

    elif selected_option == "Bitwise Operations":
        st.write("This section covers bitwise operations in Python.")
        with st.expander("Intro to Bitwise Operations"):
            st.write(
                "In this section, you'll learn about bitwise operators and how to use them in Python."
            )
        with st.expander("Vocabulary Terms"):
            st.write(
                "Here are some vocabulary terms that you should be familiar with before diving into bitwise operations."
            )
        with st.expander("Study"):
            st.write(
                "Here are some resources you can use to study for the PCEP certification."
            )
        with st.expander("Quiz"):
            st.write("Test your knowledge with this quiz on bitwise operations.")
    elif selected_option == "Comprehensions":
        st.write("This section covers comprehensions in Python.")
        with st.expander("Intro to Comprehensions"):
            st.write(
                "In this section, you'll learn about list, dictionary, and set comprehensions in Python."
            )
        with st.expander("Vocabulary Terms"):
            st.write(
                "Here are some vocabulary terms that you should be familiar with before diving into comprehensions."
            )
        with st.expander("Study"):
            st.write(
                "Here are some resources you can use to study for the PCEP certification."
            )
        with st.expander("Quiz"):
            st.write("Test your knowledge with this quiz on comprehensions.")
    elif selected_option == "Recursive Functions":
        st.write("This section covers recursive functions in Python.")
        with st.expander("Intro to Recursive Functions"):
            st.write(
                "In this section, you'll learn about recursive functions and how to use them in Python."
            )
        with st.expander("Vocabulary Terms"):
            st.write(
                "Here are some vocabulary terms that you should be familiar with before diving into recursive functions."
            )
        with st.expander("Study"):
            st.write(
                "Here are some resources you can use to study for the PCEP certification."
            )
        with st.expander("Quiz"):
            st.write("Test your knowledge with this quiz on recursive functions.")
    elif selected_option == "Exceptions":
        st.write("This section covers exceptions in Python.")
        with st.expander("Intro to Exceptions"):
            st.write(
                "In this section, you'll learn about exceptions and how to handle them in Python."
            )
        with st.expander("Vocabulary Terms"):
            st.write(
                "Here are some vocabulary terms that you should be familiar with before diving into exceptions."
            )
        with st.expander("Study"):
            st.write(
                "Here are some resources you can use to study for the PCEP certification."
            )
        with st.expander("Quiz"):
            st.write("Test your knowledge with this quiz on exceptions.")
    elif selected_option == "Miscellaneous":
        st.write("This section covers miscellaneous topics in Python.")
        with st.expander("Intro to Miscellaneous"):
            st.write(
                "In this section, you'll learn about various topics that are important for the PCEP certification."
            )
        with st.expander("Vocabulary Terms"):
            st.write(
                "Here are some vocabulary terms that you should be familiar with before diving into miscellaneous topics."
            )
        with st.expander("Study"):
            st.write(
                "Here are some resources you can use to study for the PCEP certification."
            )
        with st.expander("Quiz"):
            st.write("Test your knowledge with this quiz on miscellaneous topics.")
    else:
        st.warning("Please select a valid topic.")
