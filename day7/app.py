import streamlit as st
from dotenv import load_dotenv
import chain
from upload import upload_page

load_dotenv()

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Quiz Generator", "File Upload"])

def generate_quiz_page():
    """
    Displays the Quiz Generator Form with Multi-Query Mode support.
    """
    st.markdown(
        """
        <div style="background-color: #4CAF50; padding: 20px; text-align: center; border-radius: 10px; color: white;">
            <h1 style="font-family: Arial, sans-serif;">Quiz Generator</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    multi_query_mode = st.checkbox("Enable Multi-Query Mode", help="Generate quizzes for multiple combinations")

    if multi_query_mode:
        st.info("Multi-Query Mode Enabled: Add multiple combinations below")
        num_queries = st.number_input("How many queries do you want to add?", min_value=1, max_value=10, step=1)
        queries = []

        for i in range(num_queries):
            st.markdown(f"### Query {i + 1}")
            topic = st.selectbox(f"Topic (Query {i + 1})", ["English", "Math", "Science", "Social"], key=f"topic_{i}")
            difficulty = st.selectbox(f"Difficulty (Query {i + 1})", ["Easy", "Medium", "Hard"], key=f"difficulty_{i}")
            num_questions = st.number_input(
                f"Number of Questions (Query {i + 1})", min_value=1, max_value=50, step=1, key=f"num_questions_{i}"
            )
            queries.append((topic, difficulty, num_questions))

        if st.button("Generate All Quizzes", help="Click to generate quizzes for all combinations"):
            with st.spinner("Generating quizzes..."):
                for idx, (topic, difficulty, num_questions) in enumerate(queries):
                    st.markdown(f"#### Quiz {idx + 1}")
                    response = chain.generate_quiz(topic, difficulty, num_questions)
                    st.info(response)

    else:
        with st.form("quiz_generator"):
            topic = st.selectbox("Select the Topic for the Quiz", ["English", "Math", "Science", "Social"])
            difficulty = st.selectbox("Select Difficulty Level", ["Easy", "Medium", "Hard"])
            num_questions = st.number_input("Enter the Number of Questions", min_value=1, max_value=50, step=1)
            submitted = st.form_submit_button("Submit", help="Click to generate your quiz!")
            
            if submitted:
                with st.spinner("Generating your quiz..."):
                    response = chain.generate_quiz(topic, difficulty, num_questions)
                    st.success("Quiz Generated Successfully!")
                    st.info(response)

if page == "Home":
    from home import home_page  # Import here to avoid circular import
    home_page(navigate_to=None)  # Pass 'None' or a relevant function
elif page == "Quiz Generator":
    generate_quiz_page()
elif page == "File Upload":
    upload_page()
