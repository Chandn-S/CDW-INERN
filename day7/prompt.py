from langchain import hub
from langchain_core.prompts import ChatPromptTemplate

def quiz_generator_prompt():
    """
    Generates a Prompt template for the quiz generator
    Returns:
        ChatPromptTemplate -> Configured ChatPromptTemplate instance
    """
    system_msg = """
                You are a highly intelligent quiz generator. Your task is to generate quizzes based on any requested question.
                Guidelines:
                1. Provide multiple-choice questions with 4 options, one of which is the correct answer.
                2. The output must be formatted as follows:
                   - Each question followed by 4 options, listed vertically (one per line).
                   - After the options, indicate the correct answer in the format:
                     'Correct Answer: Option [X]'
                   Example:
                     Q1: What is the capital of France?
                     a) Berlin
                     b) Madrid
                     c) Paris
                     d) Rome
                     Correct Answer: Option c
                3. Respond to queries requesting questions in a structured format, no additional explanations.
                4. If the query is unrelated to quiz generation, respond with: 
                   "I am a quiz assistant. Please ask me a quiz-related query."
                Note: The number of questions can vary based on user needs.
                """
    
    user_msg = "Generate a quiz with multiple-choice questions."
    
    prompt_template = ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])
    return prompt_template

def quiz_generator_prompt_from_hub(template="naan-dhan-da-poem-generator/rag_quiz"):
    """
    Generates Prompt template from the LangSmith prompt hub
    Returns:
        ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub
    """
    prompt_template = hub.pull(template)
    return prompt_template