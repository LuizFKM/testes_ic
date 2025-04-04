<script setup lang="ts">
import { ref } from "vue";
import { useOperadorasStore } from "@/store/op_store";

const store = useOperadorasStore();
const searchQuery = ref("");

const buscarOperadoras = () => {
  store.fetchOperadoras(searchQuery.value);
};
</script>

<template>
  <div class="col-6 p-5 mt-5">
    
    <form @submit.prevent="buscarOperadoras">
      <label class="label" for="inOperadoras">Procure uma operadora: </label>
      <div class="input-group mb-3">
        
        <input
          type="text"
          v-model="searchQuery"
          id="inOperadoras"
          class="form-control bg-transparent"
          placeholder="Nome da operadora, cnpj, cidade, registro ans"
        />
      </div>
      <button type="submit" class="btn btn-success">Procurar</button>
    </form>
  </div>
</template>

<style scoped>
.btn {
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.582);
}
.label{
  font-weight: bold;
}
input::placeholder {
  color: rgb(122, 122, 122);
  opacity: 1;
}
</style>
