# Fase 3 - Confiabilidade

## Introdução

Nesta etapa do projeto, será especificado como serão implementadas e executadas as métricas definidas pela abordagem **Goal-Question-Metric (GQM)** para avaliar objetivamente a característica de Confiabilidade do **sistema AGIO**.

A avaliação será realizada em um ambiente local Linux, utilizando a aplicação AGIO em execução, o navegador web para interação com a interface e ferramentas de monitoramento e registro de logs do sistema. Os testes contemplarão operações fundamentais do sistema, como autenticação, cadastro, edição, remoção e consulta de itens do inventário, além da exportação de dados em formato CSV.

Serão executados cenários normais de uso e cenários com entradas inválidas e comportamentos inesperados, permitindo medir a frequência de falhas e a capacidade do sistema de lidar adequadamente com situações adversas. Os resultados coletados serão utilizados para o cálculo das métricas definidas na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/), garantindo rastreabilidade e reprodutibilidade da avaliação.

---

## Métricas a Serem Implementadas

Com base no planejamento realizado na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/), serão coletados dados para as seguintes métricas.

### M1.1 - Taxa de Falhas Funcionais

Avalia a frequência de falhas observadas durante a execução das funcionalidades principais do sistema.

**Fórmula:**

> - TFF = (NF / NO) × 100

Onde:

- **NF** = Número de falhas observadas
- **NO** = Número total de operações realizadas

### M1.2 - Taxa de Operações Bem-Sucedidas

Avalia a proporção de operações concluídas corretamente em relação ao total de operações executadas.

**Fórmula:**

> - TOBS = (OS / NO) × 100

Onde:

- **OS** = Número de operações concluídas com sucesso
- **NO** = Número total de operações realizadas

### M2.1 - Taxa de Tratamento de Entradas Inválidas (TTEI)

Avalia a capacidade do sistema de tratar adequadamente entradas incorretas sem comprometer sua execução.

**Fórmula:**

> - TTEI = (ET / EI) × 100

Onde:

- **ET** = Número de entradas inválidas tratadas corretamente
- **EI** = Número total de entradas inválidas submetidas

### M2.2 - Taxa de Proteção Contra Acesso Indevido (TPAI)

Avalia a capacidade do sistema de impedir acessos não autorizados a funcionalidades restritas.

**Fórmula:**

> - TPAI = (TB / TI) × 100

Onde:

- **TB** = Número de tentativas de acesso indevido bloqueadas
- **TI** = Número total de tentativas de acesso indevido realizadas

### Critérios de Avaliação

A tabela abaixo foi elaborada com base nos critérios estabelecidos na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/). Os resultados obtidos serão utilizados para avaliar o nível de confiabilidade do sistema e sua estabilidade operacional.

<p align="center"><strong>Tabela 1: Critérios de Aceitação</strong></p>

| Métrica | Critério Desejado (Alta Maturidade/Tolerância) |
|----------|----------|
| M1.1 - Taxa de Falhas Funcionais | < 2% |
| M1.2 - Taxa de Operações Bem-Sucedidas | > 98% |
| M2.1 - Taxa de Tratamento de Entradas Inválidas | > 95% |
| M2.2 - Taxa de Proteção Contra Acesso Indevido | > 95% |

<p align="center"><em>Autores: Arthur Guilherme, João Igor e Tiago Lemes</em></p>

---

## Ferramentas e Métodos de Coleta

Abaixo, estão especificados o ambiente de teste, os instrumentos de medição utilizados e o passo a passo realizado para a coleta dos dados.

### Ambiente de Teste

- **Sistema Operacional:** Ubuntu 22.04 LTS (ou distribuição Linux equivalente)
- **Aplicação Avaliada:** AGIO
- **Banco de Dados:** PostgreSQL (conforme configuração do projeto)
- **Navegador:** Brave

### Hardware Utilizado
  
- **CPU:** X núcleos ou superior
- **Memória RAM:** 6 GB ou superior
- **Armazenamento:** X GB ou superior
    
### Pré-requisitos:**
  
  - Ambiente local do AGIO configurado e funcional
  - Banco de dados inicializado
  - Usuário administrador cadastrado
  - Inventário contendo registros para teste

### Instrumentos de Medição

#### M1.1 - Taxa de Falhas Funcionais

Tem como objetivo medir a frequência de falhas durante a execução das funcionalidades principais do AGIO.

**Método de Coleta**

Executar repetidamente as operações de:

- Login
- Cadastro de itens
- Edição de itens
- Remoção de itens
- Consulta de inventário
- Exportação CSV

Registrar:

- Quantidade total de operações realizadas
- Quantidade de falhas observadas

Serão consideradas falhas:

- Erro 500
- Travamentos
- Funcionalidades indisponíveis
- Comportamentos incorretos
- Operações que não produzem o resultado esperado

**Ferramentas**

- Interface Web do AGIO
- Logs da aplicação
- Logs do terminal

#### M1.2 - Taxa de Operações Bem-Sucedidas

**Método de Coleta**

Executar o mesmo conjunto de operações da M1.1:

- Login
- Cadastro de itens
- Edição de itens
- Remoção de itens
- Consulta de inventário
- Exportação CSV

Registrar:

- Quantidade total de operações executadas;
- Quantidade de operações concluídas sem falhas.

Serão consideradas falhas:

- Erro 500
- Travamentos
- Funcionalidades indisponíveis
- Comportamentos incorretos
- Operações que não produzem o resultado esperado

**Ferramentas**

- Interface Web do AGIO
- Logs da aplicação
- Logs do terminal

