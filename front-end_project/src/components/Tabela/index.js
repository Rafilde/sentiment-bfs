import React from 'react';

const Table = () => {
  return (
    <div className="border border-gray-200 rounded-lg shadow-sm mt-4">
      <h3 className="text-lg font-semibold text-textcolor my-4 ml-4">Comentários</h3>
      <hr className="border-t border-gray-200"/>
      <div className="space-y-2 max-h-[400px] overflow-y-auto px-4 py-2">
        {Array.from({ length: 40 }).map((_, index) => (
          <div
            key={index}
            className="border-b border-gray-200 pb-2"
          >
            <p className="text-textcolor">Item Teste: {index}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Table;