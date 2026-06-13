# Fase 4 - Confiabilidade

## Procedimento Executado

Nesta etapa do projeto, foram medidas as métricas **1.1**, **1.2**, **2.1** e **2.2** definidas na [Fase 3](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase3/2-confiabilidade/), que tratam se sobre a **Maturidade** e **Tolerância a Falhas** do sistema AGIO.

As medições foram obtidas através de scripts de testes das funcionalidades mencionadas na Fase 3 e depois calculadas seguindo o método descrito na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/).

![Resultados dos testes](../imagens/fase%204/resultados.png)
<p align="center"><em>Figura 2: Resultados obtidos ao executar testes, que será # Fase 4 - Confiabilidade

## Procedimento Executado

Nesta etapa do projeto, foram medidas as métricas **1.1**, **1.2**, **2.1** e **2.2** definidas na [Fase 3](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase3/2-confiabilidade/), que tratam se sobre a **Maturidade** e **Tolerância a Falhas** do sistema AGIO.

As medições foram obtidas através de scripts de testes das funcionalidades mencionadas na Fase 3 e depois calculadas seguindo o método descrito na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/).

![Resultados dos testes](///.png)
<p align="center"><em>Figura 2: Resultados obtidos ao executar testes, que será utilizado para as métricas 1.1, 1.2 e 2.1</em></p>

---

## Métricas

### Métrica 1.1: Taxa de Falhas Funcionais

Esta métrica contabiliza o número de falhas encontradas em relação ao número total de operações realizadas.

**Fórmula:**

> - Taxa de Falhas = (N° de falhas / N° total de operações) x 100

### Métrica 1.2: Taxa de Operações Bem-Sucedidas

Esta métrica contabiliza o número de operações concluídas com sucesso em relação ao número total de operações realizadas.

**Fórmula:**

> - Taxa de Sucesso = (N° de operações concluídas com sucesso / N° total de operações) x 100

### Métrica 2.1: Taxa de Tratamento de Entradas Inválidas

Esta métrica contabiliza o número de operações bem-sucedidas no tratamento e rejeição controlada de dados de entrada incorretos.

**Fórmula:**

> - Taxa de Tratamento= (N° de entradas inválidas tratadas / N° total de entradas inválidas) x 100

### Métrica 2.2: Taxa de Proteção Contra Acesso Indevido

Esta métrica contabiliza a eficácia do sistema no bloqueio de tentativas de acesso não autorizadas ou maliciosas.

**Fórmula:**

> - Taxa de Proteção= (N° de tentativas bloqueadas / N° total de tentativas indevidas) x 100

## Medição (Dados Coletados)

Nesta seção são apresentados os resultados obtidos a partir da aplicação das métricas definidas anteriormente. Para cada métrica, é demonstrado o cálculo realizado com base nos dados coletados durante a execução dos testes, bem como o valor final obtido.

Além disso, cada resultado é relacionado ao respectivo critério de aceitação estabelecido pelo modelo GQM, servindo como base para a análise e o julgamento que serão realizados na seção seguinte. 

### Métrica 1.1: Taxa de Falhas Funcionais

Foram executadas as seguintes operações: Login, Cadastro de Itens, Edição de Itens, Remoção de Itens, Consulta do Inventário e Exportação CSV(a cada novo item adicionado);

Abaixo oque foi observado:

| Acão| Descrição | Quantidade | Observações| 
|:--:|:---------|:------|:--------|
| Login | | 10| Executou perfeitamente a ação de login| 
| Cadastro de Item |  |  10| Executou perfeitamente a ação de cadastrar os itens no inventário |  
| Edição de Item |  | 10 | Executou perfeitamente a ação de editar os itens do inventário |  
| Remoção de Item |  | 10 |Executou perfeitamente a ação de remover os itens do inventário  |  
| Consulta de Inventário |  | 10 | Executou perfeitamente a ação de exibir os itens do inventário |  
| Exportação CSV |  | 10 |  Exportou a lista de itens perfeitamente, a cada item adicionado| 


Executando a fórmula:
> - Taxa de Falhas = (N° de falhas / N° total de operações) x 100
> -  (60 / 60) x 100 = 100%

### Métrica 1.2: Taxa de Operações Bem-Sucedidas

Foram executadas as seguintes operações: Login, Cadastro de Itens, Edição de Itens, Remoção de Itens, Consulta do Inventário e Exportação CSV(a cada novo item adicionado);

Abaixo oque foi observado:

| Acão| Descrição | Quantidade | Observações| 
|:--:|:---------|:------|:--------|
| Login | | 10| Executou perfeitamente a ação de login| 
| Cadastro de Item |  |  10| Executou perfeitamente a ação de cadastrar os itens no inventário |  
| Edição de Item |  | 10 | Executou perfeitamente a ação de editar os itens do inventário |  
| Remoção de Item |  | 10 |Executou perfeitamente a ação de remover os itens do inventário  |  
| Consulta de Inventário |  | 10 | Executou perfeitamente a ação de exibir os itens do inventário |  
| Exportação CSV |  | 10 |  Exportou a lista de itens perfeitamente, a cada item adicionado| 

Execuatndo a fórmula:
> - Taxa de Sucesso = (N° de operações concluídas com sucesso / N° total de operações) x 100

> - (60 / 60) x 100 = 100%

### Métrica 2.1: Taxa de Tratamento de Entradas Inválidas

Foram realizados testes de consistência e robustez no sistema, focados na identificação de comportamentos inesperados. As operações validaram o comportamento da aplicação diante de: Campos Obrigatórios Vazios, Dados fora do Formato Esperado, Valores Inválidos, Dados Duplicados e Caracteres Inválidos.

Abaixo oque foi observado:

| Acão| Descrição | Quantidade | Observações| 
|:--:|:---------|:------|:--------|
| Campo Obrigatório Vazio | | 10| Em todas as situações, os campos considerados obrigatórios emitiram um aviso para seu preenchimento | 
| Dados fora do Formato Esperado |  |  10|  Em situações de preenchimento, de informações númericas, com os dados fora do esperado, o campo emitiu um alerta como: ``Preencha com um número``  |  
| Valores Inválidos |  | 10 |  Em situações de preenchimento, do campo de "Preço", com os valores inválidos, o campo aceitou sem demais reclamações, como preços negativos|  
| Dados Duplicados |  | 10 | Em situações de preenchimento das informações, com os dados duplicados, o campo emitiu um alerta dizendo: ``Erro ao adicionar produto: {"product_name":["product table with this product name already exists."]}``|  
| Caracteres Inválidos |  | 10 | Em todas as situações, de preenchimento com texto contendo Caracteres Inválidos, o campo aceitou em todas elas|  

![Tabela Cadastrada no Inventário](../imagens/fase4/tabelaTeste.png) 


> - Taxa de Tratamento= (N° de entradas inválidas tratadas / N° total de entradas inválidas) x 100

> -  (30 / 50) x 100 = 60%

### Métrica 2.2: Taxa de Proteção Contra Acesso Indevido

| Acão| Descrição | Quantidade | Observações| 
|:--:|:---------|:------|:--------|
| Acesso a Páginas Restritas sem Login | Tentativa de acessar diretamente URLs internas do inventário sem autenticação prévia | 10| O sistema barrou todas as tentativas, tratando corretamente a restrição e redirecionando para a tela de autenticação |

> - Taxa de Proteção= (N° de tentativas bloqueadas / N° total de tentativas indevidas) x 100

<p align="center"><strong>Tabela 1: Resultados Consolidados da Avaliação de Confiabilidade</strong></p>

| Métrica | Subcaracterística | Fórmula | Cáculo | Critério de Aceitação (GQM) |
|----------|------------------|----------|-------|-----------------------------|
| M1.1 (Q1) Taxa de Falhas Funcionais | Maturidade | (Nº de falhas / Nº total de operações) × 100 | | < 2% |
| M1.2 (Q1) Taxa de Operações Bem-Sucedidas | Maturidade | (Nº de operações concluídas com sucesso / Nº total de operações) × 100 | | > 98% |
| M2.1 (Q2) Taxa de Tratamento de Entradas Inválidas | Tolerância a Falhas | (Nº de entradas inválidas tratadas / Nº total de entradas inválidas) × 100 | | > 95% |
| M2.2 (Q2) Taxa de Proteção Contra Acesso Indevido | Tolerância a Falhas | (Nº de tentativas bloqueadas / Nº total de tentativas indevidas) × 100 | | > 95% |

<p align="center"><em>Autor: Arthur Guilherme, João Igor e Tiago Lemes</em></p>


## Análise e Julgamento

<p align="center"><strong>Tabela 2: Análise e Julgamento das Hipóteses</strong></p>

| Métrica | Resultado Obtido | Critério de Aceitação (GQM)  | Julgamento |
|----------|------------------|----------|-----------------------------|
| M1.1 (Q1) Taxa de Falhas Funcionais | 0% | < 2% | **CONFIRMADA** |
| M1.2 (Q1) Taxa de Operações Bem-Sucedidas | 100% | > 98% | **CONFIRMADA** |
| M2.1 (Q2) Taxa de Tratamento de Entradas Inválidas | 60% | > 95% | **REFUTADA** |
| M2.2 (Q2) Taxa de Proteção Contra Acesso Indevido | 100% | > 95% | **CONFIRMADA**|

<p align="center"><em>Autor: Arthur Guilherme, João Igor e Tiago Lemes</em></p>

## Conclusão

As métricas de Taxa de Falhas Funcionais (M1.1) e Taxa de Operações Bem-Sucedidas (M1.2) obtiveram, respectivamente, 0% e 100%. Evidenciando que as principais funcionalidades centrais avaliadas — como Login, Cadastro, Edição, Remoção, Consulta e Exportação CSV — encontram-se estáveis e robustas. Portanto, as hipóteses associadas à maturidade do sistema foram **confirmadas**.

Por outro lado, os resultados obtidos para a subcaracterística de **Tolerância a Falhas** indicam que o sistema necessita de melhorias. A Taxa de Tratamento de Entradas Inválidas (M2.1) atingiu apenas 60%, valor significativamente abaixo do critério de aceitação esperado para a análise sendo de 95%, sendo ela **refutada**. 

A análise qualitativa revelou que o AGIO trata adequadamente cenários de campos obrigatórios vazios, tipos numéricos inconsistentes e dados duplicados, mas ele falha na inserção de valores inválidos (como preços negativos) e caracteres especiais sem a devida sanitização ou bloqueio.

Por fim a Taxa de Proteção Contra Acesso Indevido (M2.2) atingiu 100%, atigindo o criterio suposto de 95%. Os testes comprovaram que o sistema lida de forma correta e segura com restrições de navegação, impedindo com sucesso o acesso às páginas privadas por usuários não autenticados, o que resultou na **confirmação** desta hipótese de segurança.


## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |   [João Igor](https://github.com/JoaoPC10)| 12/06/2026 |
| 02 | adição de print de teste e conclusão | [Arthur Guilherme](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |   [João Igor](https://github.com/JoaoPC10)| 12/06/2026 |