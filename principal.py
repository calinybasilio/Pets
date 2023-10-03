import datetime

class PetShop:
    def __init__(self, nome, preco_pequeno_semana, preco_grande_semana, preco_pequeno_fds, preco_grande_fds):
        self.nome = nome
        self.preco_pequeno_semana = preco_pequeno_semana
        self.preco_grande_semana = preco_grande_semana
        self.preco_pequeno_fds = preco_pequeno_fds
        self.preco_grande_fds = preco_grande_fds

    def calcular_preco(self, caes_pequenos, caes_grandes, data):
        if data.weekday() < 5:  # Dias úteis (segunda a sexta-feira)
            return caes_pequenos * self.preco_pequeno_semana + caes_grandes * self.preco_grande_semana
        else:  # Fim de semana (sábado ou domingo)
            return caes_pequenos * self.preco_pequeno_fds + caes_grandes * self.preco_grande_fds

def obter_data_valida():
    while True:
        data_str = input("Por favor, informe a data em que deseja atendimento (dd/mm/aaaa): ")
        try:
            dia, mes, ano = map(int, data_str.split('/'))
            data_atendimento = datetime.date(ano, mes, dia)
            return data_atendimento
        except ValueError:
            print("Formato de data inválido. Use dd/mm/aaaa.")

def obter_quantidade_animais_valida():
    while True:
        try:
            caes_pequenos = int(input("Informe a quantidade de cães PEQUENOS para qual deseja atendimento: "))
            caes_grandes = int(input("Informe a quantidade de cães GRANDES para qual deseja atendimento: "))
            if caes_pequenos >= 0 and caes_grandes >= 0:
                return caes_pequenos, caes_grandes
            else:
                print("A quantidade de cães deve ser um número não negativo.")
        except ValueError:
            print("Quantidade inválida. Insira um número inteiro não negativo para a quantidade de cães.")

# Criando objetos PetShop com os preços
meu_canino = PetShop("Meu Canino Feliz", 20, 40, 24, 48)
vai_rex = PetShop("Vai Rex", 15, 50, 20, 55)
chow_chawgas = PetShop("Chow Chawgas", 30, 45, 30, 45)

# Solicitando informações ao cliente
data_atendimento = obter_data_valida()
caes_pequenos, caes_grandes = obter_quantidade_animais_valida()

# Calculando os preços para cada pet shop
preco_meu_canino = meu_canino.calcular_preco(caes_pequenos, caes_grandes, data_atendimento)
preco_vai_rex = vai_rex.calcular_preco(caes_pequenos, caes_grandes, data_atendimento)
preco_chow_chawgas = chow_chawgas.calcular_preco(caes_pequenos, caes_grandes, data_atendimento)

# Criando uma lista com os resultados
lista = [(preco_meu_canino, 2, "Meu Canino Feliz"), (preco_vai_rex, 1.7, "Vai Rex"), (preco_chow_chawgas, 0.8, "Chow Chawgas")]

# Ordenando a lista pelo preço total e pela distância
melhor_pet_shop = min(lista, key=lambda x: (x[0], -x[1]))

# Imprimindo o resultado
print(f"O melhor pet shop é o {melhor_pet_shop[2]}, com um valor total de R${melhor_pet_shop[0]:.2f}.")
