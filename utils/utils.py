import streamlit as st
import streamlit.components.v1 as components

from utils.constants import SECTIONS


def generate_quiz(selected_option: str) -> None:
    with st.expander("Quiz"):
        st.write(f"Test your knowledge with this quiz on {selected_option}.")
        with st.form(f"{selected_option} quiz", clear_on_submit=False):
            # iterate over each question and display it to the user
            for i, question in enumerate(SECTIONS[selected_option]["quiz_questions"]):
                selected = st.radio(
                    f"{i + 1}. {question['question']}", question["choices"]
                )
                st.session_state[f"question_{i}"] = selected

            # add a submit button for the form
            submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Quiz Submitted!")
            num_correct = 0
            # iterate over each question and print the selected choice
            for i, question in enumerate(SECTIONS[selected_option]["quiz_questions"]):
                selected = st.session_state[f"question_{i}"]
                correct = question["correct_answer"][0]
                st.write(
                    f"{i + 1}. {question['question']}: {'✅' if selected == correct else '❌'}"
                )
                if selected == correct:
                    num_correct += 1
                else:
                    st.write(question["explanation"])
            # show the final score
            st.write(
                f"Final score: {num_correct}/{len(SECTIONS[selected_option]['quiz_questions'])}"
            )


# UNDER CONTRUCTION
def generate_study_guide(selected_option: str) -> None:
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


def generate_vocab_terms(selected_option: str) -> None:
    with st.expander("Vocabulary Terms"):
        for vocab in SECTIONS[selected_option]["vocabulary_terms"]:
            st.write(f"**_:green[{vocab['term']}]_**: {vocab['definition']}")
