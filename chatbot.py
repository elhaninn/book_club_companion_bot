from transformers import LlamaForCausalLM, LlamaTokenizer

# Load pre-trained LLaMA model and tokenizer
def load_llama_model():
    model_name = "meta-llama/Llama-3.2-1B"  
    model = LlamaForCausalLM.from_pretrained(model_name)
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    return model, tokenizer

# Function to generate a personalized response based on user query and book details
def get_personalized_response(book_info, user_question):
    model, tokenizer = load_llama_model()
    
    # Construct a prompt using the book details and user's question
    prompt = f"""
    I am reading a book titled "{book_info['title']}" by {book_info['authors']}. 
    Here is the description of the book: {book_info['description']}
    
    Question: {user_question}
    """
    
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response
