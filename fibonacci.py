def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

def check_fibonacci(number, sequence):
    if number in sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} não pertence à sequência de Fibonacci."

# Função principal
def main():
    number = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))
    fib_sequence = fibonacci_sequence(number)
    message = check_fibonacci(number, fib_sequence)
    print(message)

if __name__ == "__main__":
    main()