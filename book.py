import requests

def fetch_book_details(title):
    api_url = f"https://www.googleapis.com/books/v1/volumes?q={title}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            book_info = data["items"][0]["volumeInfo"]
            return {
                "title": book_info.get("title", "Unknown"),
                "authors": book_info.get("authors", ["Unknown"]),
                "description": book_info.get("description", "No description available."),
            }
    return None
