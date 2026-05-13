# Fase 1 - Justificativas

## 1 Introdução

O presente documento visa expor as razões e os propósitos que orientam a avaliação de qualidade do sistema Ágio — uma aplicação web de código aberto criada por alunos da Universidade de Brasília (UnB) no âmbito da disciplina de Métodos de Desenvolvimento de Software. A análise aqui proposta adota como referência conceitual as características de qualidade de produto estabelecidas pela norma ISO/IEC 25010, priorizando os aspectos de maior relevância para a confiabilidade operacional e a completude funcional do sistema dentro do seu cenário de utilização.


## 2 Justificativa da avaliação

A realização desta avaliação de qualidade se fundamenta na relevância prática que o Ágio possui no contexto de gestão de inventários, bem como nos riscos operacionais detectados ao longo da análise preliminar do sistema. O Ágio executa operações de natureza sensível — como autenticação de usuários, manipulação de registros em banco de dados e exportação de dados em formato CSV —, e eventuais falhas nessas operações podem provocar inconsistências no inventário e afetar de forma direta as decisões de seus usuários em ambientes corporativos de pequeno e médio porte.

### 2.1 Riscos identificados

Durante a análise preliminar do sistema, foram identificados os seguintes riscos operacionais que motivam esta avaliação:

- **Instabilidade do ambiente de produção**: a instância atual do AGIO apresenta **erro 500 (INTERNAL_SERVER_ERROR)** persistente, impedindo o acesso regular ao sistema e sugerindo fragilidades na infraestrutura ou no código de back-end;
- **Falhas em operações críticas**: erros durante login, edição e exclusão de itens podem provocar perda ou corrupção de dados no inventário;
- **Tratamento insuficiente de entradas inválidas**: a ausência de validação adequada pode expor o sistema a comportamentos inesperados diante de dados malformados ou tentativas de acesso indevido;
- **Risco de inconsistência nos dados exportados**: falhas nas funcionalidades de exportação CSV podem gerar relatórios incorretos, comprometendo decisões gerenciais baseadas nesses dados.

### 2.2 Motivações

Considerando esse panorama, a avaliação se volta para duas características de qualidade essenciais previstas na norma ISO/IEC 25010, selecionadas com o intuito de abordar os pontos de risco mais significativos do sistema.

A **Confiabilidade** se estabelece como o eixo prioritário desta avaliação, com o propósito de converter os sinais de instabilidade observados em dados objetivos e quantificáveis. A análise se debruça sobre a **Maturidade** do sistema, examinando a incidência de falhas em operações essenciais — como login, edição, exclusão de itens e consultas ao banco de dados — já que erros nessas rotinas prejudicam a experiência do usuário e desestabilizam o inventário. De forma complementar, investiga-se a **Tolerância a Falhas**, observando como o Ágio se comporta frente a entradas inválidas, tentativas de acesso indevido e inconsistências nos dados fornecidos, de modo a garantir que o sistema ofereça respostas controladas e seguras, sem interromper o serviço de maneira abrupta. As subcaracterísticas Recuperabilidade e Disponibilidade foram deixadas fora do escopo, uma vez que não é possível avaliá-las de forma adequada dada a atual indisponibilidade do sistema em ambiente de produção.

A **Funcionalidade** se justifica pela necessidade de confirmar se o Ágio realmente disponibiliza o conjunto de operações a que se propõe e se essas operações produzem resultados corretos. A avaliação se concentra na **Adequação Funcional**, analisando se o sistema oferece e executa de maneira correta suas funcionalidades centrais: autenticação de usuários, operações de criação, leitura, atualização e exclusão de itens do inventário (CRUD), controle de acesso por perfis de usuário e exportação dos dados em formato CSV. Complementarmente, avalia-se a **Acurácia Funcional**, verificando se cada funcionalidade implementada produz resultados precisos e consistentes com o comportamento esperado — por exemplo, se os dados exibidos após uma edição refletem corretamente as alterações realizadas e se os arquivos CSV exportados reproduzem fielmente o conteúdo do banco de dados. A combinação dessas duas subcaracterísticas permite não apenas verificar a existência das funções, mas também validar a precisão dos seus resultados, garantindo uma análise funcional mais completa. A subcaracterística **Conformidade Funcional** não foi incluída nesta fase porque sua avaliação exige comparação detalhada com requisitos formais, normas e documentação específica, sendo mais adequada para uma fase posterior.

## 3 Objetivo da avaliação

A partir da justificativa exposta, definem-se os seguintes objetivos específicos e práticos para esta avaliação:

- **Maturidade**: conduzir testes por meio da submissão do sistema a um conjunto de operações habituais — login com credenciais válidas e inválidas, criação, edição e exclusão de itens, consultas ao banco de dados e exportação em CSV — com o propósito de documentar, categorizar e mensurar a frequência das falhas encontradas.

- **Tolerância a Falhas**: avaliar o comportamento do sistema quando confrontado com entradas inesperadas, dados malformados e tentativas de acesso indevido, de forma a verificar se as respostas do sistema são seguras e controladas, sem exposição de dados sensíveis nem interrupção abrupta do serviço.

- **Adequação Funcional**: atestar se todas as funcionalidades descritas no repositório do projeto — gerenciamento de superusuários, controle de sessão, CRUD de inventário, visualização personalizada de itens e exportação em formato CSV — encontram-se implementadas e operam de acordo com o comportamento previsto.

- **Acurácia Funcional**: verificar se os resultados produzidos por cada funcionalidade são precisos e consistentes, assegurando que operações como edição de itens, cálculos de quantidades e exportação de dados gerem saídas fiéis ao conteúdo real do sistema.

A descrição detalhada das subcaracterísticas adotadas está disponível na seção de [Modelo de Qualidade e Escopo](5-modelo.md).

## 4 Referência bibliográfica

> ISO. ISO/IEC 25010 — ISO 25000 Software and Data Quality. Disponível em: [ISO/IEC 25010](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010). Acesso em: 11 mai. 2026.

## **Histórico de Versão**

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 11/05/2026 |  |  |
| 02 | Desenvolvimento do documento, com a criação dos tópicos de introdução, justificativa, objetivo, referência bibliográfica, histórico de versão e inserção das referências. | [Yzabella Pimenta](https://github.com/redjsun) | 12/05/2026 | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 12/05/2026 |
| 03 | Revisão e ajuste do documento: correção ortográfica, padronização de numeração, inclusão de riscos identificados, adição de Acurácia Funcional ao escopo e preenchimento da referência bibliográfica. | [Yzabella Pimenta](https://github.com/redjsun) | 13/05/2026 |  |  |