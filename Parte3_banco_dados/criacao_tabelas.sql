CREATE TABLE operadoras (
    registro_ans VARCHAR(10) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_de_comercializacao TEXT,
    data_registro_ans DATE
);

CREATE TABLE demonstracoes (
    data DATE,
    reg_ans VARCHAR(10),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    vl_saldo_inicial NUMERIC,
    vl_saldo_final NUMERIC
);
