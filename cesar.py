frase = input("Digite a frase a ser criptografada: ")
fator = input("Entre com o fator: ")
nova_frase = ''

for letter in frase:
    letter = chr(ord(letter)+1)   
    nova_frase = nova_frase + letter
print(nova_frase)
