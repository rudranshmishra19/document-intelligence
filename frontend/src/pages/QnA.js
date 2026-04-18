import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function QnA() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const askQuestion = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer('');
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/books/ask/', {
        question: question
      });
      setAnswer(res.data.answer);
    } catch (err) {
      setAnswer('Error getting answer. Please try again.');
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-3xl mx-auto">
        <button onClick={() => navigate('/')}
          className="mb-6 text-blue-600 hover:underline">← Back to Books</button>
        <div className="bg-white rounded-xl shadow p-8">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">🤖 Ask AI</h1>
          <p className="text-gray-500 mb-6">Ask anything about the books in our library</p>

          <textarea
            value={question}
            onChange={e => setQuestion(e.target.value)}
            placeholder="e.g. Recommend me a mystery book. What is Harry Potter about?"
            className="w-full border border-gray-300 rounded-lg p-4 h-32 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 mb-4"
          />

          <button onClick={askQuestion} disabled={loading}
            className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 disabled:opacity-50 font-semibold">
            {loading ? 'Thinking...' : 'Ask Question'}
          </button>

          {answer && (
            <div className="mt-6 bg-green-50 rounded-lg p-6">
              <h3 className="font-bold text-green-800 mb-2">AI Answer</h3>
              <p className="text-gray-700 whitespace-pre-wrap">{answer}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}