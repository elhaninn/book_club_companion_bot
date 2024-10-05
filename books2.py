import requests

def fetch_book_details(book_title):
    # Google Books API endpoint
    google_books_api = f"https://www.googleapis.com/books/v1/volumes?q={book_title}"

    # Fetching data from Google Books API
    response = requests.get(google_books_api)
    data = response.json()

    if "items" in data:
        book = data['items'][0]['volumeInfo']

        # Extract book details
        title = book.get('title', 'No Title')
        authors = book.get('authors', ['Unknown Author'])
        description = book.get('description', 'No Description')

        # Extract cover image if available
        image_links = book.get('imageLinks', {})
        cover_image = image_links.get('thumbnail', '')

        return {
            'title': title,
            'authors': authors,
            'description': description,
            'cover_image': cover_image  # Add cover image URL
        }
    return None
