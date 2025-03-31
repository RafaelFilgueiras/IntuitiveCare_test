# 💡 IntuitiveCare — Desafio Técnico

Solução completa do desafio técnico proposto pela **IntuitiveCare**, dividido em 4 partes:

1. **Web Scraping**
2. **Transformação de Dados**
3. **Banco de Dados**
4. **API com Flask + Interface Web com Vue.js**

---

## 🔧 Instalação do Projeto (Backend + Frontend)

### 1. Clone o repositório

```bash
git clone https://github.com/RafaelFilgueiras/IntuitiveCare_test
cd IntuitiveCare_test
```

### 2. Crie e ative um ambiente virtual Python
```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

### 3. Instale as dependências do projeto (todas as partes)
```bash
pip install -r requirements.txt
```

### 4. Instale as dependências do frontend
```bash
cd Parte4_api/frontend
npm install
```

## Parte 1 — Web Scraping

### Como executar

#### 1. Acesse a pasta da Parte 1:
```bash
cd Parte1_web_scrapping
```

#### 2. Execute o script:
```bash
python web_scrapping.py
```

## Parte 2 — Transformação de Dados

### Como executar

#### 1. Acesse a pasta da Parte 2:
```bash
cd Parte2_transformacao_dados
```

#### 2. Execute o script:
```bash
python extrair_dados_pdf.py
```
##### Atenção: 
```bash
Certifique-se de que a estrutura de pastas esteja exatamente como descrita no projeto, pois o script acessa o PDF da Parte 1 via caminho relativo.O arquivo esperado é Parte1_web_scrapping/anexos/Anexo_I.pdf. Se o nome da pasta ou do PDF estiver diferente, será necessário ajustar no script.
```
## Parte 3 — Banco de dados

### Como executar

#### 1. Acesse a pasta da Parte 3:
```bash
cd Parte3_banco_dados
```
#### 2. Corrija os arquivos trimestrais com o script:
```bash
python corrigir_csv.py
```
#### 3. Importação no Banco de Dados: Utilize um SGBD como PostgreSQL para importar os dados.

#### 1. Crie as tabelas com as queries dentro de criacao_tabelas.sql
#### 2. importe os dados com as queries dentro de importar_dados.sql
#### 3. rode as consultas analíticas com as queries de consultas_analiticas.sql

**Atenção** aos nomes das pastas e arquivos, O script corrigir_csv.py depende de um caminho exato para funcionar corretamente: `Parte3_banco_dados/demonstracoes_contabeis/`, dentro dessa pasta deve ter todos os csv dos trimestres dos ultimos dois anos que foram baixados de acordo com o que foi pedido no teste.

## Parte 4 — API

### Como executar

#### 1. Acesse a pasta da Parte 3:
```bash
cd Parte3_banco_dados
```
#### 2. Execute a API Flask (Backend)
```bash
cd backend
python api.py
```
#### 3. Rode a Interface Web
Abra outro terminal e execute:
```bash
cd Parte4_api/frontend
npm run dev
```
#### Testes com o Postman
Dentro da pasta postman/, há uma coleção pronta para testar a API:
```bash
postman/IntuitiveCare API.postman_collection.json
```
Você pode importar esse arquivo no Postman para testar requisições como: 
```bash
GET http://127.0.0.1:5000/busca?q=unimed&cidade=são paulo
```
##### Atenção: 
- O script `api.py` depende do arquivo `Relatorio_cadop.csv`, que não foi incluído no repositório.
- Baixe o CSV manualmente, e coloque-o dentro da pasta `Parte4_api/backend/`.
- O front-end faz chamadas à API local via `axios`, por isso é importante garantir que o back-end esteja rodando antes de acessar a interface.