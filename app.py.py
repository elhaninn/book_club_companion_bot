import streamlit as st
from chatbot import start_chatbot
from books import fetch_book_details
from questions import suggest_discussion_questions

st.title("Book Club Companion Chatbot")

# User input: Book title
book_title = st.text_input("Enter the book title:")

if st.button("Get Book Details"):
    book_info = fetch_book_details(book_title)
    st.write(f"Title: {book_info['title']}")
    st.write(f"Author: {book_info['authors']}")
    st.write(f"Description: {book_info['description']}")

    questions = suggest_discussion_questions(book_info['title'])
    st.write("Discussion Questions:")
    for q in questions:
        st.write(f"- {q}")
