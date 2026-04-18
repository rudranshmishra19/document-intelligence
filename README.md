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

## Screenshots

## Book List
<img width="937" height="450" alt="Book_intelligence" src="https://github.com/user-attachments/assets/2595c6c8-7a80-4f74-8891-d0114d120144" />
## Book Description
<img width="828" height="458" alt="book_intelligence01" src="https://github.com/user-attachments/assets/b170bff6-fc9b-4a88-9c94-4389b8b35e1c" />
## Q&A Page
<img width="854" height="440" alt="book_intelligence_Qa" src="https://github.com/user-attachments/assets/9a7dd7fe-992e-48a3-be12-64ee1b4e9ca0" />

