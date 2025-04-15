# print("**********Menu**********")
# print("Criar Usuário")
# print("Depositar")
# print("Sacar")

from datetime import datetime

# Variáveis principais do sistema bancário
saldo = 0
limite = 500
numero_saques = 0
limites_saques = 3
usuarios = []  # Lista para armazenar os usuários
contas = []
agencia = '0001'

# Função que exibe o menu principal
def menu():
    print('''
    ================== MENU ==================
    [1] Criar Usuário
    [2] Criar Conta
    [3] Listar Contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==========================================
    ''')
    return input('Selecione uma opção: ')

# Função para realizar depósitos
def deposito(valor, saldo):
    if valor > 0:
        saldo += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso.')
    else:
        print('Valor inválido. Por favor, insira uma quantia positiva.')
    return saldo

# Função para realizar saques
def saque(valor, saldo):
    global numero_saques, limite, limites_saques

    if numero_saques >= limites_saques:
        print('Limite diário de saques atingido. Tente novamente no próximo dia útil.')
    elif valor <= 0:
        print('Valor de saque inválido. Por favor, insira um valor positivo.')
    elif valor > limite:
        print(f'Valor excede o limite por saque (R${limite:.2f}).')
    elif valor > saldo:
        print('Saldo insuficiente para esta operação.')
    else:
        saldo -= valor
        numero_saques += 1
        print(f'Saque de R${valor:.2f} realizado com sucesso.')
    return saldo

# Função para exibir o extrato
def extrato(saldo):
    hora = datetime.now()
    hora_formatada = hora.strftime('%d/%m/%Y - %H:%M')
    print('\n============ EXTRATO ============')
    print(f'Data/Hora: {hora_formatada}')
    print(f'Saldo atual: R${saldo:.2f}')
    print('=================================\n')

# Função para encerrar o sistema
def sair():
    print('\nEncerrando o sistema bancário. Até a próxima!')

# Função para criar um novo usuário
def novo_usuario(usuarios):
    cpf = int(input('Digite seu CPF (somente números): '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Usuário já cadastrado em nossa base de dados.')
        return

    nome = input('Digite seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço completo (Rua, número, CEP, bairro, cidade): ')

    usuarios.append({
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento,
        'endereco': endereco
    })

    print('Cadastro realizado com sucesso!')

# Função para localizar usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Loop principal do sistema
while True:
    opcao = menu()

    if opcao == '1':
        novo_usuario(usuarios)
    elif opcao == 'd':
        valor = float(input('Informe o valor para depósito: R$'))
        saldo = deposito(valor, saldo)
    elif opcao == 's':
        valor = float(input('Informe o valor para saque: R$'))
        saldo = saque(valor, saldo)
    elif opcao == 'e':
        extrato(saldo)
    elif opcao == 'q':
        sair()
        break
    else:
        print('Opção inválida. Por favor, selecione uma opção do menu.')
