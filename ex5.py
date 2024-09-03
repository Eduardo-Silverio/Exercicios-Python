texto_original = input("Digite o texto que deseja inverter: ")

texto_invertido = ""
for caractere in texto_original:
    texto_invertido = caractere + texto_invertido

print("String original:", texto_original)
print("String invertida:", texto_invertido)