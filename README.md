# Teste funcão RANKX do DAX no power BI :rocket:

# O que é a função RANKX no Power BI (DAX)?

A função RANKX no Power BI é usada para classificar valores dentro de uma tabela com base em uma métrica específica, como vendas, lucro ou quantidade. Ela retorna um número indicando a posição do valor em um ranking, podendo ser ordenado de forma ascendente ou descendente.

```
RANKX(
        <Tabela>,
        <Expressão>,
        [<Valor Alternativo>],  -- (Opcional)
        [<Ordem>],  -- (Opcional: ASC | DESC)
        [<Tipo de Empate>]  -- (Opcional: DENSE | SKIP)
    )

```

- < Tabela > → A tabela onde o ranking será aplicado.
- < Expressão > → A métrica usada para ranquear (ex: soma de vendas).
- < Valor Alternativo > → (Opcional) Define um valor alternativo caso a métrica não esteja disponível.
- < Ordem > → (Opcional) DESC para ordem decrescente (maior valor = 1) ou ASC para ordem crescente.
- < Tipo de Empate > → (Opcional) DENSE mantém sequência contínua (1,2,2,3), enquanto SKIP pula rankings em empates (1,2,2,4).