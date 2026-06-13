# Fase 4 - Conclusão

## Discussão dos Resultados

A avaliação do sistema AGIO permitiu analisar duas características fundamentais da qualidade de software: **Adequação Funcional** e **Confiabilidade**. Os resultados evidenciam que o sistema possui uma base operacional funcional e estável para as atividades de gerenciamento de inventário, mas ainda apresenta limitações importantes relacionadas à cobertura dos requisitos planejados e ao tratamento de situações excepcionais.

### 1. Adequação Funcional

A análise da Adequação Funcional revelou um cenário misto entre as subcaracterísticas avaliadas.

A **Completude Funcional** apresentou o resultado mais crítico, alcançando apenas 40%, uma vez que somente 8 das 20 funcionalidades previstas no backlog foram efetivamente implementadas. Apesar de contemplar os fluxos essenciais do sistema, diversos recursos planejados permanecem ausentes, como sistema de permissões, notificações, relatórios personalizados e controle de múltiplos armazéns.

A **Correção Funcional** obteve 87,5%, indicando que a maioria das funcionalidades implementadas executa corretamente suas operações. Entretanto, os testes identificaram uma vulnerabilidade crítica de autenticação, permitindo acesso indevido a determinadas rotas da API sem validação adequada de sessão. Essa falha compromete parcialmente a confiabilidade funcional da aplicação.

Por outro lado, a **Pertinência Funcional** alcançou 100%, demonstrando que todas as funcionalidades previstas estão alinhadas aos objetivos do domínio de gestão de inventário e agregam valor ao propósito do sistema.

### 2. Confiabilidade

A avaliação da Confiabilidade apresentou resultados distintos entre as subcaracterísticas de **Maturidade** e **Tolerância a Falhas**.

Os testes de **Maturidade** demonstraram elevado grau de estabilidade operacional. A Taxa de Falhas Funcionais (TFF) atingiu 0%, enquanto a Taxa de Operações Bem-Sucedidas (TOBS) alcançou 100%. Os fluxos principais do sistema, incluindo autenticação, cadastro, edição, remoção, consulta de inventário e exportação de relatórios, foram executados com sucesso e sem interrupções significativas.

Entretanto, os resultados de **Tolerância a Falhas** indicaram limitações importantes. Embora a Taxa de Proteção Contra Acesso Indevido (TPAI) tenha alcançado 100%, evidenciando mecanismos eficazes de autenticação e autorização, a Taxa de Tratamento de Entradas Inválidas (TTEI) obteve apenas 60%.

Os testes mostraram que o sistema trata adequadamente campos obrigatórios vazios, formatos incorretos e dados duplicados, porém ainda aceita determinados valores incompatíveis com as regras de negócio e não realiza validações adequadas para alguns caracteres especiais. Isso demonstra que o sistema possui boa estabilidade operacional, mas ainda carece de mecanismos mais robustos para lidar com erros de entrada e situações inesperadas.

---

## Melhoria Proposta

Com base nos resultados obtidos, as melhorias devem concentrar-se em três frentes principais: ampliação funcional, fortalecimento da validação de dados e aprimoramento da segurança.

### 1. Ampliação da Cobertura Funcional

Implementar as funcionalidades previstas no backlog que ainda não foram entregues, priorizando:

- Sistema de permissões e níveis de acesso;
- Sistema de notificações;
- Relatórios personalizáveis;
- Controle de múltiplos armazéns;
- Integrações com serviços externos.

**Impacto esperado:** aumento da Completude Funcional e maior aderência aos requisitos originalmente definidos para o projeto.

### 2. Fortalecimento da Validação de Dados

Implementar validações mais rigorosas para entradas fornecidas pelos usuários, incluindo:

- Restrições para valores incompatíveis com as regras de negócio;
- Validação de caracteres especiais;
- Sanitização de entradas;
- Mensagens de erro mais detalhadas e orientativas.

**Impacto esperado:** aumento da Taxa de Tratamento de Entradas Inválidas (TTEI) e melhoria da Tolerância a Falhas do sistema.

### 3. Aprimoramento dos Mecanismos de Segurança

Revisar integralmente os controles de autenticação e autorização da aplicação, garantindo que todas as rotas protegidas exijam autenticação válida e permissões adequadas.

Também é recomendada a implementação de testes automatizados de segurança e validações periódicas das APIs.

**Impacto esperado:** eliminação de vulnerabilidades críticas, aumento da Correção Funcional e manutenção dos elevados níveis de Proteção Contra Acesso Indevido.

### 4. Automatização dos Testes de Qualidade

Incorporar testes automatizados funcionais, de validação e de segurança ao fluxo de desenvolvimento.

**Impacto esperado:** detecção precoce de falhas, redução de regressões e manutenção contínua da confiabilidade e qualidade funcional do sistema.

---

## Conclusão

A avaliação realizada demonstra que o AGIO apresenta uma base sólida para operações de gerenciamento de inventário, combinando elevada estabilidade operacional com funcionalidades relevantes para o domínio de aplicação.

Sob a perspectiva da **Confiabilidade**, os resultados foram positivos, especialmente em relação à Maturidade do sistema, que apresentou baixíssima incidência de falhas e elevado índice de sucesso operacional. Contudo, as limitações observadas no tratamento de entradas inválidas indicam que ainda existem oportunidades de evolução na Tolerância a Falhas.

Sob a perspectiva da **Adequação Funcional**, verificou-se que as funcionalidades implementadas são pertinentes e, em sua maioria, corretas. Entretanto, a baixa cobertura dos requisitos originalmente definidos e a existência de vulnerabilidades de autenticação impedem que o sistema seja considerado plenamente aderente às expectativas estabelecidas para o projeto.

De forma geral, o AGIO demonstra potencial para atender adequadamente às necessidades de gestão de inventário, mas ainda requer investimentos em expansão funcional, validação de dados e fortalecimento dos mecanismos de segurança. A execução deste processo de avaliação permitiu identificar, de forma objetiva e mensurável, os principais pontos fortes e as limitações atuais do sistema, fornecendo direcionamentos claros para sua evolução nas próximas versões.

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |  [João Igor](https://github.com/JoaoPC10)| 12/06/2026  |
