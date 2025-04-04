import { defineStore } from "pinia";
import operadorasService from "@/services/operadoras";

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



export const useOperadorasStore = defineStore("operadoras", {
  state: () => ({
    operadoras: [] as Operadora[],
    loading: false,
    error: null as string | null

  }),

  actions: {
    async fetchOperadoras(searchQuery?: string) {
      this.loading = true;
      this.error = null;
      try {
        const data = await operadorasService.getOperadoras(searchQuery);

        // Validação adicional
        if (!Array.isArray(data)) {
          throw new Error("Formato de dados inválido: esperado array");
        }

        this.operadoras = data;
      } catch (e) {
        this.error = (e as Error).message;
        this.operadoras = []; // Limpa os dados em caso de erro
      } finally {
        this.loading = false;
      }
    }
  }
});