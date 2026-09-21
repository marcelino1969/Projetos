# 💧 Monitor de Consumo Hídrico - Campanha de Conscientização Ambiental

Este projeto consiste em uma ferramenta em Python desenvolvida para a companhia de saneamento local. O objetivo é analisar o consumo mensal de água dos imóveis, classificar o perfil de uso e emitir alertas educativos automáticos aos moradores, incentivando o consumo consciente e a detecção precoce de vazamentos.

## 🚀 Funcionalidades

- **Identificação do Perfil:** Segmentação personalizada para residências (casas e apartamentos) e comércios.
- **Alertas Educativos:** Mensagens automáticas baseadas em faixas críticas de consumo em metros cúbicos (m³).
- **Validação de Dados:** Sistema preparado para mitigar erros de digitação do usuário.

## 📋 Regras de Negócio

O sistema avalia os dados inseridos cruzando o tipo de imóvel e o volume consumido:

| Tipo de Imóvel | Consumo (m³) | Alerta Emitido |
| :--- | :--- | :--- |
| **Comercial** | Qualquer valor | *Tarifa comercial aplicada – consulte o plano corporativo.* |
| **Apartamento** | Menor que 10 | *Consumo econômico – excelente controle de água!* |
| **Apartamento / Casa** | Até 25 | *Consumo moderado – dentro do padrão residencial.* |
| **Qualquer Outro** | Acima do limite hídrico | *Consumo excessivo – adote medidas de economia e verifique vazamentos.* |

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Estruturas de Controle:** Condicionais compostas (`if`, `elif`, `else`), Operadores Lógicos (`and`, `or`) e tratamento de exceções.

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe o arquivo `classificador_consumo.py`.
3. Abra o terminal ou prompt de comando na pasta do arquivo e execute:
   ```bash
   python classificador_consumo.py
   ```
4. Insira os dados solicitados na tela para receber o diagnóstico ambiental.

---
*Contribuindo para um futuro mais sustentável através da tecnologia e da conscientização.*
