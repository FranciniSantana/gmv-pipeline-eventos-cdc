# Tabela: fct_gmv_diario
**Descrição:**

A tabela fct_gmv_diario armazena o valor diário agregado do GMV (Gross Merchandise Value) por subsidiária, considerando apenas transações com pagamento confirmado.

A modelagem segue o padrão bitemporal, permitindo manter o histórico de versões do cálculo do GMV ao longo do tempo. Dessa forma, é possível identificar quando um determinado valor de GMV era válido para análise de negócio e também quando esse valor foi registrado ou recalculado no pipeline de dados.

Cada registro representa o valor do GMV para uma subsidiária e data de referência, mantendo controle de vigência por meio das colunas de intervalo temporal e do indicador de versão atual.

Essa abordagem permite:

- rastreabilidade de recalculações do GMV

- auditoria de métricas históricas

- reconstrução do estado da métrica em momentos passados

- controle de atualizações provenientes de reprocessamentos ou chegada tardia de dados

## Schema

| coluna                  | tipo de dado | descrição                                                                                                                                                                                                 |
| ----------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **des_subsidiario**     | VARCHAR(50)             | Identifica a origem da transação associada ao GMV. Indica se o faturamento foi gerado por compras **Nacionais** ou **Internacionais**.                                                                    |
| **dt_valida**           | DATE                    | Data de referência do GMV para análise de negócio. Representa o **dia de faturamento agregado** das transações consideradas no cálculo do GMV.                                                            |
| **vlr_gmv**             | DECIMAL(18,2)           | Valor total do **GMV (Gross Merchandise Value)** agregado para a subsidiária na data de referência. Considera apenas transações com pagamento confirmado.                                                 |
| **dt_transacao_inicio** | DATE                    | Data em que esta versão do cálculo do GMV passou a ser considerada válida na base analítica. Representa o momento em que o valor foi processado ou recalculado no pipeline de dados.                      |
| **dt_transacao_fim**    | DATE                    | Data limite de validade desta versão do cálculo do GMV. Quando igual a **9999-12-31**, indica que esta versão permanece válida até que uma nova atualização seja processada.                              |
| **flg_atual**         | BOOLEAN                 | Indica se o registro representa a **versão vigente do cálculo do GMV** para a combinação de subsidiária e data de referência. Valores possíveis: `true` (registro atual) ou `false` (registro histórico). |

## Chaves da Tabela
### 1. Chave Natural de Negócio

A combinação abaixo identifica a entidade de negócio analisada:

**Colunas:**  `des_subsidiario`, `dt_valida`

### 2. Chave Temporal (bitemporal)

Como a tabela mantém histórico de versões, a unicidade completa do registro é definida por:

**Colunas:**  `des_subsidiario`, `dt_valida`, `dt_transacao_inicio`


## Regra de validação

### Unicidade do Registro Atual

Deve existir apenas um registro ativo para cada combinação de negócio:

`(des_subsidiario, dt_valida)`

### Integridade
- **Intervalo temporal**

`dt_transacao_inicio < dt_transacao_fim`

- **Registro atual**

```
Se:
flg_atual = true
então:
dt_transacao_fim = '9999-12-31'
```

**Atualização de versão**

Quando ocorre recalculação do GMV: 
- o registro atual tem flg_atual = false
- dt_transacao_fim recebe a data da nova versão
- um novo registro é inserido com:
    -  dt_transacao_inicio = data do processamento
    - dt_transacao_fim = '9999-12-31'
    - flg_atual = true