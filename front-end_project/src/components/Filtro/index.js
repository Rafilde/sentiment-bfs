import React from 'react';

const Filters = () => {
  return (
    <div>
      <div className='mb-2'>
      <label htmlFor="product-select" className="block text-textcolor mb-2">Selecione destino inicial:</label>
        <select
          id="initial-destination"
          className="w-full border border-gray-300 rounded-md p-2 text-textcolor hover:border-primary focus:outline-none focus:ring focus:ring-primary"
        >
          <option>Sanduíche</option>
          <option>Salada</option>
          <option>Bebida</option>
        </select>
      </div>
      <div className='mb-4'>
      <label htmlFor="product-select" className="block text-textcolor mb-2">Selecione destino final:</label>
        <select
          id="final-destination"
          className="w-full border border-gray-300 rounded-md p-2 text-textcolor hover:border-primary focus:outline-none focus:ring focus:ring-primary"
        >
          <option>Sanduíche</option>
          <option>Salada</option>
          <option>Bebida</option>
        </select>
      </div>
    </div>
  );
};

export default Filters;