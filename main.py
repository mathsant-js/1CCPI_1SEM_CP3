def adicionar_temperaturas(salas):
    for i in range(len(temperaturas)):
        salas[i] = temperaturas[i]

def media_temperatura(sala):
    soma_temperatura = 0
    for i in range(len(sala)):
        soma_temperatura += sala[i]
    return soma_temperatura / len(sala)

def calcular_registro_critico(sala):
    quantidade_registro_critico = 0
    for s in sala:
        if s >= 33:
            quantidade_registro_critico += 1
    return quantidade_registro_critico

def maior_risco(salas):
    sala_critico = 0
    maior_critico = calcular_registro_critico(salas[0])
    for i in range(len(salas)):
        if calcular_registro_critico(salas[i]) > maior_critico:
            maior_critico = calcular_registro_critico(salas[i])
            sala_critico = i + 1
    return sala_critico

def exibir_informacoes():
    for i in range(len(salas)):
        print(f"\nSala {i + 1}")
        print(f"Média: {media_temperatura(salas[i])}")
        print(f"Registros Críticos: {calcular_registro_critico(salas[i])}")
    print(f"Sala com maior risco: {maior_risco(salas)}")

temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

sala_1 = [0.0] * 4
sala_2 = [0.0] * 4
sala_3 = [0.0] * 4
sala_4 = [0.0] * 4

salas = [sala_1, sala_2, sala_3, sala_4]

adicionar_temperaturas(salas)

exibir_informacoes()