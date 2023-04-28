import json

import streamlit as st
import streamlit.components.v1 as components
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from utils.constants import SECTIONS

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)


class MyCustomForm(stauth.Authenticate):
    def register_user(self, form_name: str, location: str='main', preauthorization=True) -> bool:
        """
        Creates a password reset widget.
        Parameters
        ----------
        form_name: str
            The rendered name of the password reset form.
        location: str
            The location of the password reset form i.e. main or sidebar.
        preauthorization: bool
            The preauthorization requirement, True: user must be preauthorized to register, 
            False: any user can register.
        Returns
        -------
        bool
            The status of registering the new user, True: user registered successfully.
        """
        if preauthorization:
            if not self.preauthorized:
                raise ValueError("preauthorization argument must not be None")
        if location not in ['main', 'sidebar']:
            raise ValueError("Location must be one of 'main' or 'sidebar'")
        if location == 'main':
            register_user_form = st.form('Register user')
        elif location == 'sidebar':
            register_user_form = st.sidebar.form('Register user')

        register_user_form.subheader(form_name)
        new_email = register_user_form.text_input('Email')
        new_username = register_user_form.text_input('Username').lower()
        new_name = register_user_form.text_input('School Name').lower()
        new_password = register_user_form.text_input('Password', type='password')
        new_password_repeat = register_user_form.text_input('Repeat password', type='password')
        # rest of the code from the original register_user method

        return True

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
            quiz_data = {}
            num_correct = 0
            with open("static/user_data.json", "r") as json_file:
                data = json.load(json_file)
                quiz_data = data
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

                # update json file
                if selected_option not in quiz_data:
                    quiz_data[selected_option] = {}

                if selected not in quiz_data[selected_option]:
                    quiz_data[selected_option][selected] = 0
                else:
                    quiz_data[selected_option][selected] += 1
            # show the final score
            st.write(
                f"Final score: {num_correct}/{len(SECTIONS[selected_option]['quiz_questions'])}"
            )

            if num_correct/len(SECTIONS[selected_option]['quiz_questions']) * 100 > 75:
                st.balloons()

            data = quiz_data

            with open("static/user_data.json", "w") as json_file:
                json.dump(data, json_file)


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


def login():
    pass


def create_new_user():
    with st.expander("First Time?"):
        try:
            if authenticator.register_user("Register user", preauthorization=False):
                st.success("User registered successfully")
                with open('config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
        except Exception as e:
            st.error(e)


def create_new_password():
    with st.expander("Forgot your password?"):
        try:
            (
                username_forgot_pw,
                email_forgot_password,
                random_password,
            ) = authenticator.forgot_password("Forgot password")
            if username_forgot_pw:
                st.success("New password sent securely")
                # Random password to be transferred to user securely
                with open('config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
            else:
                st.error("Username not found")
        except Exception as e:
            st.error(e)


def create_new_username():
    with st.expander("Forgot your username?"):
        try:
            (
                username_forgot_username,
                email_forgot_username,
            ) = authenticator.forgot_username("Forgot username")
            if username_forgot_username:
                st.success("Username sent securely")
                # Username to be transferred to user securely
            else:
                st.error("Email not found")
        except Exception as e:
            st.error(e)
