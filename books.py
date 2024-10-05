import requests
import streamlit as st

def fetch_book_details(title):
    # Ensure the title is provided
    if not title:
        st.error("Please enter a valid book title.")
        return None
    
    # Format the API URL
    api_url = f"https://www.googleapis.com/books/v1/volumes?q={title}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses

        data = response.json()

        # Check if books were found
        if "items" in data:
            book_info = data["items"][0]["volumeInfo"]
            return {
                "title": book_info.get("title", "Unknown"),
                "authors": book_info.get("authors", ["Unknown"]),
                "description": book_info.get("description", "No description available."),
            }
        else:
            st.error(f"No results found for the book title '{title}'.")
            return None

    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        st.error(f"An error occurred: {err}")

    return None

