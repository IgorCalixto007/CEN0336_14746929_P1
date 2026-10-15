#!/usr/bin/env python3
import sys

# Verifica se foi daDda a quantidade correta de argumentos (script + seq + 6 coordenadas)
if len(sys.argv) != 8:
    print("Erro: Forneça a sequência de DNA e 6 números inteiros (n1 a n6).")
    print("Uso: python3 script_CDS.py <seq> <n1> <n2> <n3> <n4> <n5> <n6>")
    sys.exit(1)

# Captura o primeiro argumento (sequência de DNA)
seq_dna = sys.argv[1]

# 2. Verifica se os 6 argumentos numéricos são números inteiros válidos
args_inteiros = sys.argv[2:8]
for arg in args_inteiros:
    if not arg.isdigit():
        print(f"Erro: O argumento '{arg}' não é um número inteiro válido.")
        sys.exit(1)

# Converte as 6 string para o tipo inteiro e atribui às variáveis n1 a n6
n1, n2, n3, n4, n5, n6 = [int(x) for x in args_inteiros]

# Confere se algum dos argumentos numéricos são maiores que o tamanho da sequência de DNA
tamanho_seq = len(seq_dna)
for n in [n1, n2, n3, n4, n5, n6]:
    if n > tamanho_seq:
        print(f"Erro: A coordenada {n} é maior que o tamanho da sequência ({tamanho_seq}).")
        sys.exit(1)

# 3. Extrai a sequência da CDS 1.
cds1 = seq_dna[n1-1 : n2]
# Confere se a CDS 1 inicia com o códon de início 'ATG'
inicia_com_ATG = cds1.startswith('ATG')

# 4. Extrai a sequência da CDS 2
cds2 = seq_dna[n3-1 : n4]

# 5. Extrai a sequência da CDS 3
cds3 = seq_dna[n5-1 : n6]

# Confere se a CDS 3 termina com um dos códons de parada (TAG, TAA ou TGA)
codons_parada = ['TAG', 'TAA', 'TGA']
termina_com_stop = (cds3[-3:] in codons_parada)

# 6. Caso a CDS 1 inicie com ATG e a CDS 3 termine com códon de parada, junte e imprime
if inicia_com_ATG and termina_com_stop:
    # Junta as três regiões codificantes numa única string
    sequencia_concatenada = cds1 + cds2 + cds3
    # Imprime a sequência resultante na tela
    print(sequencia_concatenada)
else:
    print("A CDS 1 não inicia com ATG ou a CDS 3 não termina com um stop codon (TAG, TAA ou TGA).")

