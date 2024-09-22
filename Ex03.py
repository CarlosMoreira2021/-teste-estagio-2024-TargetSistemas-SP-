import json

def carregar_dados(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def calcular_faturamento(dados):
    valores = [item['valor'] for item in dados['faturamento'] if item['valor'] > 0]
    
    if not valores:
        return None, None, 0  # Caso não haja faturamento
    
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)

    dias_acima_da_media = sum(1 for valor in valores if valor > media)

    return menor, maior, dias_acima_da_media

def main():
    dados = carregar_dados('faturamento.json')
    
    menor, maior, dias_acima_media = calcular_faturamento(dados)

    print(f"Menor valor de faturamento: R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias acima da média: {dias_acima_media}")

if __name__ == "__main__":
    main()
