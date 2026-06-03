# Fase 3 - Confiabilidade

## Introdução

Nesta etapa do projeto, será especificado como serão implementadas e executadas as métricas definidas pela abordagem **Goal-Question-Metric (GQM)** para avaliar objetivamente a característica de Confiabilidade do **sistema AGIO**.

A avaliação será realizada em um ambiente local Linux, utilizando a aplicação AGIO em execução, o navegador web para interação com a interface e ferramentas de monitoramento e registro de logs do sistema. Os testes contemplarão operações fundamentais do sistema, como autenticação, cadastro, edição, remoção e consulta de itens do inventário, além da exportação de dados em formato CSV.

Serão executados cenários normais de uso e cenários com entradas inválidas e comportamentos inesperados, permitindo medir a frequência de falhas e a capacidade do sistema de lidar adequadamente com situações adversas. Os resultados coletados serão utilizados para o cálculo das métricas definidas na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/), garantindo rastreabilidade e reprodutibilidade da avaliação.

## Métricas a Serem Implementadas

Com base no planejamento realizado ma [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/), serão coletados dados para as seguintes métricas:

**Maturidade**

- **Métrica 1.1:** Taxa de Falhas Funcionais
- **Métrica 1.2:** Taxa de Operações Bem-Sucedidas

**Tolerância a Falhas**

- **Métrica 2.1:** Taxa de Tratamento de Entradas Inválidas
- **Métrica 2.2:** Taxa de Continuidade Operacional após Erros

## Ferramentas e Métodos de Coleta

Abaixo, estão especificados o ambiente de teste, os instrumentos de medição utilizados e o passo a passo realizado para a coleta dos dados.

### Ambiente de Teste

- **Sistema Operacional:** Ubuntu X.X LTS (ou distribuição Linux equivalente)
- **Aplicação Avaliada:** AGIO
- **Banco de Dados:** PostgreSQL (conforme configuração do projeto)
- **Navegador:** Google Chrome ou Mozilla Firefox
- **Hardware Utilizado:**
  - *CPU:* X núcleos ou superior
  - *Memória RAM:* X GB ou superior
  - Armazenamento X
- **Pré-requisitos:**
  - Ambiente local do AGIO configurado e funcional
  = Banco de dados inicializado
  - Usuário administrador cadastrado
  - Inventário contendo registros para teste

### Instrumentos de Medição

#### Métrica 1.1: Taxa de Falhas Funcionais

**Método de Coleta**

**Fórmula**

**Ferramentas**

#### Métrica 1.2: Taxa de Operações Bem-Sucedidas

**Método de Coleta**

**Fórmula**

**Ferramentas**

#### Métrica 2.1: Taxa de Tratamento de Entradas Inválidas

**Método de Coleta**

**Fórmula**

**Ferramentas**

#### Métrica 2.2: Taxa de Continuidade Operacional após Erros

**Método de Coleta**

**Fórmula**

**Ferramentas**

## Localização dos Dados de Avaliação

## Referências Bibliográficas

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |  |  |
| 02 | Documentação inicial das métricas e das erramentas e métodos de Coleta | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 03/06/2026 |  |  |
