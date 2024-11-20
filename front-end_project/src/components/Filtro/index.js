import React from 'react';

const Filters = () => {
  return (
    <div className="mb-4">
      <label htmlFor="product-select" className="block text-textcolor mb-2">Selecione um produto:</label>
      <div className="flex gap-5">
        <select
          id="product-select"
          className="w-full border border-gray-300 rounded-md p-2 text-textcolor hover:border-primary focus:outline-none focus:ring focus:ring-primary"
        >
          <option>Sanduíche</option>
          <option>Salada</option>
          <option>Bebida</option>
        </select>

        <select
          id="filter-select"
          className="border border-gray-300 rounded-md p-2 text-textcolor hover:border-primary focus:outline-none focus:ring focus:ring-primary"
        >
          <option>Todos</option>
          <option>Positivo</option>
          <option>Negativo</option>
          <option>Neutro</option>
        </select>
      </div>
    </div>
  );
};

export default Filters;