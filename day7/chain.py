from prompt import quiz_generator_prompt
from model import create_chat_groq

"""
Function to generate a quiz
Args:
    topic (str): The topic of the quiz
    difficulty (str): Difficulty level of the quiz
    num_questions (int): Number of questions
Returns:
    str: The generated quiz content
"""

def generate_quiz(topic, difficulty, num_questions):
    prompt_template = quiz_generator_prompt()
    llm = create_chat_groq()
    
    chain = prompt_template | llm
    response = chain.invoke({
        "topic": topic,
        "difficulty": difficulty,
        "num_questions": num_questions
    })
    
    # If the response is plain text, you can split or process it further
    if isinstance(response.content, str):
        # Assuming each question is separated by a newline, you might split like this:
        questions = response.content.split("\n")  # This is just an example, adjust as per actual format
        
        # Process questions and options accordingly
        return questions  # List of questions and options
    else:
        return response.content



"""
Function to process an uploaded file (for example, a PDF) and store its contents
Args:
    file_path (str): The path to the uploaded file
Returns:
    str: Confirmation message or processing result
"""

def process_file(file_path):
    # You would implement file processing logic here (e.g., extracting text from PDF)
    # For now, it's a placeholder that assumes the file is processed successfully.
    return f"Processed file: {file_path}"
