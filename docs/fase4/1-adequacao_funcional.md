# Fase 4 - Adequação Funcional

## Procedimento Executado

A avaliação da Adequação Funcional do sistema AGIO foi conduzida com base na abordagem GQM (Goal-Question-Metric) definida na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/1-adequacao_funcional/) e no plano de coleta estabelecido na [Fase 3](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase3/1-adequacao_funcional/). O procedimento consistiu em três frentes principais de investigação:

1. **Análise Documental e do Repositório**: Foi realizada a análise de funcionalidades (mapeamento) a partir do documento de backlog presente no repositório do AGIO. Esta etapa teve como foco identificar todas as funcionalidades especificadas para o sistema. 

2. **Inspeção e Verificação das Funcionalidades**: Consistiu na validação da aplicação e do código-fonte. A partir das funcionalidades do backlog, foi extraído todas as funcionalidades planejadas para o sistema. O intuito dessa etapa foi comprovar a existência dessas funções no sistema, o funcionamento adequado de suas operações sem erros de lógica e a utilidade destas para o contexto do domínio do software.

3. **Execução de Cenários de Teste (Simulação de Uso Real)**: Para avaliar a correção funcional de maneira prática e próxima à realidade, conduzimos testes simulando interações reais com o sistema. Desenhamos dois cenários principais:
   * **Perfil 1 - Administrador de Estoque (Fluxo Principal):** Simulamos a rotina de um funcionário que precisa gerenciar o armazém. O passo a passo envolveu acessar a página de login (`/login/`), inserir usuário e senha, e navegar até o inventário. Lá, simulamos o clique no botão negro "Adicionar Item", preenchendo o formulário do modal (nome, quantidade, categoria, descrição e preço) e salvando. Por fim, testamos a extração de relatórios clicando no ícone de download na tabela de produtos. A expectativa era que tudo ocorresse sem erros, fechando o modal, exibindo uma notificação de sucesso, atualizando a tabela na tela e baixando o arquivo `dashboard.csv` corretamente.
   * **No fluxo do Administrador (Convergente):** Tudo funcionou como esperado. O login processou os dados com sucesso. Ao adicionar o produto, a interface disparou um alerta nativo ("Produto adicionado com sucesso!") e, ao clicar em OK, o modal fechou e a página atualizou os dados em tempo real (via `location.reload()`). A exportação do CSV também ocorreu perfeitamente, gerando um arquivo legível no Excel/Calc.
   * **Perfil 2 - Usuário Não Autenticado (Teste de Invasão/Segurança):** Simulamos uma pessoa mal-intencionada tentando acessar os dados da empresa sem ter uma conta. O teste consistiu em abrir uma aba anônima e colar o link de download direto (`http://127.0.0.1:8000/dashboard/export/csv/`). O comportamento esperado era que o sistema bloqueasse imediatamente essa tentativa (erro 401/403) e forçasse o redirecionamento para a tela de login.
   **Análise e Comparação das Saídas (O que observamos na prática):**
   * **No cenário de Segurança (Divergente e Crítico):** O sistema falhou ao validar a sessão. Ao tentar acessar a rota de exportação pela aba anônima, a aplicação não barrou a requisição. Em vez disso, abriu a interface do Django REST Framework (status 200 OK) e expôs abertamente todos os registros do banco de dados na tela (ex: `{"csv_data": "ID,Nome,Descrição,Preço\r\n..."}`). Isso resultou em uma quebra de sigilo da aplicação, evidenciando a falta de proteção nas rotas da API.


## Medição (Dados Coletados)

### Métrica 1.1: Completude Funcional (CF)

A métrica afere o quão completas estão as funções em relação à especificação listada no documento de Backlog do Produto.

<p align="center"><strong>Tabela 1: Avaliação de Completude Funcional</strong></p>

