# Fase 4 - Confiabilidade

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

| Ação | Descrição | Quantidade | Observações |
|:--:|:---------|:------:|:--------|
| Login | Realização do processo de autenticação de usuários por meio de credenciais válidas para acesso ao sistema. | 10 | Executou perfeitamente a ação de login, e falhou com credenciais inválidas. |
| Cadastro de Item | Inclusão de novos produtos no inventário, informando nome, quantidade, categoria, descrição e preço. | 10 | Executou perfeitamente a ação de cadastrar os itens no inventário. |
| Edição de Item | Alteração das informações de produtos já cadastrados, permitindo atualizar seus dados no inventário. | 10 | Executou perfeitamente a ação de editar os itens do inventário. |
| Remoção de Item | Exclusão de produtos previamente cadastrados, removendo-os do inventário do sistema. | 10 | Executou perfeitamente a ação de remover os itens do inventário. |
| Consulta de Inventário | Visualização dos produtos cadastrados e de suas respectivas informações armazenadas no inventário. | 10 | Executou perfeitamente a ação de exibir os itens do inventário. |
| Exportação CSV | Geração e download de um arquivo CSV contendo os dados dos produtos cadastrados no inventário. | 10 | Exportou a lista de itens perfeitamente, a cada item adicionado. | 


Executando a fórmula:
> - Taxa de Falhas = (N° de falhas / N° total de operações) x 100
> -  (1 / 60) x 100 = 1,6%

### Métrica 1.2: Taxa de Operações Bem-Sucedidas

Foram executadas as seguintes operações: Login, Cadastro de Itens, Edição de Itens, Remoção de Itens, Consulta do Inventário e Exportação CSV(a cada novo item adicionado);

Abaixo oque foi observado:


| Ação | Descrição | Quantidade | Observações |
|:--:|:---------|:------:|:--------|
| Login | Realização do processo de autenticação de usuários por meio de credenciais válidas para acesso ao sistema. | 10 | Executou perfeitamente a ação de login. |
| Cadastro de Item | Inclusão de novos produtos no inventário, informando nome, quantidade, categoria, descrição e preço. | 10 | Executou perfeitamente a ação de cadastrar os itens no inventário. |
| Edição de Item | Alteração das informações de produtos já cadastrados, permitindo atualizar seus dados no inventário. | 10 | Executou perfeitamente a ação de editar os itens do inventário. |
| Remoção de Item | Exclusão de produtos previamente cadastrados, removendo-os do inventário do sistema. | 10 | Executou perfeitamente a ação de remover os itens do inventário. |
| Consulta de Inventário | Visualização dos produtos cadastrados e de suas respectivas informações armazenadas no inventário. | 10 | Executou perfeitamente a ação de exibir os itens do inventário. |
| Exportação CSV | Geração e download de um arquivo CSV contendo os dados dos produtos cadastrados no inventário. | 10 | Exportou a lista de itens perfeitamente, a cada item adicionado. |

Execuatndo a fórmula:
> - Taxa de Sucesso = (N° de operações concluídas com sucesso / N° total de operações) x 100

> - (60 / 60) x 100 = 100%

### Métrica 2.1: Taxa de Tratamento de Entradas Inválidas

Foram realizados testes de consistência e robustez no sistema, focados na identificação de comportamentos inesperados. As operações validaram o comportamento da aplicação diante de: Campos Obrigatórios Vazios, Dados fora do Formato Esperado, Valores Inválidos, Dados Duplicados e Caracteres Inválidos.

Abaixo oque foi observado:

