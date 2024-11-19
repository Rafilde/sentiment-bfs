import React from "react";
import Graph from "../../components/Grafico";
import Filters from "../../components/Filtro";
import Table from "../../components/Tabela";
import Feedback from "../../components/Feedback";
import ReturnBtn from "../../components/Voltar";

const FeedbackComponent = () => {
  return (
    <div className="flex flex-col lg:flex-row p-6 gap-8 bg-backgroundcolor min-h-screen">
      <ReturnBtn />
      <Graph />
      <div className="flex-1 lg:max-w-lg bg-white shadow-md rounded-lg p-6">
        <Feedback />
        <Filters />
        <Table />
      </div>
    </div>
  );
};

export default FeedbackComponent;