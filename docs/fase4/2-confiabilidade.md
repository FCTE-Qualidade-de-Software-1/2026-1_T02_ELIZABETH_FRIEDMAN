# Fase 4 - Confiabilidade

## Procedimento Executado

Nesta etapa do projeto, foram medidas as métricas **1.1**, **1.2**, **2.1** e **2.2** definidas na [Fase 3](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase3/2-confiabilidade/), que tratam se sobre a **Maturidade** e **Tolerância a Falhas** do sistema AGIO.

As medições foram obtidas através de scripts de testes das funcionalidades mencionadas na Fase 3 e depois calculadas seguindo o método descrito na [Fase 2](https://fcte-qualidade-de-software-1.github.io/2026-1_T02_ELIZABETH_FRIEDMAN/fase2/2-confiabilidade/).

![Resultados dos testes](///.png)
<p align="center"><em>Figura 2: Resultados obtidos ao executar testes, que será utilizado para as métricas 1.1, 1.2 e 2.1</em></p>

---

### Métrica 1.1: Taxa de Falhas Funcionais

Esta métrica contabiliza o número de falhas encontradas em relação ao número total de operações realizadas.

**Fórmula:**
$$\text{Taxa de Falhas} = \left( \frac{\text{Nº de falhas}}{\text{Nº total de operações}} \right) \times 100$$


### Métrica 1.2: Taxa de Operações Bem-Sucedidas

Esta métrica contabiliza o número de operações concluídas com sucesso em relação ao número total de operações realizadas.

**Fórmula:**
$$\text{Taxa de Sucesso} = \left( \frac{\text{Nº de operações concluídas com sucesso}}{\text{Nº total de operações}} \right) \times 100$$

### Métrica 2.1: Taxa de Tratamento de Entradas Inválidas

Esta métrica contabiliza o número de operações bem-sucedidas no tratamento e rejeição controlada de dados de entrada incorretos.

**Fórmula:**
$$\text{Taxa de Tratamento} = \left( \frac{\text{Nº de entradas inválidas tratadas}}{\text{Nº total de entradas inválidas}} \right) \times 100$$

### Métrica 2.2: Taxa de Proteção Contra Acesso Indevido

Esta métrica contabiliza a eficácia do sistema no bloqueio de tentativas de acesso não autorizadas ou maliciosas.

**Fórmula:**
$$\text{Taxa de Proteção} = \left( \frac{\text{Nº de tentativas bloqueadas}}{\text{Nº total de tentativas indevidas}} \right) \times 100$$

## Medição (Dados Coletados)

## Análise e Julgamento

## Histórico de Versão

| ID | Descrição | Autor | Data | Revisor | Data |
|:--:|:---------|:------|:--------|:--------|:----:|
| 01 | Criação do documento | [Tiago Lemes](https://github.com/TiagoTeixeira-2005) | 02/06/2026 |   [João Igor](https://github.com/JoaoPC10)| 12/06/2026 |