<div align="center">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;">ID</th>
        <th style="text-align: left;">Funcionalidades</th>
        <th style="text-align: center;">Situação</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="text-align: center;">1</td><td style="text-align: left;">CRUD de Produtos</td><td style="text-align: center;">Implementado</td></tr>
      <tr><td style="text-align: center;">2</td><td style="text-align: left;">Gerenciamento com Códigos de Barra</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">3</td><td style="text-align: left;">Categorização dos Itens</td><td style="text-align: center;">Implementado</td></tr>
      <tr><td style="text-align: center;">4</td><td style="text-align: left;">Integração com Banco de Dados</td><td style="text-align: center;">Implementado</td></tr>
      <tr><td style="text-align: center;">5</td><td style="text-align: left;">Acesso à página de usuário e ao Dashboard</td><td style="text-align: center;">Implementado</td></tr>
      <tr><td style="text-align: center;">6</td><td style="text-align: left;">Informações e referências sobre a aplicação (Main Page)</td><td style="text-align: center;">Implementado</td></tr>
      <tr><td style="text-align: center;">7</td><td style="text-align: left;">Autenticação</td><td style="text-align: center;">Implementado</td></tr>
      <tr><td style="text-align: center;">8</td><td style="text-align: left;">Sistema de Permissões e de Níveis de Acesso</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">9</td><td style="text-align: left;">Sistema de Backup dos inventários e dados (Export CSV)</td><td style="text-align: center;">Implementado</td></tr>
      <tr><td style="text-align: center;">10</td><td style="text-align: left;">Dashboard Simples</td><td style="text-align: center;">Implementado</td></tr>
      <tr><td style="text-align: center;">11</td><td style="text-align: left;">Sistema de Notificação</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">12</td><td style="text-align: left;">Painel Completo de Gestão</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">13</td><td style="text-align: left;">Relatórios Personalizáveis</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">14</td><td style="text-align: left;">Controle de Múltiplos Armazéns</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">15</td><td style="text-align: left;">Classificação dos Inventários</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">16</td><td style="text-align: left;">Integração com serviços diversos</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">17</td><td style="text-align: left;">Gerenciamento de pedidos, compras e envios</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">18</td><td style="text-align: left;">Rastreamento por número serial</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">19</td><td style="text-align: left;">Integração com software CRM</td><td style="text-align: center;">Não implementado</td></tr>
      <tr><td style="text-align: center;">20</td><td style="text-align: left;">Aplicativo Desktop, Web, Android e IOS</td><td style="text-align: center;">Não implementado</td></tr>
    </tbody>
  </table>
</div>

<p align="center"><em>Autores: Yzabella Mirandas </em></p>

**Resultado da Métrica:**

- **Funcionalidades Especificadas (FE):** 20
- **Funcionalidades Implementadas (FI):** 8

> - CF = (8/20) x 100 = 40%

---

### Métrica 2.1: Correção Funcional (COR)

A avaliação da Correção Funcional exigiu a execução manual das principais operações do sistema para comprovar que as funcionalidades operam livres de erros lógicos.

A partir desses experimentos controlados de uso normal e de segurança, elaborou-se o quadro consolidado da Correção Funcional para as 8 funcionalidades efetivamente entregues no código:

<p align="center"><strong>Tabela 2: Avaliação de Correção Funcional</strong></p>

<div align="center">
  <table>
    <thead>
      <tr>
        <th style="text-align: left;">Funcionalidades Verificadas (FV)</th>
        <th style="text-align: center;">Correta? (FC)</th>
        <th style="text-align: left;">Observação Técnica</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: left;">CRUD de Produtos, Categorização, Banco de Dados, Main Page, Dashboard Simples, Acesso à Página e Backup (CSV)</td>
        <td style="text-align: center;">Sim (7 un.)</td>
        <td style="text-align: left;">As ações manipulam o banco e geram outputs sem interrupções de serviço.</td>
      </tr>
      <tr>
        <td style="text-align: left;">Autenticação</td>
        <td style="text-align: center;">Não (1 un.)</td>
        <td style="text-align: left;">Apesar de existir tela de Login, as rotas de API (<code>/product-manager/</code> e <code>/export/csv/</code>) não exigem sessão. Há quebra de segurança e acesso não autorizado aos dados.</td>
      </tr>
    </tbody>
  </table>
</div>

<p align="center"><em>Autores: Yzabella Mirandas </em></p>

**Resultado da Métrica:**

- **Funcionalidades Verificadas (FV):** 8 (considerando as 8 implementadas)
- **Funcionalidades Corretas (FC):** 7

> - COR = (7/8) x 100 = 87.5%

---

