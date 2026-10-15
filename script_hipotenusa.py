#!/usr/bin/env python3
import sys

# Verifica se foi dado dois argumentos adicionais na linha de comando
if len(sys.argv) != 3:
    print("Erro: Insira dois inteiros positivos na linha de comando.")
    sys.exit(1)

# Os argumentos
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# Verifica se ambos são números inteiros positivos
if not (arg1.isdigit() and arg2.isdigit()):
    print("Erro: Ambos os valores devem ser números inteiros positivos.")
    sys.exit(1)

# Converte as strings da linha de comando para o tipo numérico int
a = int(arg1)
b = int(arg2)

# Confere se os números fornecidos são inteiros estritamente positivos e menores que 500
if a >= 500 or b >= 500 or a <= 0 or b <= 0:
    print("Erro: a e b devem ser inteiros positivos maiores que 0 e menores que 500.")
    sys.exit(1)

# Calcula o valor do quadrado da hipotenusa
z = a**2 + b**2

# Imprime o resultado formatado na tela conforme o padrão exigido
print(f"O quadrado da hipotenusa para o triangulo retângulo com lados a={a} e b={b}, é {z}")
