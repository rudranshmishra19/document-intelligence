import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function BookList() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/books/')
      .then(res => { setBooks(res.data); setLoading(false); })
      .catch(err => { console.error(err); setLoading(false); });
  }, []);

  if (loading) return <div className="text-center mt-20 text-xl">Loading books...</div>;

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-6xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold text-gray-800">📚 Book Intelligence</h1>
          <button onClick={() => navigate('/qa')}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
            Ask AI Questions
          </button>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {books.map(book => (
            <div key={book.id} onClick={() => navigate(`/books/${book.id}`)}
              className="bg-white rounded-xl shadow p-5 cursor-pointer hover:shadow-lg transition">
              <h2 className="font-bold text-lg text-gray-800 mb-2">{book.title}</h2>
              <p className="text-sm text-gray-500 mb-1">⭐ {book.rating}/5</p>
              <p className="text-sm text-blue-500 mb-2">{book.genre || 'Genre N/A'}</p>
              <p className="text-sm text-gray-600 line-clamp-3">{book.description || 'No description available'}</p>
              <p className="text-sm font-semibold text-green-600 mt-3">{book.price}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}