import pdfplumber
import pandas as pd
import os
import zipfile

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Parte1_web_scrapping", "anexos"))
pdf_path = os.path.join(base_dir, "Anexo_I.pdf")

output_csv = "rol_procedimentos.csv"
output_zip = "Teste_RafaelFeijo.zip"

#lista para armazenar as tabelas
todas_tabelas = []

with pdfplumber.open(pdf_path) as pdf:
    for i, pagina in enumerate(pdf.pages):
        try:
            tabela = pagina.extract_table()
            if tabela:
                df = pd.DataFrame(tabela[1:], columns=tabela[0]) 
                todas_tabelas.append(df)
        except Exception as e:
            print(f"Erro ao processar página {i+1}: {e}")

# Junta todas as páginas
print(f"Tabelas extraídas: {len(todas_tabelas)}")
df_final = pd.concat(todas_tabelas, ignore_index=True)

substituicoes = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}

# Substitui nas colunas que contêm essas siglas
for coluna in df_final.columns:
    df_final[coluna] = df_final[coluna].replace(substituicoes)

#CSV
df_final.to_csv(output_csv, index=False)
print(f"✅ CSV salvo como: {output_csv}")

# Compacta o CSV
with zipfile.ZipFile(output_zip, "w") as zipf:
    zipf.write(output_csv)

print(f"Arquivo compactado criado: {output_zip}")