| Ação | Descrição | Quantidade | Observações |
|:--:|:---------|:------:|:--------|
| Campo Obrigatório Vazio | Verificação do comportamento do sistema quando campos obrigatórios são deixados sem preenchimento durante o cadastro ou edição de informações. | 10 | Em todas as situações, os campos considerados obrigatórios emitiram um aviso para seu preenchimento. |
| Dados fora do Formato Esperado | Avaliação da validação de formato dos dados inseridos, especialmente em campos que exigem valores numéricos. | 10 | Em situações de preenchimento de informações numéricas com dados fora do formato esperado, o campo emitiu um alerta como: `Preencha com um número`. |
| Valores Inválidos | Teste da aceitação de valores que, embora estejam no formato correto, não fazem sentido para a regra de negócio, como preços negativos. | 10 | Em situações de preenchimento do campo "Preço" com valores inválidos, o campo aceitou os dados sem apresentar qualquer restrição, como no caso de preços negativos. |
| Dados Duplicados | Verificação da validação de unicidade para evitar o cadastro repetido de produtos já existentes no inventário. | 10 | Em situações de preenchimento com dados duplicados, o sistema emitiu o alerta: `Erro ao adicionar produto: {"product_name":["product table with this product name already exists."]}`. |
| Caracteres Inválidos | Avaliação do tratamento de caracteres especiais ou não convencionais inseridos em campos textuais do sistema. | 10 | Em todas as situações de preenchimento com texto contendo caracteres considerados inválidos, o sistema aceitou os dados sem restrições. |

![Tabela Cadastrada no Inventário](../imagens/fase4/tabelaTeste.png) 


> - Taxa de Tratamento = (N° de entradas inválidas tratadas / N° total de entradas inválidas) x 100

> -  (30 / 50) x 100 = 60%

### Métrica 2.2: Taxa de Proteção Contra Acesso Indevido

Foram executadas as seguintes operações: Login, Coram executados testes relacionados à segurança e ao controle de acesso do sistema, contemplando cenários de acesso a páginas protegidas sem autenticação, acesso direto por URL a funcionalidades restritas, acesso com usuários sem privilégios administrativos, utilização de sessões expiradas e tentativas de execução de operações administrativas sem as permissões adequadas. Em todos os casos avaliados, o sistema apresentou o comportamento esperado, aplicando corretamente as restrições de autenticação e autorização.

Abaixo oque foi observado:

| Ação | Descrição | Quantidade | Observações |
|:--:|:---------|:------:|:--------|
| Acesso a páginas protegidas sem autenticação | Verificação do comportamento do sistema quando um usuário não autenticado tenta acessar páginas que exigem login prévio. | 10 | O sistema redirecionou corretamente o usuário para a página de login em todas as tentativas realizadas. |
| Acesso direto por URL a funcionalidades restritas | Avaliação da proteção das funcionalidades do sistema contra acessos realizados diretamente por meio da URL, sem passar pelo fluxo normal de autenticação. | 10 | O sistema bloqueou o acesso às funcionalidades restritas e exigiu autenticação para prosseguir. |
| Acesso com usuário sem privilégios administrativos | Verificação das restrições aplicadas a usuários sem permissões administrativas ao tentarem acessar funcionalidades de gerenciamento do sistema. | 10 | O sistema impediu o acesso às funcionalidades administrativas para usuários sem os privilégios necessários. |
| Utilização de sessão expirada | Avaliação do comportamento do sistema quando um usuário tenta realizar operações após a expiração de sua sessão autenticada. | 10 | O sistema invalidou corretamente a sessão expirada e solicitou uma nova autenticação para continuar. |
| Tentativas de executar operações administrativas sem permissão adequada | Verificação dos mecanismos de autorização ao tentar executar ações administrativas sem possuir as permissões exigidas. | 10 | O sistema bloqueou corretamente todas as operações administrativas realizadas sem a devida permissão. |


> - Taxa de Proteção = (N° de tentativas bloqueadas / N° total de tentativas indevidas) x 100

> - (50 / 50) x 100 = 100%

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
| M1.1 (Q1) Taxa de Falhas Funcionais | | < 2% | CONFIRMADA ou REFUTADA |
| M1.2 (Q1) Taxa de Operações Bem-Sucedidas | | > 98% | CONFIRMADA ou REFUTADA |
| M2.1 (Q2) Taxa de Tratamento de Entradas Inválidas |  | > 95% | CONFIRMADA ou REFUTADA |
| M2.2 (Q2) Taxa de Proteção Contra Acesso Indevido |  | > 95% | CONFIRMADA ou REFUTADA |

<p align="center"><em>Autor: Arthur Guilherme, João Igor e Tiago Lemes</em></p>

## Conclusão

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |   [João Igor](https://github.com/JoaoPC10)| 12/06/2026 |
| 02 | Criação do documento |  [João Igor](https://github.com/JoaoPC10) | 02/06/2026 |   [Tiago Lemes](https://github.com/TiagoTeixeira-2005)| 12/06/2026 |