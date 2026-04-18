# 📚 Document Intelligence Platform

A full-stack web application with AI integration that processes book data and enables intelligent querying.

## 🚀 Features
- Automated book scraping from books.toscrape.com
- AI-powered summaries and genre classification (Google Gemini)
- RAG-based question answering over books
- REST APIs with Django REST Framework
- React frontend with Tailwind CSS

## 🛠️ Tech Stack
- **Backend:** Django REST Framework, Python
- **Database:** Postgresql
- **AI:** Google Gemini API
- **Frontend:** ReactJS, Tailwind CSS
- **Scraping:** BeautifulSoup, Requests

## ⚙️ Setup Instructions

### Backend
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Configure `core/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgres',
        'NAME': 'book_intelligence',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
GEMINI_API_KEY = 'your_gemini_api_key'
```

```bash
python manage.py migrate
python manage.py scrape_books
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## 📡 API Documentation

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/books/ | List all books |
| GET | /api/books/{id}/ | Get book detail |
| GET | /api/books/{id}/recommend/ | Get recommendations |
| POST | /api/books/upload/ | Upload a book |
| POST | /api/books/ask/ | Ask AI question |

## 💬 Sample Questions
- "Recommend me a mystery book"
- "What books are about love?"
- "Which book has the highest rating?"



