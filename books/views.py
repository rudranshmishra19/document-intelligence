from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics


class BookListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset =Book.objects.all()
    serializer_class=BookSerializer

@api_view(['GET'])
def recommend_books(request,pk):
    try:
        book = Book.objects.get(pk=pk)
        related=Book.objects.filter(genre=book.genre).exclude(pk=pk)[:5]
        serializer=BookSerializer(related,many=True)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({'error':'Book not found'},status=404)

@api_view(['POST'])
def upload_book(request):
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors,status=400)

@api_view(['POST'])
def ask_question(request):
    question=request.data.get('question', '')
    book_id = request.data.get('book_id', None)

    if not question:
        return Response({'error':'Question is required'},status=400)
    #Get relevant books
    if book_id:
        books=Book.objects.filter(pk=book_id)
    else:
        books=Book.objects.all()[:10]

    context = ""
    for book in books:
         context += f"Title: {book.title}\nSummary: {book.summary}\nGenre: {book.genre}\nDescription: {book.description}\n\n"
    #Generate answer using Gemini
    try:
        import google.generativeai as genai
        from django.conf import settings
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model=genai.GenerativeModel('gemini-2.0-flash')

        prompt=f"""Based on the following books,answer this question: {question}

Books context:
{context}

Provide a helpful answer with book references."""
        response = model.generate_content(prompt)
        return Response({'answer':response.text,'question': question})
    except Exception as e:
        return Response({'answer':'AI service unavailable','question':question})
    

    