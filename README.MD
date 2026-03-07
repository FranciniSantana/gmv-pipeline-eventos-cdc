| <img src="assets/hotmart_logo.png" width="120"> | **Pipeline GMV - Eventos CDC**<br>Projeto de modelagem analítica utilizando eventos CDC e modelagem bitemporal. |
|---|---|

## Objetivo
O objetivo desta pipeline é atender o time financeiro da Hotmart disponibilizando dados diários do GMV preservando o histórico dos dados e garantindo auditoria.

## Arquitetura
O padrão segue a arquitetura medalhão:


## Stack AWS
- S3 para armazenamento dados
- Glue para ETL
- Redshift para DataWarehouse
- Linguagens: SQL e Python

## Modelagem

A tabela segue um modelo bitemporal simplificado, permitindo manter histórico de alterações no cálculo do GMV sem sobrescrever dados anteriores. Dessa forma é possível consultar tanto o valor vigente quanto versões históricas do cálculo.


**Referências:**
- [Bi-Temporal Data Modeling: An Overview](https://contact-rajeshvinayagam.medium.com/bi-temporal-data-modeling-an-overview-cbba335d1947)
- [Bitemporal History
](https://martinfowler.com/articles/bitemporal-history.html)
- [Implementing Bitemporal Modeling for the Best Value
](https://www.dataversity.net/articles/implementing-bitemporal-modeling-best-value/#:~:text=Bitemporal%20Modeling%20is%20an%20extremely,of%20sync%20with%20each%20other.)
- [The Design and Implementation of a Bitemporal DBMS](https://www.youtube.com/watch?v=YjAVsvYGbuU&t=1484s)

## Estrutura de pastas
```
Em construção
```

## Documentação
Acesse o link da documentação da tabela [aqui.]()