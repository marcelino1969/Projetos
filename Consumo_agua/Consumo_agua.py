#Autor Marcelino
def classificar_consumo():
    print("--- CAMPANHA DE CONSCIENTIZAÇÃO AMBIENTAL ---")
    print("Sistema de Análise de Consumo de Água\n")

    # Solicitação e padronização dos dados de entrada
    tipo_imovel = input("Digite o tipo de imóvel (casa, apartamento, comercial): ").strip().lower()
    
    try:
        consumo = float(input("Digite o consumo mensal de água em m³: "))
    except ValueError:
        print("Erro: O valor do consumo deve ser um número decimal válido.")
        return

    # Validação e classificação com base nas regras de negócio
    if tipo_imovel == "comercial":
        print("\nAlerta: Tarifa comercial aplicada – consulte o plano corporativo.")
        
    elif tipo_imovel == "apartamento" and consumo < 10:
        print("\nAlerta: Consumo econômico – excelente controle de água!")
        
    elif (tipo_imovel == "apartamento" and consumo >= 10) or (tipo_imovel == "casa" and consumo <= 25):
        print("\nAlerta: Consumo moderado – dentro do padrão residencial.")
        
    elif (tipo_imovel == "casa" and consumo > 25) or (tipo_imovel == "apartamento" and consumo >= 25):
        print("\nAlerta: Consumo excessivo – adote medidas de economia e verifique vazamentos.")
        
    else:
        print("\nErro: Tipo de imóvel inválido. Escolha entre 'casa', 'apartamento' ou 'comercial'.")

if __name__ == "__main__":
    classificar_consumo()
