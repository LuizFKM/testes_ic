

<script setup lang="ts">
import Formulario from './components/Formulario.vue';
import Lista from './components/Lista.vue';
</script>

<template>
  <header class=" header p-4 ">
      <h1 class="text-center text-success ">Operadoras Ativas na ANS</h1>
  </header>
  <div class="container custom-container vh-100 bg-gradient ">
  
    <Formulario/>
    <Lista />
  </div>


</template>

<style scoped>
  .header {
    background-color: aquamarine;
  }
</style>
