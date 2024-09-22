def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

def main():
    # Número a ser verificado
    numero = int(input("Informe um número: "))
    
    # Calcula a sequência de Fibonacci até o número informado
    fib_sequence = fibonacci_sequence(numero)
    
    # Verifica se o número está na sequência
    if numero in fib_sequence:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
