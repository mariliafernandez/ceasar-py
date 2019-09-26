from utils import *

opt = input("Entre com a opção:\n[1] Criptografar\n[2] Descriptografar\n")

if opt == '1':
    frase = input("Digite a frase a ser criptografada: ")
    k = int(input("Entre com o fator k: "))
    print(encode(frase, k))

elif opt == '2':
    frase = input("Digite a frase a ser descriptografada: ")
    k = int(input("Entre com o fator k: "))
    print(decode(frase, k))

