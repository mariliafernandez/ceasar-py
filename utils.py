def decode(frase, k):
    decoded = ''
    for letter in frase:
        letter = chr(ord(letter)-k)   
        decoded = decoded + letter
    return decoded

def encode(frase, k):
    encoded = ''
    for letter in frase:
        letter = chr(ord(letter)+k)   
        encoded = encoded + letter
    return encoded