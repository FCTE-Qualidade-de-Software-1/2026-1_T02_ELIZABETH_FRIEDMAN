# Fase 4 - Conclusão

## Discussão dos Resultados

A avaliação do sistema AGIO permitiu analisar duas dimensões principais da qualidade de software: **Adequação Funcional** e **Confiabilidade**, com base na aplicação do modelo GQM e nas métricas definidas na fase anterior.

Os resultados indicam que o sistema apresenta uma base funcional consistente para o gerenciamento de inventário, porém ainda possui limitações relevantes relacionadas à cobertura de requisitos e ao tratamento de situações excepcionais.

### 1. Adequação Funcional

A análise da Adequação Funcional revelou um cenário misto entre as subcaracterísticas avaliadas.

A **Completude Funcional** apresentou resultado crítico, com apenas 40% das funcionalidades especificadas implementadas, evidenciando lacunas importantes em relação ao backlog do sistema. Funcionalidades essenciais de apoio ao gerenciamento de inventário ainda não foram contempladas, reduzindo a aderência do sistema ao escopo inicialmente proposto.

A **Correção Funcional** alcançou 87,5%, indicando que a maior parte das funcionalidades implementadas executa corretamente suas operações. Entretanto, foram identificadas inconsistências em alguns fluxos, o que impede o enquadramento no nível de alta correção funcional.

Por outro lado, a **Pertinência Funcional** atingiu 100%, demonstrando que todas as funcionalidades previstas e implementadas estão alinhadas ao domínio de gestão de inventário e contribuem diretamente para os objetivos do sistema.

### 2. Confiabilidade

A avaliação da Confiabilidade apresentou resultados distintos entre as subcaracterísticas de **Maturidade** e **Tolerância a Falhas**.

Os testes de **Maturidade** indicaram um comportamento estável do sistema, com Taxa de Falhas Funcionais (2,46%) e Taxa de Operações Bem-Sucedidas (97,54%), ambas classificadas como maturidade média. Isso demonstra que o sistema executa suas operações principais de forma consistente, porém sem atingir o nível de alta maturidade.

Em relação à **Tolerância a Falhas**, observou-se desempenho desigual. A Taxa de Proteção Contra Acesso Indevido atingiu 100%, demonstrando eficácia dos mecanismos de autenticação e autorização. Por outro lado, a Taxa de Tratamento de Entradas Inválidas foi de apenas 60%, indicando dificuldades do sistema em lidar adequadamente com entradas inválidas e situações não previstas.

Os testes mostraram que o sistema trata adequadamente campos obrigatórios vazios, formatos incorretos e dados duplicados, porém ainda aceita determinados valores incompatíveis com as regras de negócio e não realiza validações adequadas para alguns caracteres especiais. Isso demonstra que o sistema possui boa estabilidade operacional, mas ainda carece de mecanismos mais robustos para lidar com erros de entrada e situações inesperadas.

---

## Melhoria Proposta

Com base nos resultados obtidos, as melhorias são organizadas em três frentes principais: expansão funcional, aprimoramento da validação de dados e fortalecimento da robustez do sistema.

### 1. Ampliação da Cobertura Funcional

Implementar funcionalidades ainda não contempladas no sistema, conforme definido no backlog, incluindo:

- Sistema de permissões e níveis de acesso
- Notificações de eventos
- Relatórios gerenciais
- Controle de múltiplos estoques
- Integração com serviços externos

**Impacto esperado:** aumento da Completude Funcional e maior aderência aos requisitos originalmente definidos para o projeto.

### 2. Fortalecimento da Validação de Dados

Aprimorar os mecanismos de validação de entradas do sistema, incluindo:

- Restrições para valores incompatíveis com as regras de negócio
- Validação de caracteres especiais
- Sanitização de dados de entrada
- Mensagens de erro mais claras para o usuário

**Impacto esperado:** aumento da Taxa de Tratamento de Entradas Inválidas (TTEI) e melhoria da Tolerância a Falhas do sistema.

### 3. Aprimoramento dos Mecanismos de Segurança

Revisar integralmente os controles de autenticação e autorização da aplicação, garantindo que todas as rotas protegidas exijam autenticação válida e permissões adequadas.

Também é recomendada a implementação de testes automatizados de segurança e validações periódicas das APIs.

**Impacto esperado:** eliminação de vulnerabilidades críticas, aumento da Correção Funcional e manutenção dos elevados níveis de Proteção Contra Acesso Indevido.

### 4. Automatização dos Testes de Qualidade

Incorporar testes automatizados no ciclo de desenvolvimento, incluindo testes funcionais e de validação.

**Impacto esperado:** detecção precoce de falhas, redução de regressões e manutenção contínua da confiabilidade e qualidade funcional do sistema.

---

## Conclusão

A avaliação realizada demonstra que o AGIO possui uma base funcional relevante para o gerenciamento de inventário, apresentando funcionalidades alinhadas ao domínio da aplicação e desempenho satisfatório na execução de suas operações principais.

Sob a perspectiva da Confiabilidade, os resultados indicaram um nível intermediário de maturidade, com baixa incidência de falhas funcionais e elevada taxa de operações bem-sucedidas. Além disso, o sistema demonstrou eficácia na proteção contra acessos indevidos. Entretanto, as limitações observadas no tratamento de entradas inválidas evidenciam oportunidades de melhoria na subcaracterística de Tolerância a Falhas, especialmente no que se refere à validação de dados fornecidos pelos usuários.

Sob a perspectiva da Adequação Funcional, verificou-se que as funcionalidades implementadas apresentam alta pertinência ao contexto de gerenciamento de inventário e nível intermediário de correção funcional. Contudo, a baixa taxa de completude funcional demonstra que uma parcela significativa das funcionalidades previstas ainda não foi implementada, reduzindo a aderência do sistema ao escopo originalmente definido.

De forma geral, o AGIO demonstra potencial para atender às necessidades de gestão de inventário, apresentando estabilidade operacional e funcionalidades adequadas ao seu propósito. No entanto, a ampliação da cobertura funcional e o aprimoramento dos mecanismos de validação de entradas constituem pontos fundamentais para a evolução da qualidade do sistema. A aplicação da abordagem GQM permitiu identificar de maneira objetiva os principais pontos fortes e as limitações da aplicação, fornecendo subsídios para o planejamento de melhorias e para o desenvolvimento de versões futuras mais completas e robustas.

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |  [João Igor](https://github.com/JoaoPC10)| 12/06/2026  |