#### M2.1 - Taxa de Tratamento de Entradas Inválidas

**Método de Coleta**

Realizar tentativas de:

- Campos obrigatórios vazios
- Dados fora do formato esperado
- Valores inválidos
- Dados duplicados
- Caracteres inválidos

Registrar:

- Quantidade total de entradas inválidas submetidas
- Quantidade de entradas inválidas tratadas corretamente pelo sistema

Será considerado tratamento correto quando:

- O sistema exibir mensagem de erro adequada
- O sistema impedir a operação
- Não ocorrer travamento ou erro interno

**Ferramentas**

- Interface Web do AGIO
- Logs da aplicação

#### M2.2 - Taxa de Proteção Contra Acesso Indevido

Tem como objetivo avaliar a capacidade do AGIO de impedir acessos não autorizados e proteger funcionalidades restritas contra usuários sem as permissões adequadas.

**Método de Coleta**

Realizar tentativas de:

- Acesso a páginas protegidas sem autenticação
- Acesso direto por URL a funcionalidades restritas
- Acesso com usuário sem privilégios administrativos
- Utilização de sessão expirada
- Tentativas de executar operações administrativas sem permissão adequada

Registrar:

- Quantidade total de tentativas de acesso indevido realizadas
- Quantidade de tentativas corretamente bloqueadas pelo sistema

Será considerado bloqueio correto quando:

- O acesso for negado
- O usuário for redirecionado para a tela de login
- O sistema exibir mensagem de permissão insuficiente
- A operação solicitada não for executada
- Não ocorrer erro interno ou exposição indevida de informações

**Ferramentas**

- Interface Web do AGIO
- Navegador Web
- Ferramentas de desenvolvedor do navegador (DevTools)
- Logs da aplicação
- Logs do servidor

---

## Cronograma de Avaliação

O cronograma abaixo faz parte do planejamento da Fase 3 e define as datas previstas para a execução das atividades de coleta e análise da característica de **Confiabilidade** durante a [Fase 4](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase4/2-confiabilidade/#m22-taxa-de-protecao-contra-acesso-indevido-tpai). Nesta etapa, realiza-se apenas o planejamento da agenda de avaliação; a coleta efetiva dos dados, o cálculo das métricas, a comparação com os critérios estabelecidos e o julgamento dos resultados serão realizados posteriormente na Fase 4.

Toda a execução está prevista para ocorrer no período de **06/06/2026 a 12/06/2026**.

<p align="center"><strong>Tabela 2: Cronograma de Execução da Avaliação de Confiabilidade</strong></p>

| Etapa | Atividades | Métricas | Responsável | Data Realizada |
|--------|--------|--------|--------|--------|
| 1 | Preparação do ambiente de testes: inicialização do AGIO, configuração do banco de dados e validação do acesso ao sistema | — | Arthur Guilherme e João Igor | 06/06/2026 |
| 2 | Definição e organização dos cenários de teste para as funcionalidades principais do sistema | TFF, TOBS | Arthur Guilherme | 07/06/2026 |
| 3 | Execução dos testes de maturidade: login, cadastro, edição, remoção, consulta de inventário e exportação CSV | TFF, TOBS | João Igor | 07/06/2026 |
| 4 | Registro e análise das falhas observadas e cálculo da Taxa de Falhas Funcionais e da Taxa de Operações Bem-Sucedidas | TFF, TOBS | Arthur Guilherme, João Igor Tiago Lemes | 08/06/2026 |
| 5 | Execução dos testes de tratamento de entradas inválidas: campos vazios, formatos incorretos, valores inválidos, duplicidades e caracteres especiais | TTEI | Arthur Guilherme e João Igor | 11/06/2026 |
| 6 | Execução dos testes de proteção contra acesso indevido: acesso sem autenticação, acesso direto por URL, sessão expirada e operações sem permissão | TPAI | Arthur Guilherme e João Igor | 11/06/2026 |
| 7 | Consolidação dos dados coletados, cálculo das métricas, análise dos resultados e elaboração do relatório final da avaliação | TFF, TOBS, TTEI, TPAI  | Arthur Guilherme, João Igor e Tiago Lemes | 12/06/2026 |

<p align="center"><em>Autores: Arthur Guilherme, João Igor e Tiago Lemes</em></p>

---

## Conclusão

O planejamento apresentado nesta fase foi elaborado com base nas métricas, hipóteses e critérios de avaliação definidos na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/). Os cenários de teste, métodos de coleta e ferramentas selecionadas permitem a obtenção dos dados necessários para o cálculo das métricas de Taxa de Falhas Funcionais, Taxa de Operações Bem-Sucedidas, Taxa de Tratamento de Entradas Inválidas e Taxa de Proteção Contra Acesso Indevido.

Dessa forma, a execução prevista nesta fase garante que os resultados obtidos posteriormente possam ser comparados diretamente aos critérios estabelecidos na Fase 2, assegurando a rastreabilidade e a consistência da avaliação da Confiabilidade do sistema AGIO.

---

## Referências Bibliográficas

> ISO/IEC. ISO/IEC 25010:2011 – S**ystems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models**. Geneva: International Organization for Standardization, 2011.
>
> PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de software: uma abordagem profissional**. 9. ed. Porto Alegre: AMGH, 2021.
>
> SOMMERVILLE, Ian. **Engenharia de software**. 10. ed. São Paulo: Pearson, 2019.

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |  |  |
| 02 | Documentação inicial das métricas e das ferramentas e métodos de Coleta | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 03/06/2026 |  |  |
