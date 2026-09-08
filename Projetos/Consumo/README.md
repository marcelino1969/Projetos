# ⚡ Calculadora de Consumo de Energia Elétrica 💡

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-F7DF1E?style=for-the-badge&logo=star&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📖 Sobre o Projeto

Este projeto é uma **calculadora simples em Python** que estima o consumo mensal de energia elétrica de aparelhos domésticos e comerciais. Através de dados como potência e tempo de uso, o programa calcula quantos kWh um aparelho consome por mês e qual o custo estimado na conta de luz.

### 🎯 Objetivos

- 🔌 Calcular o consumo energético de qualquer aparelho elétrico
- 💰 Estimar o custo mensal baseado no consumo
- 📊 Ajudar no planejamento e economia de energia
- 🌱 Promover conscientização sobre uso eficiente de energia

---

## 🛠️ Tecnologias Utilizadas

<div align="center">

| Tecnologia | Descrição | Badge |
|------------|-----------|-------|
| **Python** | Linguagem de programação principal | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Terminal** | Interface de execução (CLI) | ![Terminal](https://img.shields.io/badge/Terminal-000000?style=flat-square&logo=gnu-bash&logoColor=white) |
| **GitHub** | Hospedagem do código | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) |

</div>

---

## 🧮 Fórmula Utilizada

O cálculo do consumo mensal é baseado na seguinte fórmula:

### 📝 Explicação da Fórmula

| Variável | Descrição | Unidade |
|----------|-----------|---------|
| **potência** | Potência do aparelho | Watts (W) |
| **horas de uso por dia** | Tempo médio diário de utilização | Horas (h) |
| **30** | Dias no mês (média) | Dias |
| **1000** | Conversão de Watts para Kilowatts | Fator |

### 💰 Cálculo do Custo
custoEstimado (R$) = consumoMensal (kWh) × custoPorKWh (R$ 0,75)