import datetime
from operator import itemgetter

#Funções com cálculos referentes aos serviços dos Pets

#Meu Canino Feliz - Durante a Semana
def meu_Canino_Semana (caesPequenos, caesGrandes):
    meuCanino_P_semana = caesPequenos * 20
    meuCanino_G_semana = caesGrandes * 40
    return meuCanino_G_semana + meuCanino_P_semana

#Meu Canino Feliz - Durante o final de semana
def meu_Canino_FDS (caesPequenos, caesGrandes):
    vaiRex_P_FDS = caesPequenos * (20 + (20 * 0.2))
    vaiRex_G_FDS = caesGrandes * (40 + (40 * 0.2))
    return vaiRex_P_FDS + vaiRex_G_FDS

#Vai Rex - Durante a Semana
def vai_Rex_Semana (caesPequenos, caesGrandes):
    vaiRex_Uteis_P = caesPequenos * 15
    vaiRex_Uteis_G = caesGrandes * 50
    return vaiRex_Uteis_P + vaiRex_Uteis_G

#Vai Rex - Durante o Final de Semana
def vai_Rex_FDS(caesPequenos, caesGrandes):
    vaiRex_P_FDS = caesPequenos * 20
    vaiRex_G_FDS = caesGrandes * 55
    return vaiRex_P_FDS + vaiRex_G_FDS

#Chow Chawgas- Durante todos os dias
def chow_Chagas (caesPequenos, caesGrandes):
    chowChawgas_P = caesPequenos * 30
    chowChawgas_G = caesGrandes * 45
    return chowChawgas_P + chowChawgas_G

#Solicitando data ao cliente
print("Por favor, informe a data em que deseja atendimento (dd/mm/aaaa): ")
data = str(input())

#Solicitando quantidade de cães pequenos que o cliente deseja atendimento
print("Informe a quantidade de cães PEQUENOS para qual deseja atendimento: ")
caesPequenos = int(input())

#Solicitando quantidade de cães grandes que o cliente deseja atendimento
print("Informe a quantidade de cães GRANDES para qual deseja atendimento: ")
caesGrandes = int(input())

#Tratando data inserida pelo cliente
d, m, a = data.split('/')
ano = int(a)
mes = int(m)
dia = int(d)

data_atendimento = datetime.date(ano, mes, dia)

dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
dia_semana = dias[data_atendimento.weekday()]
#print(dia_semana)
#print(data_atendimento)

#Chamando funções conforme data de atendimento solicitado
if dia_semana == 'Sábado' or dia_semana == 'Domingo':
    meu_canino = meu_Canino_FDS(caesPequenos, caesGrandes)
    vai_rex = vai_Rex_FDS(caesPequenos, caesGrandes)
    chow_chawgas = chow_Chagas(caesPequenos, caesGrandes)
else:
    meu_canino = meu_Canino_Semana(caesPequenos, caesGrandes)
    vai_rex = vai_Rex_Semana(caesPequenos, caesGrandes)
    chow_chawgas = chow_Chagas(caesPequenos, caesGrandes)
    #print("Entrou!!!")

#Lista com tuplas possuindo retorno das funções, distância, e nome do PetShop
lista = [(meu_canino, 2, "Meu Canino Feliz"), (vai_rex, 1.7, "Vai Rex"), (chow_chawgas, 0.8, "Chow Chawgas")]

#Ordenação da lista
total = (sorted(lista, key=itemgetter(0, 1))[0])

#Imprimindo o Pet Shop com o melhor valor e mais próximo do canil do Sr. Eduardo
print("O melhor canil é o", total[2], ", tendo como valor total dos banhos solicitados R$", total[0])
