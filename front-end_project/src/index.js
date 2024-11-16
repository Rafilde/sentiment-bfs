import React from 'react';
import ReactDOM from 'react-dom/client';
import './views/styles/index.css';
import App from './views/pages/App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);