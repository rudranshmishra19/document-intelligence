from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/recommend/', views.recommend_books, name='recommend'),
    path('books/upload/', views.upload_book, name='upload'),
    path('books/ask/', views.ask_question, name='ask'),
]