from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

#carrega CSV
df = pd.read_csv("Relatorio_cadop.csv", sep=";", encoding="utf-8")

@app.route("/busca")
def busca_operadoras():
    termo = request.args.get("q", "").strip().lower()
    cidade = request.args.get("cidade", "").strip().lower()

    if not termo:
        return jsonify({"erro": "Parâmetro 'q' é obrigatório."}), 400

    #filtro por termo
    resultados = df[
        df["Razao_Social"].str.lower().str.contains(termo) |
        df["Nome_Fantasia"].fillna("").str.lower().str.contains(termo)
    ]

    #filtro por cidade
    if cidade:
        resultados = resultados[resultados["Cidade"].str.lower() == cidade]

    #converte NaN para None - erro chato
    registros = resultados.replace({np.nan: None}).to_dict(orient="records")
    return jsonify(registros)

if __name__ == "__main__":
    app.run(debug=True)
