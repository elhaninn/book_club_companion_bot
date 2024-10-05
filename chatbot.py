import subprocess

# Function to call the Ollama model using subprocess and pass a prompt
def generate_response_with_ollama(prompt):
    try:
        # Use subprocess to call ollama command-line tool
        result = subprocess.run(
            ["ollama", "run", "llama3.2", prompt], 
            input=prompt,
            text=True,
            capture_output=True,
            check=True,
            encoding='utf-8'
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error generating response with Ollama: {e}"

# Function to generate a personalized response based on user query and book details
def get_personalized_response(book_info, user_question):
    # Construct a detailed prompt
    prompt = f"""
    You are an expert on books. 
    I am reading a book titled '{book_info['title']}' by {book_info['authors']}. 
    The description of the book is: {book_info['description']}.

    Here's a question I have about the book: {user_question}.
    
    Please provide a detailed and thoughtful response.
    """

    # Call the Ollama model and generate the response
    response = generate_response_with_ollama(prompt)
    return response




    
    
