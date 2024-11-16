export async function fetchData() {
    try {
      const response = await fetch(''); //Definir caminho de consumo!
      if (!response.ok) throw new Error('Erro ao buscar os dados');
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Erro:', error);
      throw error;
    }
  }
  