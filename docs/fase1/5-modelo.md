# Fase 1 - Modelo de Qualidade e Escopo

## 1. Introdução

O objetivo desta etapa é apresentar o modelo de qualidade ISO/IEC 25010, destacando as duas características escolhidas pelo grupo: Confiabilidade e Funcionalidade. A partir delas, buscamos definir o que será analisado e até que ponto essa análise irá aprofundar cada característica.

## 2. Diagrama

O diagrama abaixo mostra o modelo ISO/IEC 25010 com as características escolhidas para a Fase 1.

![diagrama](../imagens/fase1/diagrama.png)
> Para a **Fase 1**, o diagrama apresenta as caracteristicas priorizadas com base no modelo central (ISO/IEC 25010)

## 3. Escopo

Nesta avaliação, vamos analisar apenas as características de Confiabilidade e Funcionalidade, seguindo as definições da ISO/IEC 25010. As outras características do modelo não serão incluídas no escopo, mas isso não diminui sua importância.

## 4. Adaptação ao Modelo

O modelo ISO/IEC 25010 foi adaptado para priorizar os aspectos mais críticos ao propósito desta avaliação: garantir a **confiabilidade** do sistema AGIO e a **completude/adequação de suas funcionalidades essenciais**.

A seleção das características foi guiada pelo cenário de uso do AGIO, um sistema web de inventário utilizado para gerenciar itens, usuários e registros em banco de dados, considerando a necessidade de assegurar que o sistema opere de forma previsível, estável e correta durante o uso.

### 4.1 Confiabilidade

Refere-se à capacidade do sistema AGIO de executar suas operações fundamentais (login, CRUD de itens, exportação CSV, controle de acesso, persistência de dados) sem apresentar falhas, interrupções inesperadas ou inconsistências nos dados.

|Subcaracterística de Confiabilidade (SQuaRE)|justificativa|
|--------|--------|
|**Maturidade**|Avalia a ocorrência de erros nas operações, como nas de login, edição e remoção de itens, consultas ao banco. Compromentendo o fluxo do usuário e a estabilidade do inventário |
|**Tolerância**| Avalia como o AGIO lida com entradas inválidas, tentativas de acesso não autorizado ou inconsitencia de dados.|

### 4.2 Funcionalidade

Refere-se ao grau em que o AGIO entrega corretamente as funcionalidades previstas, incluindo autenticação, gerenciamento de inventário, controle de acesso e exportação de dados.

|Subcaracterística de Confiabilidade (SQuaRE)|justificativa|
|--------|--------|
|Adequação Funcional| Avalia se o sistema está entregando tudo que promente: Login, CRUD, visualização e exportação|

## 5. Referências Bibliográficas

ISO. ISO/IEC 25010 — ISO 25000 Software and Data Quality. Disponível em: [ISO/IEC 25010](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010). Acesso em: 11 mai. 2026.

## **Histórico de Versão**

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 11/05/2026 | [Arthur Guilherme](https://github.com/ArthurGuilher62) |  |
| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Arthur Guilherme](https://github.com/ArthurGuilher62) | 11/05/2026 |  |  |