
CREATE TABLE tabela_operadoras (
    registro_ans VARCHAR (6),
    cnpj VARCHAR(14) NOT NULL,
    razao_social VARCHAR(140) NOT NULL,
    nome_fantasia VARCHAR(140),
    modalidade VARCHAR(40),
    logradouro VARCHAR(40),
    numero VARCHAR(20),
    complemento VARCHAR(40),
    bairro VARCHAR(30),
    cidade VARCHAR(30),
    uf VARCHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(4),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(50),
    cargo_representante VARCHAR(40),
    regiao_de_comercializacao INTEGER,
    data_registro_ans DATE
);

CREATE TABLE tabela_dados_contabeis (
    reg_ans integer NOT NULL,
    cd_conta_contabil INTEGER NOT NULL,
    descricao VARCHAR(150),
    vl_saldo_inicial NUMERIC(15,2),
    vl_saldo_final NUMERIC(15,2),
    data DATE
);
