#autor:Marcelino
#Pesquisa de satisfação do atendimento da empresa TudoWeb.
#Coleta dados de 50 entrevistados e contabiliza as opiniões:
#1 - EXCELENTE
#2 - BOM
#3 - RUIM


TOTAL_ENTREVISTADOS = 50

quantidade_excelente = 0
quantidade_ruim = 0

print("=" * 50)
print("     PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("=" * 50)

for entrevistado in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\nEntrevistado {entrevistado} de {TOTAL_ENTREVISTADOS}")

    nome = input("Digite o nome: ").strip()

    while nome == "":
        print("O nome não pode ficar vazio.")
        nome = input("Digite o nome: ").strip()

    while True:
        try:
            idade = int(input("Digite a idade: "))

            if idade > 0:
                break

            print("A idade deve ser maior que zero.")

        except ValueError:
            print("Digite uma idade válida usando apenas números.")

    print("\nOpções de atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    while True:
        try:
            opiniao = int(input("Digite o número correspondente à opinião: "))

            if opiniao in (1, 2, 3):
                break

            print("Opção inválida. Digite 1, 2 ou 3.")

        except ValueError:
            print("Digite apenas o número da opção.")

    if opiniao == 1:
        quantidade_excelente += 1
        descricao = "EXCELENTE"
    elif opiniao == 2:
        descricao = "BOM"
    else:
        quantidade_ruim += 1
        descricao = "RUIM"

    print(f"Resposta registrada para {nome}: {descricao}")

print("\n" + "=" * 50)
print("RESULTADO FINAL DA PESQUISA")
print("=" * 50)
print(f"Quantidade de respostas EXCELENTE: {quantidade_excelente}")
print(f"Quantidade de respostas RUIM: {quantidade_ruim}")
print("=" * 50)