--Top 10 operadoras com maiores despesas na categoria exigidas no último trimestre
SELECT o.razao_social,d.reg_ans AS registro_ans,SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes d
JOIN operadoras o ON d.reg_ans = o.registro_ans
WHERE 
    EXTRACT(YEAR FROM d.data) = 2024
    AND EXTRACT(QUARTER FROM d.data) = 4
    AND d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
GROUP BY o.razao_social, d.reg_ans
ORDER BY total_despesas DESC
LIMIT 10;


--Top 10 operadoras com maiores despesas nessa categoria no último ano
SELECT o.razao_social,d.reg_ans AS registro_ans,SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes d
JOIN operadoras o ON d.reg_ans = o.registro_ans
WHERE 
    EXTRACT(YEAR FROM d.data) = 2024
    AND d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
GROUP BY o.razao_social, d.reg_ans
ORDER BY total_despesas DESC
LIMIT 10;