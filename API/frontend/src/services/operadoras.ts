import request from "./api";

interface Operadora {
  registro_ans: string;
  cnpj: string;
  nome_empresa: string;
  nome_fantasia: string;
  modalidade: string;
  cidade: string;
  uf: string;
  telefone: string;
  razao_social: string;
}

export default {
  async getOperadoras(searchQuery?: string): Promise<Operadora[]> {
    const queryParam = searchQuery ? `?search=${encodeURIComponent(searchQuery)}` : "";
    const response = await request<{
      count: number;
      next: string | null;
      previous: string | null;
      results: Operadora[];
    }>(`/operadoras/${queryParam}`);
    return response.results;
  }
};