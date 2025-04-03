COPY operadoras 
FROM 'C:\dados_ans\operadoras\Relatorio_cadop.csv' 
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8';

COPY dados_contabeis
FROM 'C:\dados_ans\contabeis\1T2023.csv' 
DELIMITER ';'
CSV HEADER
ENCODING 'UTF 8';

COPY dados_contabeis
FROM 'C:\dados_ans\contabeis\1T2024.csv' 
DELIMITER ';'
CSV HEADER
ENCODING 'UTF 8';

COPY dados_contabeis
FROM 'C:\dados_ans\contabeis\2T2023.csv' 
DELIMITER ';'
CSV HEADER
ENCODING 'UTF 8';

COPY dados_contabeis
FROM 'C:\dados_ans\contabeis\2T2024.csv' 
DELIMITER ';'
CSV HEADER
ENCODING 'UTF 8';

COPY dados_contabeis
FROM 'C:\dados_ans\contabeis\3T2023.csv' 
DELIMITER ';'
CSV HEADER
ENCODING 'UTF 8';

COPY dados_contabeis
FROM 'C:\dados_ans\contabeis\3T2024.csv' 
DELIMITER ';'
CSV HEADER
ENCODING 'UTF 8';

COPY dados_contabeis
FROM 'C:\dados_ans\contabeis\4T2023.csv' 
DELIMITER ';'
CSV HEADER
ENCODING 'UTF 8';

COPY dados_contabeis
FROM 'C:\dados_ans\contabeis\4T2024.csv' 
DELIMITER ';'
CSV HEADER
ENCODING 'UTF 8';
