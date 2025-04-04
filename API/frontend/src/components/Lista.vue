<script lang="ts">
import { defineComponent, onMounted } from "vue";
import { useOperadorasStore } from "@/store/op_store";
import { storeToRefs } from "pinia";

export default defineComponent({
  setup() {
    const operadorasStore = useOperadorasStore();
    const { operadoras, loading, error } = storeToRefs(operadorasStore);

    onMounted(() => {
      operadorasStore.fetchOperadoras();
    });

    return { operadoras, loading, error };
  }
});
</script>

<template >
  <div  v-for="operadora in operadoras" :key="operadora.registro_ans"> 
    <p>{{ operadora.razao_social}}</p>
    <div v-if="loading" class="text-center">
      Carregando...
    </div>
    <div v-else-if="error" class="text-center text-danger">
      {{ error }}
    </div>
    <template v-else>

      <div v-if="operadoras.length > 0" class="col-md-12 d-flex flex-column align-items-center">
        <div class="table-container" >
          <table class="table table-success table-bordered">
            <thead class="table-light">
              <tr>
                <th>Registro ANS</th>
                <th>CNPJ</th>
                <th>Razão Social</th>
                <th>Nome Fantasia</th>
                <th>Modalidade</th>
                <th>Cidade/UF</th>
                <th>Telefone</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{{ operadora.registro_ans }}</td>
                <td>{{ operadora.cnpj }}</td>
                <td>{{ operadora.razao_social }}</td>
                <td>{{ operadora.nome_fantasia || 'N/A' }}</td>
                <td>{{ operadora.modalidade }}</td>
                <td>{{ operadora.cidade }} / {{ operadora.uf }}</td>
                <td>{{ operadora.telefone }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div v-else class="text-center">
        Nenhuma operadora encontrada
      </div>
    </template>
  </div>
</template>

<style scoped>
p {
  color: rgb(23, 109, 80);
  text-align: center;
  margin-bottom: 16px;
  font-weight: bold;
}

.table {
  font-size: 0.9rem;
  max-width: 50px;

}

th, td {
  text-align: center;
}
</style>
