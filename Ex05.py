def inverter_string(s):
    string_invertida = ""  # Inicia uma string vazia
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]  # Adiciona cada caractere à string invertida
    return string_invertida  # Retorna a string invertida

def main():
    # Solicita ao usuário uma string
    entrada = input("Informe uma string para inverter: ")
    resultado = inverter_string(entrada)  # Chama a função para inverter
    print(f"String invertida: {resultado}")  # Exibe o resultado

if __name__ == "__main__":
    main()  # Executa a função principal
