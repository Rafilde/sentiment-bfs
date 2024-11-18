import React from 'react';
import ReactDOM from 'react-dom/client';
import './views/styles/global.css';
import App from './views/pages/main';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);