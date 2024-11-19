import React from 'react';

const ReturnBtn = () => {
  return (
    <a
      className="flex items-center px-4 py-2 bg-secondary text-white font-semibold rounded-lg hover:bg-primary shadow-md hover:shadow-lg transition-all duration-300 ease-in-out"
      href="/"
      aria-label="Voltar"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        className="h-6 w-6 mr-2"
        fill="none"
        stroke="currentColor"
        strokeWidth="3"
      >
        <path d="M19 12H5" />
        <polyline points="12 19 5 12 12 5" />
      </svg>
      Voltar
    </a>
  );
};

export default ReturnBtn;