import re

while True:
    senha = input("Digite a senha com os seguintes critérios mínimos: 8 caracteres, 1 letra maiúscula, 1 letra minúscula,\n1 número, 1 caracter especial): ")
    if (len(senha) >= 8 and
            any(c.isupper() for c in senha) and
            any(c.islower() for c in senha) and
            any(c.isdigit() for c in senha) and
            any(c in "!@#$%^&*()_+{}:<>?~-" for c in senha)):
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("Senha inválida. Por favor, verifique os requisitos.")