#!/usr/bin/env python3
import sys

# Solicita a entrada das temperaturas em graus Celsius
entrada = input("Digite as temperaturas em graus Celsius (separadas por espaço): ")

# Transforma a string de entrada numa lista de strings
lista_celsius_str = entrada.split()

# Verifica se a lista não está vazia
if not lista_celsius_str:
    print("Erro: Nenhuma temperatura foi inserida.")
    sys.exit(1)

# Cria uma lista vazia para armazenar as temperaturas convertidas
lista_fahrenheit = []

# Utiliza um loop for para iterar sobre a lista de temperaturas fornecidas
for temp_str in lista_celsius_str:
    # Verifica os dados de entrada para garantir que contêm apenas tipos válidos (números)
    try:
        celsius = float(temp_str)
    except ValueError:
        print(f"Erro: O valor '{temp_str}' não é numérico.")
        sys.exit(1)
    
    # Realiza a conversão de Celsius para Fahrenheit
    fahrenheit = (9 / 5) * celsius + 32
    
    # Adiciona o valor convertido à lista vazia
    lista_fahrenheit.append(fahrenheit)

# Exibe as temperaturas em Fahrenheit numa tabela
for i in range(len(lista_celsius_str)):
    print(f"{lista_celsius_str[i]:<4} {lista_fahrenheit[i]:.1f}")

