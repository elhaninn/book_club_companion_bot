import streamlit as st
from books2 import fetch_book_details
from chatbot import get_personalized_response
import time

# Title and theme image
st.title("Book Club Companion Chatbot")
st.image("images\\novel.jpg", caption=None, use_column_width=True)

# Step 1: User input for the book title
book_title = st.text_input("Enter the book title:")

# Step 2: Button to fetch book details
if st.button("Get Book Details"):
    book_info = fetch_book_details(book_title)
    if book_info:
        # Display cover image if available
        if book_info.get('cover_image'):
            st.image(book_info['cover_image'], caption=f"Cover of {book_info['title']}", use_column_width=True)
        
        st.write(f"**Title**: {book_info['title']}")
        st.write(f"**Author**: {', '.join(book_info['authors'])}")
        st.write(f"**Description**: {book_info['description']}")

        # Store the book info in session state for later use
        st.session_state.book_info = book_info
        
        # Initialize conversation history in session state
        if 'conversation_history' not in st.session_state:
            st.session_state.conversation_history = []

        # Display conversation history
        st.subheader("Conversation History:")
        for entry in st.session_state.conversation_history:
            st.write(f"**User**: {entry['question']}")
            st.write(f"**Bot**: {entry['response']}")

        # Step 3: User asks personalized questions
        user_question = st.text_input("Enter your question:", key="question_ask")

        # Display the Ask button
        if st.button("Ask"):
            if user_question:
                # Simulate waiting for response (replace with actual model call later)
                progress_bar = st.progress(0)
                max_wait_time = 2  # Simulating a 2-second wait time
                
                for i in range(max_wait_time):
                    time.sleep(1)  # Simulate the wait time
                    progress_bar.progress((i + 1) / max_wait_time)
                
                # Generate personalized response using LLaMA
                response = get_personalized_response(st.session_state.book_info, user_question)
                
                # Append the new question and response to the conversation history
                st.session_state.conversation_history.append({
                    'question': user_question,
                    'response': response
                })
                
                # Display the updated conversation history
                st.write(f"**Answer**: {response}")
            else:
                st.write("Please enter a question.")
    else:
        st.image("https://via.placeholder.com/800x400?text=No+Book+Details+Found", caption="Book details not found!", use_column_width=True)
        st.write("No details found for this book.")

# This section ensures the Ask button is always available
if 'book_info' in st.session_state and 'conversation_history' in st.session_state:
    # Display conversation history
    st.subheader("Conversation History:")
    for entry in st.session_state.conversation_history:
        st.write(f"**User**: {entry['question']}")
        st.write(f"**Bot**: {entry['response']}")

    # If book_info is present in session state, show the question input and Ask button
    user_question = st.text_input("Enter your next question:", key="question_ask_repeated")

    if st.button("Ask Again"):
        if user_question:
            # Simulate waiting for response (replace with actual model call later)
            progress_bar = st.progress(0)
            max_wait_time = 2  # Simulating a 2-second wait time
            
            for i in range(max_wait_time):
                time.sleep(1)  # Simulate the wait time
                progress_bar.progress((i + 1) / max_wait_time)

            # Generate personalized response using LLaMA
            response = get_personalized_response(st.session_state.book_info, user_question)
            
            # Append the new question and response to the conversation history
            st.session_state.conversation_history.append({
                'question': user_question,
                'response': response
            })
            
            # Display the updated conversation history
            st.write(f"**Answer**: {response}")
        else:
            st.write("Please enter a question.")
