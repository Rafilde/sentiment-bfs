import React from "react";

const Feedback = () => {
  return (
    <div className="flex items-center justify-between mb-4">
      <h2 className="text-2xl font-bold text-textcolor">
        Feedback Geral do Produto:
      </h2>
      <span className="text-sm font-bold text-red-600 bg-red-100 px-3 py-1 rounded-md">
        {/* Refatorar aqui para aparecer o maior feedback (seja negativo, positivo ou neutro) */}
        NEGATIVO
      </span>
    </div>
  );
};

export default Feedback;