import requests
from bs4 import BeautifulSoup
from django.conf import settings
import anthropic
import time

BASE_URL = "https://books.toscrape.com/"

RATING_MAP = {
    'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
}

def get_book_description(book_url):
    try:
        response = requests.get(book_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        desc = soup.find('div', id='product_description')
        if desc:
            return desc.find_next_sibling('p').text.strip()
        return None
    except:
        return None

def generate_ai_insights(title, description):
    try:
        import google.generativeai as genai
        from django.conf import settings
        
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Book Title: {title}
        Description: {description or 'No description available'}
        
        Please provide:
        1. SUMMARY: A 2-3 sentence summary of this book
        2. GENRE: Single genre classification (e.g., Fiction, Mystery, Romance, Science Fiction, Self-Help, History)
        
        Respond in exactly this format:
        SUMMARY: <your summary here>
        GENRE: <single genre here>
        """
        
        response = model.generate_content(prompt)
        response_text = response.text
        summary = ""
        genre = ""
        
        for line in response_text.split('\n'):
            if line.startswith('SUMMARY:'):
                summary = line.replace('SUMMARY:', '').strip()
            elif line.startswith('GENRE:'):
                genre = line.replace('GENRE:', '').strip()
        
        return summary, genre
    except Exception as e:
        print(f"AI error: {e}")
        return None, None

def scrape_books(max_pages=5):
    from books.models import Book
    
    books_scraped = 0
    page = 1
    
    while page <= max_pages:
        if page == 1:
            url = BASE_URL
        else:
            url = f"{BASE_URL}catalogue/page-{page}.html"
        
        print(f"Scraping page {page}...")
        
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            book_list = soup.find_all('article', class_='product_pod')
            
            if not book_list:
                break
                
            for book in book_list:
                try:
                    # Title
                    title = book.find('h3').find('a')['title']
                    
                    # Book detail URL
                    relative_url = book.find('h3').find('a')['href']
                    if 'catalogue/' in relative_url:
                        book_url = BASE_URL + relative_url
                    else:
                        book_url = BASE_URL + 'catalogue/' + relative_url
                    
                    # Rating
                    rating_word = book.find('p', class_='star-rating')['class'][1]
                    rating = RATING_MAP.get(rating_word, 0)
                    
                    # Price
                    price = book.find('p', class_='price_color').text.strip()
                    
                    # Availability
                    availability = book.find('p', class_='availability').text.strip()
                    
                    # Skip if already exists
                    if Book.objects.filter(title=title).exists():
                        continue
                    
                    # Get description from detail page
                    description = get_book_description(book_url)
                    
                    # Generate AI insights
                    print(f"  Generating AI insights for: {title}")
                    summary, genre = generate_ai_insights(title, description)
                    
                    # Save to DB
                    Book.objects.create(
                        title=title,
                        author="Unknown",  # books.toscrape.com doesn't have authors
                        rating=rating,
                        description=description,
                        summary=summary,
                        genre=genre,
                        book_url=book_url,
                        price=price,
                        availability=availability,
                    )
                    
                    books_scraped += 1
                    print(f"  Saved: {title}")
                    time.sleep(0.5)  # be polite to the server
                    
                except Exception as e:
                    print(f"  Error scraping book: {e}")
                    continue
                    
        except Exception as e:
            print(f"Page error: {e}")
            break
            
        page += 1
    
    print(f"\nDone! Scraped {books_scraped} books.")
    return books_scraped