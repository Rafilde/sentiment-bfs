import React from 'react';

const GenerationBtn = () => {
  return (
    <button
      className="flex items-center px-4 py-2 w-full bg-secondary text-white font-semibold rounded-lg hover:bg-primary shadow-md hover:shadow-lg transition-all duration-300 ease-in-out"
      onClick={() => alert('Botão de gerar clicado!')}
      aria-label="Gerar"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        className="h-6 w-6 mr-2"
        fill="none"
        stroke="currentColor"
        strokeWidth="3"
      >
        <path d="M5 12h14" />
        <polyline points="12 5 19 12 12 19" />
      </svg>
      Gerar
    </button>
  );
};

export default GenerationBtn;
