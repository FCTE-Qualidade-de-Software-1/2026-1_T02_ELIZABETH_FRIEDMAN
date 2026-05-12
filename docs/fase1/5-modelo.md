# Fase 1 - Modelo de Qualidade e Escopo

## 1. Introdução

O objetivo desta etapa é apresentar o modelo de qualidade ISO/IEC 25010, destacando as duas características escolhidas pelo grupo: Confiabilidade e Funcionalidade. A partir delas, buscamos definir o que será analisado e até que ponto essa análise irá aprofundar cada característica.

## 2. Diagrama

O diagrama abaixo apresenta o modelo ISO/IEC 25010 com as características selecionadas para a Fase 1, bem como as respectivas subcaracterísticas escolhidas.

![diagrama](../imagens/fase1/diagrama.png)
> Para a Fase 1, o diagrama apresenta as características priorizadas com base no modelo central (ISO/IEC 25010), assim como as respectivas subcaracterísticas selecionadas para a análise.

## 3. Escopo

Nesta avaliação, analisaremos apenas as características de **Confiabilidade e Funcionalidade**, de acordo com as definições da ISO/IEC 25010. As demais características do modelo não farão parte do escopo, embora continuem sendo relevantes. 

Além disso, não foram selecionadas todas as subcaracterísticas associadas a cada característica; optamos por aquelas que consideramos mais aplicáveis ao projeto e mais adequadas para análise.

## 4. Adaptação ao Modelo

O modelo ISO/IEC 25010 foi adaptado para priorizar os aspectos mais críticos ao propósito desta avaliação: garantir a **confiabilidade** do sistema AGIO e a **completude/adequação de suas funcionalidades essenciais**.

A seleção das características foi guiada pelo cenário de uso do AGIO, um sistema web de inventário utilizado para gerenciar itens, usuários e registros em banco de dados, considerando a necessidade de assegurar que o sistema opere de forma previsível, estável e correta durante o uso.

### 4.1 Confiabilidade

Refere-se à capacidade do sistema AGIO de executar suas operações fundamentais (login, CRUD de itens, exportação CSV, controle de acesso, persistência de dados) sem apresentar falhas, interrupções inesperadas ou inconsistências nos dados.

|Subcaracterística de Confiabilidade (SQuaRE)| Justificativa |
|--------|--------|
|**Maturidade**| Avalia a ocorrência de erros durante operações como login, edição, remoção de itens e consultas ao banco, pois falhas comprometem o fluxo do usuário e a estabilidade do inventário |
|**Tolerância a Falhas**| Avalia como o AGIO reage a entradas inválidas, tentativas de acesso não autorizado ou inconsistências de dados |

Na tabela acima, apresentamos apenas as subcaracterísticas **Maturidade e Tolerância a Falhas**, que foram selecionadas para a análise do projeto. As demais subcaracterísticas, **Recuperabilidade e Disponibilidade**, não foram incluídas porque não poderiam ser avaliadas adequadamente, já que a página web analisada apresenta o **erro 500: INTERNAL_SERVER_ERROR**, impossibilitando a verificação de continuidade de serviço ou de mecanismos de recuperação.

### 4.2 Funcionalidade

Refere-se ao grau em que o AGIO entrega corretamente as funcionalidades previstas, incluindo autenticação, gerenciamento de inventário, controle de acesso e exportação de dados.

|Subcaracterística de Confiabilidade (SQuaRE)| Justificativa |
|--------|--------|
|Adequação Funcional| Avalia se o sistema entrega tudo o que promete: login, operações CRUD, visualização de itens e exportação de dados |

Na tabela acima, apresentamos apenas a subcaracterística **Adequação Funcional**, que foi selecionada para a análise do projeto. As demais subcaracterísticas, **Acurácia Funcional e Conformidade Funcional**, não foram incluídas porque o foco da avaliação está em verificar se o AGIO dispõe das funcionalidades necessárias ao seu uso, e esse escopo já é atendido pela Adequação Funcional.

Dessa forma, optamos por reduzir o escopo da análise para garantir uma avaliação mais profunda e bem fundamentada. Selecionar um número muito grande de características e subcaracterísticas poderia comprometer a qualidade da análise, enquanto concentrar a avaliação em pontos específicos permite trabalhar com um maior nível de detalhamento e excelência técnica.

## 5. Referências Bibliográficas

ISO. ISO/IEC 25010 — ISO 25000 Software and Data Quality. Disponível em: [ISO/IEC 25010](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010). Acesso em: 11 mai. 2026.

## **Histórico de Versão**

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento e documentação da Introdução, Escopo e Referências Bibliográficas | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 11/05/2026 | [Arthur Guilherme](https://github.com/ArthurGuilher62) | 11/05/2026 |
| 02 | Documentação do Diagrama e da Adaptação do Modelo | [Arthur Guilherme](https://github.com/ArthurGuilher62) | 11/05/2026 | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 12/05/2026 |
| 03 | Atualização da documentação da Adaptação do Modelo | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 12/05/2026 | [Arthur Guilherme](https://github.com/ArthurGuilher62) | 12/05/2026 |
