import requests
from bs4 import BeautifulSoup
import os
import zipfile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

os.makedirs("anexos", exist_ok=True)

#baixar arquivos 
def baixar_pdf(link, nome_arquivo):
    response = requests.get(link)
    if response.status_code == 200:
        with open(f"anexos/{nome_arquivo}", "wb") as f:
            f.write(response.content)
        print(f"Baixado: {nome_arquivo}")
    else:
        print(f"Erro ao baixar {nome_arquivo} ")

#links encontrados via scraping 
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for link in soup.find_all("a", href=True):
    href = link["href"]
    texto = link.get_text(strip=True)

    if href.endswith(".pdf"):
        print(f"Texto: {texto} | Link: {href}")

#Baixar os anexos com os links 
anexo_1_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
anexo_2_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

baixar_pdf(anexo_1_url, "Anexo_I.pdf")
baixar_pdf(anexo_2_url, "Anexo_II.pdf")

#Zipar os arquivos
with zipfile.ZipFile("Anexos_Compactados.zip", "w") as zipf:
    for nome in ["Anexo_I.pdf", "Anexo_II.pdf"]:
        caminho = os.path.join("anexos", nome)
        if os.path.exists(caminho):
            zipf.write(caminho, arcname=nome)

print("Arquivos compactados em: Anexos_Compactados.zip")
