import streamlit as st
from books import fetch_book_details
from chatbot import get_personalized_response

st.title("Book Club Companion Chatbot")

# Step 1: User input for the book title
book_title = st.text_input("Enter the book title:")

if st.button("Get Book Details"):
    book_info = fetch_book_details(book_title)
    if book_info:
        st.write(f"**Title**: {book_info['title']}")
        st.write(f"**Author**: {book_info['authors']}")
        st.write(f"**Description**: {book_info['description']}")

        # Step 2: User asks personalized questions
        st.subheader("Ask a personalized question about the book:")
        user_question = st.text_input("Enter your question:")
        
        if st.button("Ask"):
            if user_question:
                # Generate personalized response using LLaMA
                response = get_personalized_response(book_info, user_question)
                st.write(f"**Answer**: {response}")
            else:
                st.write("Please enter a question.")
    else:
        st.write("No details found for this book.")
