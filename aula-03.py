# Desafio 
# Criar um programa para verificar a maioridade

# Passo 1: Criar uma variável
# Passo 2: criar uma estrutura de condição para verificar a idade
# Passo 3: Exibir a frase adequada de acordo com a idade da pessoa

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("você é um adolescente")
else:
    print("Você é uma criança!")
