# 📚 Sistema de Cálculo de Notas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Licen%C3%A7a](https://img.shields.io/badge/licen%C3%A7a-MIT-yellow)
![Feito%20por](https://img.shields.io/badge/autor-Eu-purple)

## 🎯 Objetivo

O **Sistema de Cálculo de Notas** foi desenvolvido para automatizar o cálculo das médias dos alunos, identificar se foram aprovados, estão em recuperação ou reprovados e gerar um relatório simples de desempenho escolar.

## 🧑‍💻 Autor

- **Marcelino** — Estudante de Técnico em Desenvolvimento de Sistemas.

## 🐍 Linguagem utilizada

- [Python](https://www.python.org/)

## 🧮 Fórmula utilizada

O sistema calcula a média aritmética simples das notas:

\[
media = \frac{n_1 + n_2 + n_3}{3}
\]

### Critérios de avaliação

| Média | Situação |
|---|---|
| 7,0 ou mais | ✅ Aprovado |
| 5,0 a 6,99 | ⚠️ Recuperação |
| Abaixo de 5,0 | ❌ Reprovado |

## 🚀 Como executar

1. Instale o Python 3 em seu computador.
2. Salve o código em um arquivo chamado `sistema_notas.py`.
3. Abra o terminal na pasta do arquivo.
4. Execute o comando:

```bash
python sistema_notas.py
```

5. O relatório de desempenho será exibido no terminal.

## 🗂️ Estrutura do projeto

```text
sistema-notas/
│
├── calculo_de_media_funções.py   # Código principal do sistema
├── README.md          # Documentação do projeto
```

## ⚙️ Funções principais

- `calcular_media(notas)`: calcula a média das notas.
- `verificar_aprovacao(media)`: define a situação do aluno.
- `gerar_relatorio_aluno(aluno)`: cria o relatório individual.
- `gerar_relatorio_geral(alunos)`: cria o relatório de todos os alunos.
- `exibir_relatorio(relatorio)`: mostra o relatório na tela.

## 🔮 Possíveis melhorias

- Permitir cadastro de alunos pelo teclado.
- Usar média ponderada com pesos para provas e trabalhos.
- Salvar o relatório em arquivo `.txt` ou `.csv`.
- Criar interface gráfica ou versão web.

## 📄 Licença

Este projeto foi criado para fins educacionais.