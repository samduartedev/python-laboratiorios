# Desafio

#Criar uma calculadora para realizar operações básicas de Matemática

#Requisitos

# 1: As operações matemáticas devem ser realizadas entre dois números
# 2: As operações básicas são: adição, subtração, multiplicação e divisão 
# 3: O programa deve tratar entradas inválidas

def calculator():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operation = input("Digite a operação(+,-,*,/):")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 + num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1/num2
            else:
                raise ValueError
            
            print(f"Resultado:{result}")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente Novamente.")
        except ZeroDivisionError:
            print("Erro: Divisão por 0 não é permitida. Tente Novamente.")
        
calculator()
