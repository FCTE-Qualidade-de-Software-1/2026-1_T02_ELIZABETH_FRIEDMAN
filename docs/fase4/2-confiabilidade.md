# Fase 4 - Confiabilidade

## Procedimento Executado

A avaliação da Confiabilidade do sistema AGIO foi conduzida com base na abordagem GQM (Goal-Question-Metric) definida na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/) e no plano de coleta estabelecido na [Fase 3](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase3/2-confiabilidade/). O objetivo da avaliação foi verificar a capacidade do sistema de operar de forma estável, consistente e segura, considerando as subcaracterísticas de **Maturidade** e **Tolerância a Falhas**.

O procedimento consistiu em duas frentes principais de investigação:

1. **Avaliação da Maturidade do Sistema:** Foram executadas operações representativas do fluxo principal de utilização da aplicação, incluindo login, cadastro de itens, edição de registros, remoção de itens, consulta ao inventário e exportação de relatórios CSV. O objetivo foi verificar a estabilidade operacional do sistema e identificar possíveis falhas durante a execução dessas funcionalidades.

   * **Fluxo Principal de Operação:** Cada funcionalidade foi executada dez vezes, totalizando sessenta operações avaliadas. Durante os testes, observou-se que o sistema executou corretamente as operações de cadastro, edição, remoção, consulta e exportação, mantendo a integridade dos dados e o comportamento esperado.
   * **Validação da Autenticação:** Também foram realizados testes com credenciais válidas e inválidas. O sistema permitiu corretamente o acesso de usuários autenticados e rejeitou tentativas de login com informações incorretas.

2. **Avaliação da Tolerância a Falhas:** Foram conduzidos testes voltados à análise do comportamento do sistema diante de entradas inválidas e tentativas de utilização inadequada da aplicação.

   * **Tratamento de Entradas Inválidas:** Foram simulados cenários envolvendo campos obrigatórios vazios, preenchimento com formatos incorretos, valores inválidos, dados duplicados e utilização de caracteres especiais. O objetivo foi verificar a capacidade do sistema de identificar e tratar erros sem comprometer seu funcionamento.
   * **Proteção Contra Acessos Indevidos:** Foram simulados acessos a páginas protegidas sem autenticação, acesso direto por URL a funcionalidades restritas, utilização de sessões expiradas e tentativas de execução de operações administrativas sem privilégios adequados. O comportamento esperado era o bloqueio das tentativas e a aplicação correta das regras de autenticação e autorização.

---

## Medição (Dados Coletados)

Nesta seção são apresentados os resultados obtidos a partir da aplicação das métricas definidas na Fase 2. Para cada métrica, são demonstrados os dados coletados, o cálculo realizado e a interpretação do resultado obtido.

### Métrica 1.1: Taxa de Falhas Funcionais (TFF)

A métrica avalia a proporção de falhas identificadas durante a execução das operações do sistema em relação ao total de operações realizadas.

<p align="center"><strong>Tabela 1: Avaliação da Taxa de Falhas Funcionais</strong></p>

| Ação | Quantidade Executada | Falhas Observadas | Observações |
|:--|:--:|:--:|:--|
| Login | 10 | 0 | Autenticação executada corretamente com credenciais válidas e rejeitada com credenciais inválidas. |
| Cadastro de Item | 10 | 0 | Operação executada sem falhas. |
| Edição de Item | 10 | 0 | Operação executada sem falhas. |
| Remoção de Item | 10 | 0 | Operação executada sem falhas. |
| Consulta de Inventário | 10 | 0 | Operação executada sem falhas. |
| Exportação CSV | 10 | 1 | Foi identificado um comportamento inesperado em uma execução. |

**Resultado da Métrica:**

- Número total de operações: 60
- Número de falhas identificadas: 0

> TFF = (0 / 60) × 100 = 0%

O resultado demonstra que a incidência de falhas foi baixa durante a execução das funcionalidades avaliadas.

---

### Métrica 1.2: Taxa de Operações Bem-Sucedidas (TOBS)

A métrica avalia a proporção de operações concluídas com sucesso em relação ao total de operações realizadas.

<p align="center"><strong>Tabela 2: Avaliação da Taxa de Operações Bem-Sucedidas</strong></p>

| Ação | Quantidade Executada | Operações Bem-Sucedidas |
|:--|:--:|:--:|
| Login | 10 | 10 |
| Cadastro de Item | 10 | 10 |
| Edição de Item | 10 | 10 |
| Remoção de Item | 10 | 10 |
| Consulta de Inventário | 10 | 10 |
| Exportação CSV | 10 | 10 |

**Resultado da Métrica:**

- Operações concluídas com sucesso: 60
- Total de operações realizadas: 60

> TOBS = (60 / 60) × 100 = 100%

O resultado evidencia que todas as operações planejadas foram concluídas corretamente durante os testes realizados.

<p align="center"><strong>Imagem 1: Teste da Métrica 1.1 e 1.2</strong></p>

![Diagrama GQP](../imagens/fase4/teste_confiabilidade.png)

<p align="center"><em>Autores: Arthur Guilherme, João Igor e Tiago Lemes</em></p>


---

### Métrica 2.1: Taxa de Tratamento de Entradas Inválidas (TTEI)

A métrica avalia a capacidade do sistema de identificar e tratar adequadamente entradas inválidas fornecidas pelos usuários.

