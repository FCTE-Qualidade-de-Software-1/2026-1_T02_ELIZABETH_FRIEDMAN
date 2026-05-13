# Fase 1 - Modelo de Qualidade e Escopo

## 1. Introdução

O objetivo desta etapa é apresentar o modelo de qualidade **ISO/IEC 25010**, destacando as duas características escolhidas pelo grupo: Confiabilidade e Funcionalidade. A partir delas, buscamos definir o que será analisado e até que ponto essa análise irá aprofundar cada característica.

## 2. Diagrama

O diagrama abaixo apresenta o **modelo ISO/IEC 25010** com as características selecionadas para a Fase 1, bem como as respectivas subcaracterísticas escolhidas.

![diagrama](../imagens/fase1/diagrama.png)
> Para a Fase 1, o diagrama apresenta as características priorizadas com base no modelo central (ISO/IEC 25010), assim como as respectivas subcaracterísticas.

## 3. Escopo

Nesta avaliação, analisaremos apenas as características de **Confiabilidade e Funcionalidade**, conforme definidas pela ISO/IEC 25010. As demais características do modelo, embora relevantes, não farão parte do escopo desta fase.

Além disso, nem todas as subcaracterísticas associadas a essas características foram selecionadas. Optou-se por incluir apenas aquelas mais adequadas ao contexto do projeto e mais relevantes para a análise pretendida.

Dessa forma, definiu-se por um escopo reduzido, visando **garantir uma avaliação mais aprofundada e metodologicamente consistente**. A inclusão de um número muito grande de características e subcaracterísticas poderia comprometer a profundidade da investigação, enquanto concentrar a análise em pontos específicos permite trabalhar com maior detalhamento e clareza.

## 4. Adaptação ao Modelo

O modelo ISO/IEC 25010 foi adaptado para priorizar os aspectos mais críticos ao propósito desta avaliação: garantir a **confiabilidade** do sistema AGIO e a **adequação e completude de suas funcionalidades essenciais**.

A seleção das características considerou o cenário de uso do AGIO, um sistema web de inventário utilizado para gerenciar itens, usuários e registros em banco de dados, levando em conta a necessidade de assegurar que o sistema opere de forma previsível, estável e correta durante o uso.

### 4.1 Confiabilidade

Refere-se à capacidade do sistema AGIO de executar suas operações fundamentais (login, CRUD de itens, exportação CSV, controle de acesso, persistência de dados) sem apresentar falhas, interrupções inesperadas ou inconsistências nos dados.

> A tabela a seguir apresenta a classificação das subcaracterísticas de Confiabilidade do modelo SQuaRE (ISO/IEC 25010), utilizando a matriz Impacto × Risco para apoiar a priorização.

|Subcaracterística de Confiabilidade (SQuaRE)| Impacto | Risco |Justificativa |
|--------|--------|--------|--------|
|**Maturidade**| Alto | Alto | Avalia a ocorrência de erros durante operações como login, edição, remoção de itens e consultas ao banco, pois falhas comprometem o fluxo do usuário e a estabilidade do inventário |
|**Tolerância a Falhas**| Alto | Alto | Avalia como o AGIO reage a entradas inválidas, tentativas de acesso não autorizado ou inconsistências de dados |
|**Disponibilidade**| Alto | Alto | Avalia a capacidade do sistema de permanecer operacional e acessível aos usuários |
|**Recuperabilidade**| Médio | Alto | Avalia a capacidade de o sistema retornar ao funcionamento normal após falhas |

Para o escopo do projeto, selecionamos apenas as subcaracterísticas **Maturidade e Tolerância a Falhas**, pois ambas representam os aspectos mais diretamente observáveis e críticos do comportamento do AGIO no estado atual. Essas subcaracterísticas permitem avaliar a frequência de falhas e a resposta do sistema a situações inesperadas, dois fatores essenciais para compreender a estabilidade operacional e a robustez mínima necessária para o uso cotidiano do inventário. Além disso, são elementos cuja análise não depende de monitoramento contínuo, podendo ser examinados mesmo diante das limitações técnicas apresentadas pelo ambiente.

As demais subcaracterísticas, **Recuperabilidade e Disponibilidade** não foram avaliadas nesta fase porque o ambiente analisado (instância atual do AGIO) apresenta **erro 500: INTERNAL_SERVER_ERROR** persistente, impedindo medições contínuas de uptime, comportamento após falhas e mecanismos de recuperação. Embora essas características possam ser medidas em um ambiente local, optamos por não adicioná-las ao escopo da Fase 1.

### 4.2 Funcionalidade

Refere-se ao grau em que o AGIO entrega corretamente as funcionalidades previstas, incluindo autenticação, gerenciamento de inventário, controle de acesso e exportação de dados.

> A tabela a seguir apresenta a classificação das subcaracterísticas de Funcionalidade do modelo SQuaRE (ISO/IEC 25010), utilizando a matriz Impacto × Risco para apoiar a priorização.

|Subcaracterística de Confiabilidade (SQuaRE)| Impacto | Risco |Justificativa |
|--------|--------|--------|--------|
| **Adequação Funcional** | Alto | Alto | Avalia se o sistema entrega tudo o que promete: login, operações CRUD, visualização de itens e exportação de dados |
| **Acurácia Funcional** | Alto | Médio | Avalia se cada funcionalidade é executada de forma correta e com resultados consistentes |
| **Conformidade Funcional** | Médio | Médio | Avalia o alinhamento das funcionalidades com normas, requisitos formais e regras de negócio |

Para o escopo do projeto, selecionamos as subcaracterísticas **Adequação Funcional e Acurácia Funcional**, pois ambas permitem avaliar não apenas se o AGIO disponibiliza as funcionalidades essenciais ao seu uso, mas também se essas funcionalidades produzem resultados corretos e consistentes. Dessa forma, o escopo combina a verificação da existência das funções com a validação da precisão dos resultados, garantindo uma análise funcional mais completa.

A subcaracterística **Conformidade Funcional** não foi incluída nesta fase porque sua avaliação exige comparação detalhada com requisitos formais, normas e documentação específica. Como o foco atual está em analisar o comportamento real do sistema e a qualidade funcional observável, a verificação de conformidade documental foi adiada para uma fase posterior, quando existir maior estabilidade e clareza dos requisitos.

## 5. Referências Bibliográficas

ISO. ISO/IEC 25010 — ISO 25000 Software and Data Quality. Disponível em: [ISO/IEC 25010](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010). Acesso em: 11 mai. 2026.

## **Histórico de Versão**

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento e documentação da Introdução, Escopo e Referências Bibliográficas | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 11/05/2026 | [Arthur Guilherme](https://github.com/ArthurGuilher62) | 11/05/2026 |
| 02 | Documentação do Diagrama e da Adaptação do Modelo | [Arthur Guilherme](https://github.com/ArthurGuilher62) | 11/05/2026 | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 12/05/2026 |
| 03 | Atualização da documentação da Adaptação do Modelo | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 12/05/2026 | [Arthur Guilherme](https://github.com/ArthurGuilher62) | 12/05/2026 |
