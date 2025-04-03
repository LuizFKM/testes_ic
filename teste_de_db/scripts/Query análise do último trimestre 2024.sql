--último trimestre de 2024. Ultimo trimestre considerando a data atual, não há resultados.
SELECT dc.reg_ans, op.razao_social, SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS despesas
FROM public.dados_contabeis dc
JOIN public.operadoras op ON dc.reg_ans = op.registro_ans::INTEGER
WHERE dc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
  AND dc.data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY dc.reg_ans, op.razao_social
ORDER BY despesas DESC
LIMIT 10;

