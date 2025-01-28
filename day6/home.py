import streamlit as st

def home_page(navigate_to):
    """
    Displays the Home Page with an Enhanced UI and Navigation Button
    Args:
        navigate_to (function): Function to change the navigation state
    """
    # Enhanced Header Section
    st.markdown(
        """
        <div style="
            background: linear-gradient(90deg, #4CAF50, #2E8B57);
            padding: 30px;
            text-align: center;
            border-radius: 12px;
            color: white;">
            <h1 style="font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 2.5rem; margin-bottom: 10px;">
                Welcome to the Quiz Generator Platform
            </h1>
            <p style="font-size: 1.2rem; margin: 0;">
                Create, customize, and manage quizzes effortlessly!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Introductory Text
    st.markdown(
        """
        <div style="text-align: center; margin-top: 30px;">
            <p style="font-size: 1.1rem; line-height: 1.6; font-family: Arial, sans-serif;">
                This platform makes it simple to generate quizzes tailored to your needs.
                Click the button below to get started and unleash the power of interactive learning!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Centered Navigation Button
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <button style="
                background-color: #4CAF50;
                color: white;
                font-size: 1.2rem;
                padding: 12px 24px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-family: 'Helvetica Neue', Arial, sans-serif;">
                Go to Quiz Generator
            </button>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add navigation functionality for Streamlit button
    if st.button("Click here to Generate Quiz", key="navigate_button", help="Click to create your quiz"):
        navigate_to("Generate Quiz")
