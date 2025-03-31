<template>
    <div class="container">
      <h1>Busca de Operadoras</h1>
  
      <form @submit.prevent="buscarOperadoras" class="form">
        <input
          v-model="termo"
          placeholder="Buscar por nome ou razão social"
          class="input"
        />
        <input
          v-model="cidade"
          placeholder="Filtrar por cidade (opcional)"
          class="input"
        />
        <button type="submit" class="button">Buscar</button>
      </form>
  
      <div v-if="carregando" class="loading">🔄 Carregando...</div>
  
      <div v-else-if="resultados.length">
        <h2 class="result-title">Resultados:</h2>
        <ul class="result-list">
          <li v-for="(op, index) in resultados" :key="index" class="result-item">
            <strong>{{ op.Nome_Fantasia || op.Razao_Social }}</strong><br />
            <span>Cidade:</span> {{ op.Cidade || 'N/A' }} - {{ op.UF || 'N/A' }}<br />
            <span>Modalidade:</span> {{ op.Modalidade || 'N/A' }}
          </li>
        </ul>
      </div>
  
      <div v-else-if="buscou" class="no-results">Nenhuma operadora encontrada.</div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const termo = ref('')
  const cidade = ref('')
  const resultados = ref([])
  const carregando = ref(false)
  const buscou = ref(false)
  
  const buscarOperadoras = async () => {
    carregando.value = true
    buscou.value = false
    resultados.value = []
  
    try {
      const response = await axios.get('http://127.0.0.1:5000/busca', {
        params: { q: termo.value, cidade: cidade.value },
        headers: { 'Accept': 'application/json' }
      })
  
      resultados.value = response.data
    } catch (error) {
      console.error("❌ Erro na busca:", error)
      resultados.value = []
    } finally {
      carregando.value = false
      buscou.value = true
    }
  }
  </script>
  
  <style scoped>
  .container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    font-family: 'Segoe UI', sans-serif;
  }
  
  h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
    color: #2c3e50;
  }
  
  .form {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }
  
  .input {
    padding: 0.5rem 0.75rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 6px;
    min-width: 250px;
  }
  
  .button {
    padding: 0.5rem 1rem;
    font-size: 1rem;
    background-color: #2c3e50;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }
  .button:hover {
    background-color: #1a252f;
  }
  
  .loading {
    margin-top: 1rem;
    font-style: italic;
  }
  
  .result-title {
    margin-top: 1.5rem;
    font-size: 1.25rem;
    color: #34495e;
  }
  
  .result-list {
    list-style: none;
    padding: 0;
    margin-top: 1rem;
    max-width: 600px;
    width: 100%;
  }
  
  .result-item {
    background: #f9f9f9;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  
  .result-item span {
    font-weight: 600;
  }
  
  .no-results {
    margin-top: 1rem;
    font-style: italic;
    color: #888;
  }
  </style>
  