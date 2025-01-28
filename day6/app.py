from dotenv import load_dotenv
import chain
import streamlit as st

load_dotenv()

def poem_generator_app():
    # This function creates a simple Streamlit app for generating poems based on a user-provided topic.
    # It contains the following steps:
    # 1. A form is created using Streamlit's `st.form` method with the identifier "poem_generating_form".
    # 2. Inside the form, a text input field is added for the user to specify the topic of the poem.
    # 3. A submit button is included in the form, which, when clicked, triggers the form submission.
    # 4. On form submission, the `generate_poem` method from the `chain` object is called with the provided topic.
    # 5. The response, which is the generated poem, is displayed in the app using Streamlit's `st.write` function.
    with st.form("poem_generating_form"):
        topic = st.text_input("enter the poem topic")
        submitted = st.form_submit_button("Generate Poem")
        if submitted:
            response = chain.generate_poem(topic)
            st.write(response)


poem_generator_app()