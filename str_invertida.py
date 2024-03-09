def inverter_str(string):
    inverte_str = ""
    for i in range(len(string) - 1, -1, -1):
        inverte_str += string[i]
    return inverte_str


# Solicitando ao usuário que insira uma string
str_exemplo = input("Digite uma string para inverter: ")

# Invertendo a string fornecida pelo usuário
str_invertida = inverter_str(str_exemplo)

# Imprimindo a string invertida
print("String original:", str_exemplo)
print("String invertida:", str_invertida)
