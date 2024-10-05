import streamlit as st
from books2 import fetch_book_details
from chatbot import get_personalized_response
import time 

st.image("images\\novel.jpg", caption=None, use_column_width=True)
# Step 1: User input for the book title
book_title = st.text_input("Enter the book title:")

# Step 2: Button to fetch book details
if st.button("Get Book Details"):
    book_info = fetch_book_details(book_title)
    if book_info:
        st.write(f"**Title**: {book_info['title']}")
        st.write(f"**Author**: {book_info['authors']}")
        st.write(f"**Description**: {book_info['description']}")
        if book_info.get('cover_image'):
            st.image(book_info['cover_image'], caption=f"Cover of {book_info['title']}", use_column_width=True)

        # Store the book info in session state for later use
        st.session_state.book_info = book_info
        
        # Display the question input and Ask button
        

    else:
        st.write("No details found for this book.")

# This section ensures the Ask button is always available
if 'book_info' in st.session_state:
    # If book_info is present in session state, show the question input and Ask button
    st.subheader("Ask a personalized question about the book:")
    user_question = st.text_input("Enter your question:", key="question_ask")

    if st.button("Ask"):
        if user_question:
            # Display progress bar while waiting for response
            progress_bar = st.progress(0)
            max_wait_time = 120  # Maximum wait time in seconds
            wait_interval = 2  # Update interval in seconds
            
            # Update progress bar over time
            for i in range(0, max_wait_time, wait_interval):
                progress_bar.progress((i + wait_interval) / max_wait_time)
                time.sleep(wait_interval)

            response = get_personalized_response(st.session_state.book_info, user_question)
            st.write(f"**Answer**: {response}")
        else:
            st.write("Please enter a question.")




