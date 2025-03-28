# Teste funcão RANKX do DAX no power BI :rocket:

# O que é a função RANKX no Power BI (DAX)?

A função RANKX no Power BI é usada para classificar valores dentro de uma tabela com base em uma métrica específica, como vendas, lucro ou quantidade. Ela retorna um número indicando a posição do valor em um ranking, podendo ser ordenado de forma ascendente ou descendente.

```DAX
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

### Rankx dimanmico utilizado _IF_

```dax
rankking filtrado = 
                IF(SELECTEDVALUE(Filtro[TIPO])=="Venda",RANKX(A(dataset_ficticio),[venda],,DESC),
                IF(SELECTEDVALUE(Filtro[TIPO])=="Devolução",RANKX(ALL(dataset_ficticio),[devolucao],,ASC),
                IF(SELECTEDVALUE(Filtro[TIPO])=="Qtd Cliente",RANKX(ALL(dataset_ficticio),[quantidade cliente],,DESC),
                IF(SELECTEDVALUE(Filtro[TIPO])=="Qtd Nota",RANKX(ALL(dataset_ficticio),[quantidade nota],,DESC),
                    RANKX(ALL(dataset_ficticio),[venda],,DESC
                )
            )
        )
    )
)

```

### Rankx dinâmico utilizando _SWITCH_

```dax

rank_filtrado2 = SWITCH(TRUE(),
                            SELECTEDVALUE(Filtro[TIPO]) = "Venda",RANKX(ALL(dataset_ficticio),[venda],,DESC),
                            SELECTEDVALUE(Filtro[TIPO]) = "Devolução",RANKX(ALL(dataset_ficticio),[devolucao],,ASC),
                            SELECTEDVALUE(Filtro[TIPO]) = "Qtd Cliente",RANKX(ALL(dataset_ficticio),[quantidade cliente],,DESC,Skip),
                            SELECTEDVALUE(Filtro[TIPO]) = "Qtd Nota",RANKX(ALL(dataset_ficticio),[quantidade nota],,DESC),
                            RANKX(ALL(dataset_ficticio),[venda],,DESC))

```



![Static Badge](https://img.shields.io/badge/quelvin-blue?logo=github&logoColor=white&labelColor=black&cacheSeconds=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fquelvincarvalho%2F)



