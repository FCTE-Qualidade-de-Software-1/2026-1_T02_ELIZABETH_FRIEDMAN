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

**Fórmula**

> - Taxa de Falhas = (N° de falhas / N° total de operações) x 100

**Ferramentas**

- Interface Web do AGIO
- Logs da aplicação
- Logs do terminal

#### Métrica 1.2: Taxa de Operações Bem-Sucedidas

Tem como objetivo avaliar o percentual de operações concluídas corretamente pelo sistema.

**Método de Coleta**

Executar o mesmo conjunto de operações da Métrica 1.1:

- Login
- Cadastro de itens
- Edição de itens
- Remoção de itens
- Consulta de inventário
- Exportação CSV

Registrar:

- Quantidade total de operações executadas;
- Quantidade de operações concluídas sem ffalhas.

Serão consideradas falhas:

- Erro 500
- Travamentos
- Funcionalidades indisponíveis
- Comportamentos incorretos
- Operações que não produzem o resultado esperado

**Fórmula**

> - Taxa de Sucesso= (N° de operações concluídas com sucesso / N° total de operações) x 100

**Ferramentas**

- Interface Web do AGIO
- Logs da aplicação
- Logs do terminal

#### Métrica 2.1: Taxa de Tratamento de Entradas Inválidas

Tem como objetivo avaliar a capacidade do AGIO de lidar adequadamente com entradas incorretas sem interromper sua execução.

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

**Fórmula**

> - Taxa de Tratamento= (N° de entradas inválidas tratadas / N° total de entradas inválidas) x 100

**Ferramentas**

- Interface Web do AGIO
- Logs da aplicação

#### Métrica 2.2: Taxa de Proteção Contra Acesso Indevido

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

**Fórmula**

> - Taxa de Proteção= (N° de tentativas bloqueadas / N° total de tentativas indevidas) x 100

**Ferramentas**
- Interface Web do AGIO
Navegador Web;
Ferramentas de desenvolvedor do navegador (DevTools);
Logs da aplicação;
Logs do servidor.

## Localização dos Dados de Avaliação


## Referências Bibliográficas

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |  |  |
| 02 | Documentação inicial das métricas e das erramentas e métodos de Coleta | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 03/06/2026 |  |  |
