# Fase 1 - Justificativas

## 1 Introdução

O presente documento visa expor as razões e os propósitos que orientam a avaliação de qualidade do sistema Ágio — uma aplicação web de código aberto criada por alunos da Universidade de Brasília (UnB) no âmbito da disciplina de Métodos de Desenvolvimento de Software. A análise aqui proposta adota como referência conceitual as características de qualidade de produto estabelecidas pela norma ISO/IEC 25010, priorizando os aspectos de maior relevância para a confiabilidade operacional e a completude funcional do sistema dentro do seu cenário de utilização.


## Justrificativa da avaliação

A realização desta avaliação de qualidade se fundamenta na relevância prática que o Ágio possui no contexto de gestão de inventários, bem como nos riscos operacionais detectados ao longo da análise preliminar do sistema. O Ágio executa operações de natureza sensível — como autenticação de usuários, manipulação de registros em banco de dados e exportação de dados em formato CSV —, e eventuais falhas nessas operações podem provocar inconsistências no inventário e afetar de forma direta as decisões de seus usuários em ambientes corporativos de pequeno e médio porte.

Considerando esse panorama, a avaliação se volta para duas características de qualidade essenciais previstas na norma ISO/IEC 25010, selecionadas com o intuito de abordar os pontos de risco mais significativos do sistema.

A Confiabilidade se estabelece como o eixo prioritário desta avaliação, com o propósito de converter os sinais de instabilidade observados em dados objetivos e quantificáveis. A análise se debruça sobre a Maturidade do sistema, examinando a incidência de falhas em operações essenciais — como login, edição, exclusão de itens e consultas ao banco de dados — já que erros nessas rotinas prejudicam a experiência do usuário e desestabilizam o inventário. De forma complementar, investiga-se a Tolerância a Falhas, observando como o Ágio se comporta frente a entradas inválidas, tentativas de acesso indevido e inconsistências nos dados fornecidos, de modo a garantir que o sistema ofereça respostas controladas e seguras, sem interromper o serviço de maneira abrupta. As subcaracterísticas Recuperabilidade e Disponibilidade foram deixadas fora do escopo, uma vez que não é possível avaliá-las de forma adequada dada a atual indisponibilidade do sistema em ambiente de produção.

A Funcionalidade se justifica pela necessidade de confirmar se o Ágio realmente disponibiliza o conjunto de operações a que se propõe. A avaliação se concentra na Adequação Funcional, analisando se o sistema oferece e executa de maneira correta suas funcionalidades centrais: autenticação de usuários, operações de criação, leitura, atualização e exclusão de itens do inventário (CRUD), controle de acesso por perfis de usuário e exportação dos dados em formato CSV. Essa subcaracterística foi priorizada porque o foco desta avaliação reside em atestar a existência e o funcionamento adequado das capacidades fundamentais do sistema, evitando dispersar o esforço de análise em aspectos de importância secundária. As subcaracterísticas Acurácia Funcional e Conformidade Funcional não foram contempladas pelo mesmo motivo — a Adequação Funcional já abrange suficientemente o objetivo central desta etapa.

## Objetivo da avaliação

A partir da justificativa exposta, definem-se os seguintes objetivos específicos e práticos para esta avaliação:

Conduzir testes de Maturidade por meio da submissão do sistema a um conjunto de operações habituais — login com credenciais válidas e inválidas, criação, edição e exclusão de itens, consultas ao banco de dados e exportação em CSV — com o propósito de documentar, categorizar e mensurar a frequência das falhas encontradas.

Avaliar a Tolerância a Falhas do Ágio, examinando o comportamento do sistema quando confrontado com entradas inesperadas, dados malformados e tentativas de acesso indevido, de forma a verificar se as respostas do sistema são seguras e controladas, sem exposição de dados sensíveis nem interrupção abrupta do serviço.

Atestar a Adequação Funcional do sistema, verificando se todas as funcionalidades descritas no repositório do projeto — gerenciamento de superusuários, controle de sessão, CRUD de inventário, visualização personalizada de itens e exportação em formato CSV — encontram-se implementadas e operam de acordo com o comportamento previsto.

A descrição detalhada das subcaracterísticas adotadas está disponível na seção de Modelo de Qualidade e Escopo.

## Referência bibliográfica



## **Histórico de Versão**

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 11/05/2026 |  |  |
| 02 | Desenvolvimento do documento, com a criação dos tópicos de introdução, justificativa, objetivo, referência bibliográfica, histórico de versão e inserção das referências. | [Yzabella Pimenta](https://github.com/redjsun) | 12/05/2026 | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 12/05/2026 |