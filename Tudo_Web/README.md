# 📊 Pesquisa de Atendimento TudoWeb

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

## 🎯 Objetivo

O sistema **Pesquisa de Atendimento TudoWeb** coleta opiniões de clientes
sobre a qualidade do atendimento prestado pela empresa.

Cada entrevistado informa:

- Nome;
- Idade;
- Opinião sobre o atendimento.

As opções disponíveis são:

1. EXCELENTE;
2. BOM;
3. RUIM.

Ao final da pesquisa, o programa exibe a quantidade de respostas
**EXCELENTE** e **RUIM**.

## 🛠️ Tecnologias utilizadas

- Python 3;
- Estrutura de repetição `for`;
- Estrutura de repetição `while`;
- Estruturas condicionais `if`, `elif` e `else`;
- Validação de dados com `try` e `except`.

## 📁 Estrutura do projeto

```text
tudoweb-pesquisa/
├── pesquisa_atendimento.py
└── README.md
```

## ▶️ Como executar

1. Instale o Python 3 em seu computador.
2. Baixe ou clone este projeto.
3. Abra o terminal na pasta do projeto.
4. Execute o comando:

```bash
python pesquisa_atendimento.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 pesquisa_atendimento.py
```

## 🧮 Fórmula utilizada

A quantidade de respostas `BOM` pode ser calculada pela fórmula:

```text
BOM = Total de entrevistados - (EXCELENTE + RUIM)
```

Neste projeto:

```text
BOM = 50 - (EXCELENTE + RUIM)
```

## 🧪 Teste

Para realizar um teste rápido com 10 entrevistados, altere temporariamente
a constante no arquivo Python:

```python
TOTAL_ENTREVISTADOS = 10
```

Após a validação, altere novamente para:

```python
TOTAL_ENTREVISTADOS = 50
```

## 📌 Resultado

Ao terminar as entrevistas, o programa informa:

- Quantidade de respostas `EXCELENTE`;
- Quantidade de respostas `RUIM`.

