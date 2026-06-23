# Fase 4 - Adequação Funcional

## Procedimento Executado

A avaliação da Adequação Funcional do sistema AGIO foi conduzida com base na abordagem GQM (Goal-Question-Metric) definida na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/1-adequacao_funcional/) e no plano de coleta estabelecido na [Fase 3](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase3/1-adequacao_funcional/). O procedimento consistiu em três frentes principais de investigação:

1. **Análise Documental e do Repositório**: Foi realizada a análise de funcionalidades (mapeamento) a partir do documento de backlog presente no repositório do AGIO. Esta etapa teve como foco identificar todas as funcionalidades especificadas para o sistema. 

2. **Inspeção e Verificação das Funcionalidades**: Consistiu na validação da aplicação e do código-fonte. A partir das funcionalidades do backlog, foi extraído todas as funcionalidades planejadas para o sistema. O intuito dessa etapa foi comprovar a existência dessas funções no sistema, o funcionamento adequado de suas operações sem erros de lógica e a utilidade destas para o contexto do domínio do software.

3. **Execução de Cenários de Teste (Simulação de Uso Real)**: Para avaliar a correção funcional de maneira prática e próxima à realidade, conduzimos testes simulando interações reais com o sistema. Desenhamos dois cenários principais:
   * **Perfil 1 - Administrador de Estoque (Fluxo Principal):** Simulamos a rotina de um funcionário que precisa gerenciar o armazém. O passo a passo envolveu acessar a página de login (`/login/`), inserir usuário e senha, e navegar até o inventário. Lá, simulamos o clique no botão negro "Adicionar Item", preenchendo o formulário do modal (nome, quantidade, categoria, descrição e preço) e salvando. Por fim, testamos a extração de relatórios clicando no ícone de download na tabela de produtos. A expectativa era que tudo ocorresse sem erros, fechando o modal, exibindo uma notificação de sucesso, atualizando a tabela na tela e baixando o arquivo `dashboard.csv` corretamente.
   * **No fluxo do Administrador (Convergente):** Tudo funcionou como esperado. O login processou os dados com sucesso. Ao adicionar o produto, a interface disparou um alerta nativo ("Produto adicionado com sucesso!") e, ao clicar em OK, o modal fechou e a página atualizou os dados em tempo real (via `location.reload()`). A exportação do CSV também ocorreu perfeitamente, gerando um arquivo legível no Excel/Calc.

<p align="center"><strong>Figura 1: Dashboard — Inventário de Estoque</strong></p>

![Dashboard do AGIO](../imagens/fase%204/agio-dashboard.png)

<p align="center"><em>Autores: <a href="https://github.com/redjsun">Yzabella Miranda</a></em></p>

<p align="center"><strong>Figura 2: Modal de Adição de Novo Produto</strong></p>

![Adição de Item no AGIO](../imagens/fase%204/agio-adicaoItem.png)

<p align="center"><em>Autores: <a href="https://github.com/redjsun">Yzabella Miranda</a></em></p>

<p align="center"><strong>Figura 3: Tabela Atualizada após Adição</strong></p>

![Tabela Atualizada](../imagens/fase%204/agio-tabelaAtualizada.png)

<p align="center"><em>Autores: <a href="https://github.com/redjsun">Yzabella Miranda</a></em></p>

<p align="center"><strong>Figura 4: Exportação de Relatório CSV</strong></p>

![Exportação CSV](../imagens/fase%204/agio-exportaCSV.png)

<p align="center"><em>Autores: <a href="https://github.com/redjsun">Yzabella Miranda</a></em></p>

   * **Perfil 2 - Usuário Não Autenticado (Teste de Invasão/Segurança):** Simulamos uma pessoa mal-intencionada tentando acessar os dados da empresa sem ter uma conta. O teste consistiu em abrir uma aba anônima e colar o link de download direto (`http://127.0.0.1:8000/dashboard/export/csv/`). O comportamento esperado era que o sistema bloqueasse imediatamente essa tentativa (erro 401/403) e forçasse o redirecionamento para a tela de login.
   **Análise e Comparação das Saídas (O que observamos na prática):**
   * **No cenário de Segurança (Divergente e Crítico):** O sistema falhou ao validar a sessão. Ao tentar acessar a rota de exportação pela aba anônima, a aplicação não barrou a requisição. Em vez disso, abriu a interface do Django REST Framework (status 200 OK) e expôs abertamente todos os registros do banco de dados na tela (ex: `{"csv_data": "ID,Nome,Descrição,Preço\r\n..."}`). Isso resultou em uma quebra de sigilo da aplicação, evidenciando a falta de proteção nas rotas da API.