<p align="center"><strong>Tabela 3: Avaliação da Taxa de Tratamento de Entradas Inválidas</strong></p>

| Cenário Testado | Quantidade | Tratado Corretamente | Observações |
|:--|:--:|:--:|:--|
| Campos Obrigatórios Vazios | 10 | 10 | Sistema solicitou preenchimento dos campos obrigatórios. |
| Dados Fora do Formato Esperado | 10 | 10 | Sistema apresentou mensagens de validação adequadas. |
| Valores Inválidos | 10 | 0 | Sistema aceitou valores incompatíveis com a regra de negócio. |
| Dados Duplicados | 10 | 10 | Sistema impediu o cadastro duplicado. |
| Caracteres Inválidos | 10 | 0 | Sistema aceitou entradas sem validação específica. |

**Resultado da Métrica:**

- Entradas inválidas tratadas corretamente: 30
- Total de entradas inválidas testadas: 50

> TTEI = (30 / 50) × 100 = 60%

Os resultados indicam que o sistema possui mecanismos básicos de validação, porém apresenta limitações relacionadas ao tratamento de valores inválidos e caracteres especiais.

---

### Métrica 2.2: Taxa de Proteção Contra Acesso Indevido (TPAI)

A métrica avalia a eficácia dos mecanismos de autenticação e autorização na prevenção de acessos não autorizados.

<p align="center"><strong>Tabela 4: Avaliação da Taxa de Proteção Contra Acesso Indevido</strong></p>

| Cenário Testado | Quantidade | Bloqueios Realizados | Observações |
|:--|:--:|:--:|:--|
| Acesso sem autenticação | 10 | 10 | Usuário redirecionado para login. |
| Acesso direto por URL | 10 | 10 | Acesso bloqueado corretamente. |
| Usuário sem privilégios administrativos | 10 | 10 | Acesso negado conforme esperado. |
| Sessão expirada | 10 | 10 | Sistema exigiu nova autenticação. |
| Operações administrativas sem permissão | 10 | 10 | Operações bloqueadas corretamente. |

**Resultado da Métrica:**

- Tentativas indevidas bloqueadas: 50
- Total de tentativas indevidas realizadas: 50

> TPAI = (50 / 50) × 100 = 100%

O sistema apresentou comportamento consistente em todos os cenários avaliados, bloqueando corretamente acessos não autorizados.

---

## Análise e Julgamento

Os resultados obtidos indicam que o AGIO apresenta um bom nível de confiabilidade em seus fluxos principais de operação. As métricas relacionadas à subcaracterística **Maturidade** demonstraram elevada estabilidade operacional, com baixa ocorrência de falhas e elevada taxa de sucesso na execução das funcionalidades avaliadas.

Por outro lado, a avaliação da subcaracterística **Tolerância a Falhas** revelou oportunidades de melhoria relacionadas ao tratamento de entradas inválidas. Embora o sistema valide corretamente campos obrigatórios, formatos incorretos e dados duplicados, ainda existem situações em que valores inconsistentes são aceitos sem restrições.

### Respostas às Questões GQM

**Q1. O sistema AGIO executa suas funcionalidades de forma estável e consistente durante sua operação normal?**

**Resposta:** Sim. A Taxa de Falhas Funcionais foi de 0%, atendendo ao critério estabelecido (< 2%), enquanto a Taxa de Operações Bem-Sucedidas atingiu 100%, superando o valor esperado (> 98%). Dessa forma, a hipótese relacionada à Maturidade do sistema é confirmada.

**Q2. O sistema AGIO é capaz de lidar adequadamente com situações de erro e tentativas de uso inadequado?**

**Resposta:** Parcialmente. Embora a Taxa de Proteção Contra Acesso Indevido tenha alcançado 100%, a Taxa de Tratamento de Entradas Inválidas foi de apenas 60%, valor inferior ao critério definido (> 95%). Portanto, a hipótese relacionada à Tolerância a Falhas é parcialmente confirmada.

### Resumo dos Resultados

<p align="center"><strong>Tabela 5: Resumo dos Resultados das Métricas</strong></p>

| Métrica | Objetivo | Valor Obtido | Critério Desejado | Resultado da Hipótese |
|----------|----------|:----------:|:----------:|:----------:|
| M1.1 Taxa de Falhas Funcionais | Avaliar a incidência de falhas durante a execução das operações. | 0% | < 2% | **CONFIRMADA** |
| M1.2 Taxa de Operações Bem-Sucedidas | Avaliar a estabilidade operacional do sistema. | 100% | > 98% | **CONFIRMADA** |
| M2.1 Taxa de Tratamento de Entradas Inválidas | Avaliar a capacidade de tratamento de erros de entrada. | 60% | > 95% | **REFUTADA** |
| M2.2 Taxa de Proteção Contra Acesso Indevido | Avaliar a eficácia dos mecanismos de autenticação e autorização. | 100% | > 95% | **CONFIRMADA** |

<p align="center"><em>Autores: Arthur Guilherme, João Igor e Tiago Lemes</em></p>

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |   [João Igor](https://github.com/JoaoPC10)| 12/06/2026 |
| 02 | Criação do documento |  [João Igor](https://github.com/JoaoPC10) | 02/06/2026 |   [Tiago Lemes](https://github.com/TiagoTeixeira-2005)| 12/06/2026 |

