# Fase 3 - Adequação Funcional

## Introdução

A Adequação Funcional é uma das características de qualidade definidas pela norma ISO/IEC 25010 e refere-se ao grau em que um produto de software fornece funções que atendem às necessidades explícitas e implícitas dos usuários quando utilizado sob condições específicas. Essa característica busca verificar se as funcionalidades disponibilizadas pelo sistema são suficientes para atender aos objetivos propostos, produzem resultados corretos e contribuem para a realização das tarefas esperadas pelos usuários.

De acordo com a ISO/IEC 25010, a Adequação Funcional é composta por três subcaracterísticas:

- **Completude Funcional (Functional Completeness):** avalia se o conjunto de funcionalidades cobre todas as tarefas e objetivos especificados para o sistema;
- **Correção Funcional (Functional Correctness):** verifica se as funcionalidades fornecem resultados corretos e precisos;
- **Pertinência Funcional (Functional Appropriateness):** analisa se as funcionalidades facilitam a realização das tarefas para as quais foram projetadas.

No contexto da Aplicação de Gestão de Inventário Otimizada (AGIO), a avaliação dessa característica tem como objetivo verificar se as funcionalidades implementadas são suficientes para atender às necessidades de gerenciamento de inventário propostas pelo projeto. Entre essas funcionalidades estão o controle de acesso por usuários, gerenciamento de itens do inventário, visualização dos dados cadastrados e exportação das informações para arquivos CSV.

---

## Métricas a Serem Implementadas

A avaliação da Adequação Funcional será realizada considerando as três subcaracterísticas definidas pela ISO/IEC 25010.

### M1 - Taxa de Completude Funcional

Avalia a proporção de funcionalidades implementadas em relação ao conjunto de funcionalidades especificadas na documentação do projeto.

**Fórmula:**

> - CF = (FI/FE) x 100

Onde:

- **FI** = Quantidade de funcionalidades implementadas;
- **FE** = Quantidade de funcionalidades especificadas.

### M2 - Taxa de Correção Funcional

Avalia a proporção de funcionalidades que executam corretamente suas operações durante a verificação do sistema.

**Fórmula:**

> - COR = (FC/FV) x 100

Onde:

- **FC** = Quantidade de funcionalidades funcionando corretamente;
- **FV** = Quantidade de funcionalidades verificadas.

### M3 - Taxa de Pertinência Funcional

Avalia a proporção de funcionalidades que contribuem diretamente para os objetivos de gerenciamento de inventário propostos pelo sistema.

**Fórmula:**

> - PF = (FP/FT) x 100

Onde:

- **FP** = Quantidade de funcionalidades consideradas pertinentes aos objetivos do sistema;
- **FT** = Quantidade total de funcionalidades avaliadas.

### Critérios de Avaliação

A tabela abaixo foi elaborada com base nos critérios estabelecidos na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/). Os resultados obtidos serão utilizados para verificar o grau de aderência do AGIO aos requisitos funcionais definidos para o projeto.


<p align="center"><strong>Tabela 1: Critérios de Aceitação</strong></p>

| Métrica | Critério Desejado (Alta Completude/Correção/Pertinência) |
|----------|----------|
| M1 - Taxa de Completude Funcional | ≥ 90% |
| M2 - Taxa de Correção Funcional | ≥ 95% |
| M3 - Taxa Pertinência Funcional | ≥ 90% |

<p align="center"><em>Autores: Letícia da Silva, Vitor Pereira e Yzabella Miranda</em></p>

---

## Ferramentas e Métodos de Coleta

A coleta dos dados será realizada por meio da análise documental e da inspeção das funcionalidades implementadas no sistema.

### Análise da Documentação

Serão analisados os artefatos disponíveis no repositório do projeto para identificar os requisitos e funcionalidades previstas para o sistema. Entre os documentos analisados estão:

- README do projeto;
- Documentação técnica disponível;
- Backlog do projeto;
- Issues cadastradas no GitHub;
- Pull Requests relacionados à implementação de funcionalidades.

### Verificação das Funcionalidades

Será realizada uma inspeção das funcionalidades implementadas na aplicação para verificar sua existência e aderência aos requisitos identificados na documentação.

As principais funcionalidades avaliadas incluem:

- Criação e autenticação de usuários;
- Controle de acesso ao sistema;
- Cadastro de itens no inventário;
- Edição de itens;
- Remoção de itens;
- Visualização do inventário;
- Exportação de dados em formato CSV.

Durante a avaliação serão registrados:

- Funcionalidades especificadas;
- Funcionalidades implementadas;
- Funcionalidades ausentes;
- Funcionalidades com comportamento incorreto;
- Evidências encontradas no sistema e no repositório.

### Inspeção do Repositório

Também serão utilizados dados obtidos diretamente do repositório GitHub do projeto, incluindo:

- Histórico de Issues;
- Pull Requests;
- Commits relacionados às funcionalidades avaliadas;
- Casos de teste automatizados existentes.

Essas informações servirão como evidências para apoiar a análise da completude, correção e pertinência funcional do sistema.

---

## Cronograma de Avaliação

O cronograma abaixo faz parte do planejamento da Fase 3 e define as datas previstas para a execução das atividades de coleta e análise da característica de **Adequação Funcional** durante a [Fase 4](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase4/1-adequacao_funcional/). Nesta etapa, realiza-se apenas o planejamento da agenda de avaliação; a coleta efetiva dos dados, o cálculo das métricas, a comparação com os critérios estabelecidos e o julgamento dos resultados serão realizados posteriormente na Fase 4.

Toda a execução está prevista para ocorrer no período de **06/06/2026 a 12/06/2026**.

<p align="center"><strong>Tabela 2: Cronograma de Execução da Avaliação de Adequação Funcional</strong></p>

| Etapa | Atividades | Métricas | Responsável | Data Realizada |
|--------|--------|--------|--------|--------|
| 1 | Preparação do ambiente de avaliação: acesso ao repositório do AGIO, levantamento do backlog do produto e configuração da aplicação para inspeção | — | Yzabella Miranda | 06/06/2026 |
| 2 | Análise documental do backlog e identificação das funcionalidades especificadas para o sistema | CF | Yzabella Miranda | 06/06/2026 |
| 3 | Inspeção do código-fonte e da aplicação para verificar a implementação das funcionalidades especificadas | CF | Yzabella Miranda | 07/06/2026 |
| 4 | Mapeamento das funcionalidades implementadas e cálculo da Completude Funcional (CF) | CF | Yzabella Miranda | 07/06/2026 |
| 5 | Execução dos cenários de teste do Perfil 1 (Administrador de Estoque), avaliando login, gerenciamento de produtos e exportação CSV | COR | Yzabella Miranda | 10/06/2026 |
| 6 | Execução dos cenários de teste do Perfil 2 (Usuário Não Autenticado), avaliando autenticação, controle de acesso e proteção das rotas da aplicação | COR | Yzabella Miranda | 10/06/2026 |
| 7 | Análise dos resultados dos testes, avaliação da Pertinência Funcional (PF), cálculo das métricas e consolidação do relatório final | CF, COR, PF | Yzabella Miranda | 12/06/2026 |

<p align="center"><em>Autor: Yzabella Miranda</em></p>

---

### Conclusão

O planejamento apresentado nesta fase foi elaborado com base nas métricas, hipóteses e critérios de avaliação definidos na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/). Os métodos de coleta, as fontes de evidência e os procedimentos de inspeção selecionados permitem a obtenção dos dados necessários para o cálculo das métricas de **Completude Funcional, Correção Funcional e Pertinência Funcional**.

Dessa forma, a execução prevista nesta fase garante que os resultados obtidos posteriormente possam ser comparados diretamente aos critérios estabelecidos na Fase 2, assegurando a rastreabilidade e a consistência da avaliação da Adequação Funcional do sistema AGIO.

---

## Referências Bibliográficas

ISO/IEC. **ISO/IEC 25010:2011 – Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models**. Geneva: International Organization for Standardization, 2011.

PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de Software: uma abordagem profissional**. 9. ed. Porto Alegre: AMGH, 2021.

SOMMERVILLE, Ian. **Engenharia de Software**. 10. ed. São Paulo: Pearson, 2019.

---

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |  [João Igor](https://github.com/JoaoPC10)| 12/06/2026 |
| 02 | Elaboração da Fase 3 - Adequação Funcional | [Letícia Monteiro](https://github.com/LeticiaMonteiroo) | 08/06/2026 |  [João Igor](https://github.com/JoaoPC10)| 12/06/2026  |