<p align="center"><strong>Figura 5: Acesso Não Autenticado — Dados Expostos em Modo Anônimo</strong></p>

![Modo Anônimo - Falha de Segurança](../imagens/fase%204/agio-modoAnonimo.png)

<p align="center"><em>Autor: <a href="https://github.com/redjsun">Yzabella Miranda</a></em></p>


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

<p align="center"><em>Autores: Yzabella Miranda </em></p>

**Resultado da Métrica:**

- **Funcionalidades Especificadas (FE):** 20
- **Funcionalidades Implementadas (FI):** 8

> -  CF = (8/20) x 100 = 40%

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

<p align="center"><em>Autores: Yzabella Miranda </em></p>

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

> - PF = (20/20) x 100 = 100%

## Análise e Julgamento

O AGIO demonstra alinhamento parcial com os objetivos de um sistema de gerenciamento de estoque. Os resultados indicam que, embora o sistema apresente boa aderência funcional ao domínio proposto, ainda existem lacunas importantes na implementação de funcionalidades essenciais e na robustez da execução das operações.

Além disso, observa-se que o sistema apresenta inconsistências relevantes na camada de execução das funcionalidades e limitações no atendimento completo do escopo definido, o que impacta diretamente sua avaliação global de adequação funcional.

### Respostas às Questões GQM

**Q1. O AGIO possui todas as funcionalidades necessárias para atender aos objetivos de gerenciamento de inventário propostos pelo projeto?**<br>
**Resposta:** Apenas 40% das funcionalidades especificadas estão implementadas no sistema. Como o valor obtido é inferior ao critério estabelecido (< 70%), o resultado é classificado como baixa completude funcional, refutando a hipótese H1.

**Q2. As funcionalidades implementadas pelo AGIO produzem resultados corretos durante sua execução?**<br>
**Resposta:** 87,5% das funcionalidades apresentaram execução correta, enquadrando-se no nível de média correção funcional (80%–95%). Dessa forma, a hipótese H2 é confirmada em nível intermediário de correção funcional.

**Q3. As funcionalidades implementadas são adequadas para apoiar as atividades de gerenciamento de inventário propostas pelo sistema?**<br>
**Resposta:** 100% das funcionalidades avaliadas são pertinentes ao domínio de gestão de estoque. O resultado atende plenamente ao critério estabelecido (> 90%), confirmando a hipótese H3.

### Resumo dos Resultados

<p align="center"><strong>Tabela 3: Resumo dos Resultados das Métricas</strong></p>

| Métrica | Objetivo | Valor Obtido | Critério Desejado (Alta) | Resultado da Hipótese |
|---------|----------|:------------:|:-----------------:|:--------------------:|
| M1.1 Taxa de Completude Funcional | Medir a taxa de funções implementadas frente às especificadas. | 40% | > 90% | **H1 REFUTADA** |
| M2.1 Taxa de Correção Funcional | Medir se as funções estão entregando resultados livres de erros lógicos. | 87.5% | > 95% | **H2 CONFIRMADA EM NÍVEL DE CORREÇÃO MÉDIO** |
| M3.1 Taxa de Pertinência Funcional | Medir a relevância do escopo implementado. | 100% | > 90% | **H3 CONFIRMADA EM NÍVEL DE PERTINÊNCIA ALTA** |

<p align="center"><em>Autores: Yzabella Miranda </em></p>

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |   [João Igor](https://github.com/JoaoPC10)| 12/06/2026  |
| 02 | Atualização do documento com a explicação do procedimento executado, medição e análise | [Yzabella Pimenta](https://github.com/redjsun) | 12/06/2026 | [Tiago Lemes](https://github.com/TiagoTeixeira-2005)  | 12/06/2026 |
| 03 | Adição de imagem dos casos de testes | [Yzabella Pimenta](https://github.com/redjsun) | 21/06/2026 | [Tiago Lemes](https://github.com/TiagoTeixeira-2005)  | 22/06/2026 |
