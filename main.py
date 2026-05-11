def adicionar_temperaturas(sala, numero_sala, temperaturas):
    numero_sala -= 1
    for i in range(len(temperaturas)):
        sala[i] = temperaturas[numero_sala][i]

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

def maior_risco(sala_1, sala_2, sala_3, sala_4):
    critico_sala_1 = calcular_registro_critico(sala_1)
    critico_sala_2 = calcular_registro_critico(sala_2)
    critico_sala_3 = calcular_registro_critico(sala_3)
    critico_sala_4 = calcular_registro_critico(sala_4)
    sala_critico = 0
    for _ in sala_1:
        maior_critico = critico_sala_1
        if critico_sala_2 > maior_critico:
            sala_critico = 2
        elif critico_sala_3 > maior_critico:
            sala_critico = 3
        elif critico_sala_4 > maior_critico:
            sala_critico = 4
        else:
            sala_critico = 1
    return sala_critico

def exibir_informacoes(sala, numero_sala):
    print(f"\nSala {numero_sala}")
    print(f"Média: {media_temperatura(sala)}")
    print(f"Registros Críticos: {calcular_registro_critico(sala)}")

temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

sala_1 = [0.0] * 4
adicionar_temperaturas(sala_1, 1, temperaturas)

sala_2 = [0.0] * 4
adicionar_temperaturas(sala_2, 2, temperaturas)

sala_3 = [0.0] * 4
adicionar_temperaturas(sala_3, 3, temperaturas)

sala_4 = [0.0] * 4
adicionar_temperaturas(sala_4, 4, temperaturas)

exibir_informacoes(sala_1, 1)
exibir_informacoes(sala_2, 2)
exibir_informacoes(sala_3, 3)
exibir_informacoes(sala_4, 4)

print(f"Sala com maior temperatura: {maior_risco(sala_1, sala_2, sala_3, sala_4)}")