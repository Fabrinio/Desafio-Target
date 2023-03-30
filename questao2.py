def is_in_sequence(num):
    # inciando a sequencia
    a, b = 0, 1

    # fazendo o laço até o numero informado
    while b < num:
        a, b = b, a + b

    # verificando se faz parte da sequencia
    if b == num:
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

num = int(input("Informe um número: "))

is_in_sequence(num)