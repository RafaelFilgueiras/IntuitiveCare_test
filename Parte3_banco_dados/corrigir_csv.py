import pandas as pd
import os

#CSV trimestrais
arquivos = [
    "1T2023.csv", "2t2023.csv", "3T2023.csv", "4T2023.csv",
    "1T2024.csv", "2T2024.csv", "3T2024.csv", "4T2024.csv"
]

#Caminho da pasta onde estão os arquivos
pasta = os.path.join("Parte3_banco_dados", "demonstracoes_contabeis")

for nome_arquivo in arquivos:
    caminho_original = os.path.join(pasta, nome_arquivo)
    caminho_corrigido = os.path.join(pasta, nome_arquivo.replace(".csv", "_corrigido.csv"))

    print(f"Corrigindo: {nome_arquivo}")

    df = pd.read_csv(caminho_original, sep=";", encoding="utf-8")

    for coluna in ['VL_SALDO_INICIAL', 'VL_SALDO_FINAL']:
        if coluna in df.columns:
            df[coluna] = (
                df[coluna].astype(str)
                .str.replace(".", "", regex=False)  # remove separadores de milhar
                .str.replace(",", ".", regex=False)  # troca vírgula por ponto
            ).astype(float)

    #CSV corrigido
    df.to_csv(caminho_corrigido, sep=";", index=False, encoding="utf-8")
    print(f"Corrigido salvo como: {caminho_corrigido}")



