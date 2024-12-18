import React from "react";
import Graph from "../../components/Grafico";
import Filters from "../../components/Filtro";
import Table from "../../components/Tabela";
import ReturnBtn from "../../components/Voltar";
import GenerationBtn from "../../components/Gerar"

const FeedbackComponent = () => {
  return (
    <div className="flex flex-col lg:flex-row p-6 gap-8 bg-backgroundcolor min-h-screen">
      <ReturnBtn />
      <Graph />
      <div className="flex-1 lg:max-w-lg bg-white shadow-md rounded-lg p-6">
        <Filters />
        <Table />
        <div className="mt-4">
          <GenerationBtn />
        </div>
      </div>
    </div>
  );
};

export default FeedbackComponent;