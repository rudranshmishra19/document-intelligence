import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';

export default function BookDetail() {
  const { id } = useParams();
  const [book, setBook] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/api/books/${id}/`)
      .then(res => setBook(res.data));
    axios.get(`http://127.0.0.1:8000/api/books/${id}/recommend/`)
      .then(res => setRecommendations(res.data));
  }, [id]);

  if (!book) return <div className="text-center mt-20 text-xl">Loading...</div>;

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-3xl mx-auto">
        <button onClick={() => navigate('/')}
          className="mb-6 text-blue-600 hover:underline">← Back to Books</button>
        <div className="bg-white rounded-xl shadow p-8">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">{book.title}</h1>
          <p className="text-gray-500 mb-1">Author: {book.author}</p>
          <p className="text-yellow-500 mb-1">⭐ {book.rating}/5</p>
          <p className="text-blue-500 mb-1">Genre: {book.genre || 'N/A'}</p>
          <p className="text-green-600 font-semibold mb-4">Price: {book.price}</p>
          <p className="text-gray-500 mb-4">Availability: {book.availability}</p>

          {book.summary && (
            <div className="bg-blue-50 rounded-lg p-4 mb-4">
              <h3 className="font-bold text-blue-800 mb-2">AI Summary</h3>
              <p className="text-gray-700">{book.summary}</p>
            </div>
          )}

          {book.description && (
            <div className="mb-4">
              <h3 className="font-bold text-gray-800 mb-2">Description</h3>
              <p className="text-gray-600">{book.description}</p>
            </div>
          )}

          <a href={book.book_url} target="_blank" rel="noreferrer"
            className="inline-block bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
            View Book →
          </a>
        </div>

        {recommendations.length > 0 && (
          <div className="mt-8">
            <h2 className="text-xl font-bold text-gray-800 mb-4">You might also like</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {recommendations.map(rec => (
                <div key={rec.id} onClick={() => navigate(`/books/${rec.id}`)}
                  className="bg-white rounded-lg shadow p-4 cursor-pointer hover:shadow-lg transition">
                  <h3 className="font-semibold text-gray-800">{rec.title}</h3>
                  <p className="text-sm text-blue-500">{rec.genre}</p>
                  <p className="text-sm text-yellow-500">⭐ {rec.rating}/5</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}