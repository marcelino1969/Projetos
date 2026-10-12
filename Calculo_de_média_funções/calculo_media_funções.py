# ============================================
# Sistema de Cálculo de Notas
# Autor: Marcelino
# Objetivo: calcular médias, verificar situação
# e gerar relatório de desempenho.
# ============================================

def calcular_media(notas):
#Calcula a média aritmética das notas.

# Parâmetro:
# notas (list): lista com as notas do aluno.

#Retorno:
#float: média das notas.
# Evita divisão por zero caso a lista esteja vazia

    if len(notas) == 0:
        return 0.0

    # Soma todas as notas e divide pela quantidade
    media = sum(notas) / len(notas)

    # round() deixa o resultado com duas casas decimais
    return round(media, 2)


def verificar_aprovacao(media):
    
    #Verifica a situação do aluno com base na média.

    # Parâmetro:
    #media (float): média calculada do aluno.

    #Retorno:
        #str: "Aprovado", "Recuperação" ou "Reprovado".
    
    # Regra de aprovação: média maior ou igual a 7
    if media >= 7:
        return "Aprovado "

    # Regra de recuperação: média entre 5 e 6.99
    elif media >= 5:
        return "Recuperação "

    # Qualquer média abaixo de 5 é reprovação
    else:
        return "Reprovado "


def gerar_relatorio_aluno(aluno):
    
    # Gera o relatório individual de um aluno.

    # Parâmetro:
    # aluno (dict): dicionário com nome e notas por disciplina.

    #Retorno:
    # str: relatório formatado do aluno.

    nome = aluno["nome"]
    linhas = []
    linhas.append(f"Aluno: {nome}")
    linhas.append("-" * 35)

    # Percorre cada disciplina e suas notas
    for disciplina, notas in aluno["notas"].items():
        media = calcular_media(notas)
        situacao = verificar_aprovacao(media)

        linhas.append(f"Disciplina: {disciplina}")
        linhas.append(f"Notas: {notas}")
        linhas.append(f"Média: {media}")
        linhas.append(f"Situação: {situacao}")
        linhas.append("")

    return "\n".join(linhas)


def gerar_relatorio_geral(alunos):
    
   # Gera o relatório de desempenho de todos os alunos.

    #Parâmetro:
    # alunos (list): lista de dicionários com dados dos alunos.

    # Retorno:
    # str: relatório geral formatado.
    
    relatorio = ["RELATÓRIO DE DESEMPENHO ESCOLAR", "=" * 35, ""]

    # Para cada aluno, adiciona o relatório individual
    for aluno in alunos:
        relatorio.append(gerar_relatorio_aluno(aluno))

    return "\n".join(relatorio)


def exibir_relatorio(relatorio):
    
    # Procedimento para exibir o relatório na tela.

    # Parâmetro:
    # relatorio (str): texto do relatório.

    print(relatorio)


# ============================================
# Programa principal
# ============================================
if __name__ == "__main__":
    # Dados de exemplo para testar o sistema
    alunos = [
        {
            "nome": "Ana",
            "notas": {
                "Matemática": [8.0, 7.5, 9.0],
                "Português": [6.0, 5.5, 7.0],
                "Programação": [9.5, 8.0, 10.0]
            }
        },
        {
            "nome": "Bruno",
            "notas": {
                "Matemática": [4.0, 5.0, 3.5],
                "Português": [6.5, 7.0, 6.0],
                "Programação": [5.0, 4.5, 5.5]
            }
        }
    ]

    # Gera e mostra o relatório final
    relatorio_final = gerar_relatorio_geral(alunos)
    exibir_relatorio(relatorio_final)