# Fase 1 - Justificativas

## Introdução

O presente documento visa expor as razões e os propósitos que orientam a avaliação de qualidade do sistema Ágio. A análise aqui proposta adota como referência conceitual as características de qualidade de produto estabelecidas pela norma ISO/IEC 25010, priorizando os aspectos de maior relevância para a confiabilidade operacional e a completude funcional do sistema dentro do seu cenário de utilização.


## Justificativa da avaliação

A realização desta avaliação de qualidade se fundamenta na relevância prática que o Ágio possui no contexto de gestão de inventários, bem como nos riscos operacionais detectados ao longo da análise preliminar do sistema. O Ágio executa operações de natureza sensível — como autenticação de usuários, manipulação de registros em banco de dados e exportação de dados em formato CSV —, e eventuais falhas nessas operações podem provocar inconsistências no inventário e afetar de forma direta as decisões de seus usuários em ambientes corporativos de pequeno e médio porte.

### Riscos identificados

Durante a análise preliminar do sistema, foram identificados os seguintes riscos operacionais que motivam esta avaliação:

- **Tratamento insuficiente de entradas inválidas**: a ausência de validação adequada pode expor o sistema a comportamentos inesperados diante de dados malformados ou tentativas de acesso indevido;
- **Risco de inconsistência nos dados exportados**: falhas nas funcionalidades de exportação CSV podem gerar relatórios incorretos, comprometendo decisões gerenciais baseadas nesses dados.

### Motivações

Considerando esse panorama, a avaliação se volta para duas características de qualidade essenciais previstas na norma ISO/IEC 25010, selecionadas com o intuito de abordar os pontos de risco mais significativos do sistema.

A *Confiabilidade* se estabelece como o eixo prioritário desta avaliação, com o propósito de converter os sinais de instabilidade observados em dados objetivos e quantificáveis. A análise se debruça sobre a Maturidade do sistema, examinando a incidência de falhas em operações essenciais já que erros nessas rotinas prejudicam a experiência do usuário e desestabilizam o inventário. De forma complementar, investiga-se a Tolerância a Falhas, observando como o Ágio se comporta frente a entradas inválidas, tentativas de acesso indevido e inconsistências nos dados fornecidos, de modo a garantir que o sistema ofereça respostas controladas e seguras, sem interromper o serviço de maneira abrupta. As subcaracterísticas Recuperabilidade e Disponibilidade foram deixadas fora do escopo, uma vez que não é possível avaliá-las de forma adequada dada a atual indisponibilidade do sistema em ambiente de produção.

A *Adequação Funcional* se justifica pela necessidade de verificar se o AGIO atende de forma adequada aos objetivos de um sistema de gestão de inventários. A análise contempla a Completude Funcional, avaliando se o sistema disponibiliza todas as funcionalidades necessárias para atender aos requisitos definidos; a Correção Funcional, verificando se essas funcionalidades produzem resultados corretos e consistentes; e a Pertinência Funcional, examinando se os recursos implementados são relevantes e alinhados ao propósito do sistema. A combinação dessas subcaracterísticas permite avaliar de forma abrangente a qualidade funcional do AGIO, considerando tanto a cobertura e a precisão das funcionalidades quanto sua adequação aos objetivos do produto.

## Objetivo da avaliação

A partir da justificativa exposta, definem-se os seguintes objetivos específicos e práticos para esta avaliação:

- **Maturidade**: conduzir testes por meio da submissão do sistema a um conjunto de operações habituais com o propósito de documentar, categorizar e mensurar a frequência das falhas encontradas.

- **Tolerância a Falhas**: avaliar o comportamento do sistema quando confrontado com entradas inesperadas, dados malformados e tentativas de acesso indevido, de forma a verificar se as respostas do sistema são seguras e controladas, sem exposição de dados sensíveis nem interrupção abrupta do serviço.

- **Completude Funcional**: verificar se o AGIO disponibiliza todas as funcionalidades necessárias para atender aos objetivos e requisitos definidos para o sistema de gestão de inventários, incluindo autenticação de usuários, operações de criação, leitura, atualização e exclusão de itens (CRUD), controle de acesso por perfis e exportação de dados.
  
- **Correção Funcional**: avaliar se as funcionalidades implementadas produzem resultados corretos, consistentes e com o nível de precisão esperado, assegurando que operações como atualização de itens, controle de quantidades, autenticação e exportação de dados reflitam fielmente o estado real do sistema.
  
- **Pertinência Funcional**: analisar se as funcionalidades disponibilizadas pelo AGIO são relevantes e adequadas aos objetivos principais do sistema, verificando se contribuem efetivamente para a gestão de inventários sem incluir recursos desnecessários ou desalinhados ao escopo do produto.

A descrição detalhada das subcaracterísticas adotadas está disponível na seção de [Modelo de Qualidade e Escopo](5-modelo.md).

## Referência bibliográfica

> ISO. ISO/IEC 25010 — ISO 25000 Software and Data Quality. Disponível em: [ISO/IEC 25010](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010). Acesso em: 11 mai. 2026.

## **Histórico de Versão**

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 11/05/2026 |  [Yzabella Pimenta](https://github.com/redjsun) | 11/05/2026 |
| 02 | Desenvolvimento do documento, com a criação dos tópicos de introdução, justificativa, objetivo, referência bibliográfica, histórico de versão e inserção das referências. | [Yzabella Pimenta](https://github.com/redjsun) | 12/05/2026 | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 12/05/2026 |
| 03 | Revisão e ajuste do documento: correção ortográfica, padronização de numeração, inclusão de riscos identificados, adição de Acurácia Funcional ao escopo e preenchimento da referência bibliográfica. | [Yzabella Pimenta](https://github.com/redjsun) | 13/05/2026 |  [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 13/05/2026 |