### Métrica 3.1: Pertinência Funcional (PF)

A métrica afere a proporção de funcionalidades que contribuem diretamente para os objetivos de gerenciamento de inventário propostos pelo sistema.

**Resultado da Métrica:**

- **Funcionalidades Totais (FT):** 20 (todas as funcionalidades listadas no Backlog são aderentes ao conceito de um software ERP de gestão de inventário).
- **Funcionalidades Pertinentes (FP):** 20

>  - PF = (20/20) x 100 = 100%

---

## Análise e Julgamento

O AGIO se mostrou muito consistente ao demonstrar que a equipe compreendeu exatamente as necessidades de um controle de estoque. O grande viés que compromete a entrega, contudo, é a falta de funções essenciais do backlog e uma vulnerabilidade crítica de segurança na API, que permite o acesso aos dados sem autenticação. Diante desse cenário, o software ainda não tem condições de ir para produção, sendo indispensável que a equipe priorize a proteção dessas rotas e a entrega do fluxo de criação de contas antes do lançamento.

### Respostas às Questões GQM

**Q1. O AGIO possui todas as funcionalidades necessárias para atender aos objetivos de gerenciamento de inventário propostos pelo projeto?**<br>
**Resposta:** 40% das funcionalidades especificadas estão integralmente representadas no código avaliado. Como o valor obtido ficou muito abaixo da meta (> 90%), o resultado é inaceitável e não confirma a hipótese H1 (Refutada).

**Q2. As funcionalidades implementadas pelo AGIO produzem resultados corretos durante sua execução?**<br>
**Resposta:** 87.5% das operações funcionaram livres de erros lógicos na interface. Porém, a detecção de uma grave brecha de segurança no backend afetou a métrica. O resultado é considerado de nível médio e não confirma totalmente a hipótese H2 (Parcialmente Refutada).

**Q3. As funcionalidades implementadas são adequadas para apoiar as atividades de gerenciamento de inventário propostas pelo sistema?**<br>
**Resposta:** 100% das funcionalidades entregues contribuem diretamente para o domínio de gestão de estoque. O resultado atende plenamente ao critério esperado (> 90%), confirmando de forma absoluta a hipótese H3.

### Resumo dos Resultados

<p align="center"><strong>Tabela 3: Resumo dos Resultados das Métricas</strong></p>

<div align="center">
  <table>
    <thead>
      <tr>
        <th style="text-align: left;">Métrica</th>
        <th style="text-align: left;">Objetivo</th>
        <th style="text-align: center;">Valor Obtido</th>
        <th style="text-align: center;">Critério Desejado</th>
        <th style="text-align: center;">Resultado da Hipótese</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: left;"><strong>M1.1 Completude Funcional</strong></td>
        <td style="text-align: left;">Medir a taxa de funções implementadas frente às especificadas.</td>
        <td style="text-align: center;">40%</td>
        <td style="text-align: center;">&gt; 90%</td>
        <td style="text-align: center;"><strong>H1 REFUTADA</strong></td>
      </tr>
      <tr>
        <td style="text-align: left;"><strong>M2.1 Correção Funcional</strong></td>
        <td style="text-align: left;">Medir se as funções estão entregando resultados livres de erros lógicos.</td>
        <td style="text-align: center;">87.5%</td>
        <td style="text-align: center;">&gt; 95%</td>
        <td style="text-align: center;"><strong>H2 MÉDIA</strong><br>(Parcialmente Refutada)</td>
      </tr>
      <tr>
        <td style="text-align: left;"><strong>M3.1 Pertinência Funcional</strong></td>
        <td style="text-align: left;">Medir a relevância do escopo implementado.</td>
        <td style="text-align: center;">100%</td>
        <td style="text-align: center;">&gt; 90%</td>
        <td style="text-align: center;"><strong>H3 CONFIRMADA</strong></td>
      </tr>
    </tbody>
  </table>
</div>

<p align="center"><em>Autores: Yzabella Mirandas </em></p>

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |   [João Igor](https://github.com/JoaoPC10)| 12/06/2026  |
| 02 | Atualização do documento com a explicação do procedimento executado, medição e análise | [Yzabella Pimenta](https://github.com/redjsun) | 12/06/2026 |   |  |
