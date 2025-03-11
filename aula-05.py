# Desafio

def note_register():
    notes = []
    while True:
        try:
            entry = input("Digite a nota do aluno: (ou 'fim' para encerrar): ")
            if entry.lower() == 'fim':
                break
            note = float(entry)
            if 0 <= note <=10:
                notes.append(note)
            else:
                print("Nota inválida! Digite um valor de 0 a 10")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim' para encerrar.")

            if notes:
                mean = sum(notes)/len(notes)
                print(f"A média das notas é: {mean:2f}")
                print(f"Total de notas válidas inseridas: {len(notes)}")
            
            else:
                print("Nenhuma nota válida inserida")

note_register()

