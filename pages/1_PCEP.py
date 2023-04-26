import streamlit as st
import streamlit.components.v1 as components
import streamlit_analytics

from utils.constants import SECTIONS
from utils.utils import *

with streamlit_analytics.track():
    st.header("PCEP Certification")
    options = [section for section in SECTIONS]
    selected_option = st.selectbox("Select a topic", options)
    if selected_option == "Intro To PCEP":
        st.write("This section provides an introduction to PCEP.")

        st.video("https://www.youtube.com/embed/8qG463VRPjI?wmode=opaque")

    elif selected_option == "Numbering Systems":
        st.write(SECTIONS[selected_option]["description"])
        with st.expander(f"Intro to {selected_option}"):
            st.write(SECTIONS[selected_option]["intro_text"])

            st.video("https://www.youtube.com/embed/FFDMzbrEXaE?wmode=opaque")

        generate_vocab_terms(selected_option)

        with st.expander("Study"):
            st.write(SECTIONS[selected_option]["study_resources"]["intro_text"])
            # with elements("study"):
            #     html.iframe(
            #         src="https://quizlet.com/662948012/learn/embed?i=489qnu&x=1jj1",
            #         height="550",
            #         width="100%",
            #     )
            components.iframe(
                "https://quizlet.com/662948012/learn/embed?i=489qnu&x=1jj1",
                height=550,
                width=670,
            )

        generate_quiz(selected_option=selected_option)

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
