from model import create_chat_groq
import prompts
def generate_poem(topic):
    """
    This function generates an 8-line poem by invoking a GROQ-based language model.
    
    Steps:
    1. Creates a ChatGroq instance using the `create_chat_groq` function.
    2. Sends a prompt to the model to generate an 8-line poem.
    3. Returns the model's response content.
    
    Returns:
        str: The content of the generated poem returned by the model.
    """
    prompt_template = prompts.poem_generator_prompt_from_hub()
    llm= create_chat_groq()
    chain = prompt_template | llm
    response = chain.invoke({"topic": topic})
    return response.content