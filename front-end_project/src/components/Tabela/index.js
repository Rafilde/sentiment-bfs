import React from 'react';

const Table = () => {
  const exampleText = `Este é um exemplo de texto recebido da API. Ele pode conter várias informações úteis para o usuário. Este texto simula como ficará a interface quando os dados reais forem integrados.
  
  Este é um exemplo de texto recebido da API. Ele pode conter várias informações úteis para o usuário. Este texto simula como ficará a interface quando os dados reais forem integrados.

  Este é um exemplo de texto recebido da API. Ele pode conter várias informações úteis para o usuário. Este texto simula como ficará a interface quando os dados reais forem integrados.

  Este é um exemplo de texto recebido da API. Ele pode conter várias informações úteis para o usuário. Este texto simula como ficará a interface quando os dados reais forem integrados.
  
  PAPOCOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO`;

  return (
    <div className="border border-gray-200 rounded-lg shadow-sm mt-4">
      <h3 className="text-lg font-semibold text-textcolor my-4 ml-4">Comentários</h3>
      <hr className="border-t border-gray-200" />
      <div className="space-y-2 max-h-[400px] overflow-y-auto px-4 py-2">
        <div className="border-b border-gray-200 pb-2">
          <p className="text-textcolor">{exampleText}</p>
        </div>
      </div>
    </div>
  );
};

export default Table;
