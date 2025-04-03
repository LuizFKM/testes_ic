--último ano(2024)
SELECT dc.reg_ans, op.razao_social, SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS despesas
FROM public.dados_contabeis dc
JOIN public.operadoras op ON dc.reg_ans = op.registro_ans::INTEGER
WHERE dc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
 AND EXTRACT(YEAR FROM dc.data) = 2024
GROUP BY dc.reg_ans, op.razao_social
ORDER BY despesas DESC
LIMIT 10;