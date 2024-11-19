import React from 'react';
import ReactDOM from 'react-dom/client';
import RouterController from './controllers/routerController';
import './views/styles/global.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterController />
  </React.StrictMode>
);