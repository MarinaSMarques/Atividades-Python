def palavra_vogal(palavras):
    return [palavra for palavra in palavras
            if palavra[0].lower() in 'aeiou']

palavras = ["gato", "elefante", "urso", "abelha", "cobra"]
resultado = palavra_vogal(palavras)

print("Palavras que começam com uma vogal:", resultado)