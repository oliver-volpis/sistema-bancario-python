from datetime import datetime

# Variáveis iniciais
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = '0001'
extrato_operacoes = []

# Menu com as opções
def menu():
    print('''
        **********Menu**********
        (1) Criar Usuário
        (2) Criar Conta
        (3) Listar Contas
        (d) Depositar
        (s) Sacar
        (e) Extrato
        (q) Sair
    ''')
    return input('Escolha uma opção: ')

# Função de depósito
def deposito(valor, saldo):
    if valor > 0:
        saldo += valor
        extrato_operacoes.append(f"{datetime.now().strftime('%d/%m/%Y %H:%M')} - Depósito: R${valor:.2f}")
        print(f'Você depositou R${valor:.2f}')
    else:
        print('Valor do depósito inválido.')
    return saldo

# Função de saque
def saque(valor, saldo):
    global numero_saques

    if numero_saques >= LIMITE_SAQUES:
        print('Limite diário de saques atingido.')
    elif valor <= 0:
        print('Valor inválido para saque.')
    elif valor > limite:
        print('Valor excede o limite de R$500 por saque.')
    elif valor > saldo:
        print('Saldo insuficiente.')
    else:
        saldo -= valor
        numero_saques += 1
        extrato_operacoes.append(f"{datetime.now().strftime('%d/%m/%Y %H:%M')} - Saque: R${valor:.2f}")
        print(f'Saque de R${valor:.2f} realizado com sucesso.')

    return saldo

# Função de extrato
def extrato(saldo):
    print('============= Extrato =============')
    if not extrato_operacoes:
        print('Nenhuma operação realizada.')
    else:
        for operacao in extrato_operacoes:
            print(operacao)
    print(f'Saldo atual: R${saldo:.2f}')
    print('===================================')

# Função para sair
def sair():
    print('*************** Encerrando o Sistema ***************')

# Função para criar novo usuário
def novo_usuario():
    cpf = input('Digite seu CPF (somente números): ')
    usuario = filtrar_usuario(cpf)

    if usuario:
        print('Usuário já cadastrado!')
        return

    nome = input('Digite seu nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe seu endereço (Rua, número - Bairro - Cidade/Estado): ')

    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print('Usuário cadastrado com sucesso!')

# Função para filtrar usuário pelo CPF
def filtrar_usuario(cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função para criar conta
def criar_conta():
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({'agencia': AGENCIA, 'numero_conta': numero_conta, 'usuario': usuario})
        print(f'Conta criada com sucesso! Agência: {AGENCIA} Conta: {numero_conta}')
    else:
        print('Usuário não encontrado!')

# Função para listar contas
def listar_contas():
    for conta in contas:
        print(f'''
        Agência: {conta["agencia"]}
        Conta: {conta["numero_conta"]}
        Titular: {conta["usuario"]["nome"]}
        ''')

# Loop principal
while True:
    opcao = menu()

    if opcao == '1':
        novo_usuario()
    elif opcao == '2':
        criar_conta()
    elif opcao == '3':
        listar_contas()
    elif opcao == 'd':
        valor = float(input('Digite o valor do depósito: '))
        saldo = deposito(valor, saldo)
    elif opcao == 's':
        valor = float(input('Digite o valor do saque: '))
        saldo = saque(valor, saldo)
    elif opcao == 'e':
        extrato(saldo)
    elif opcao == 'q':
        sair()
        break
    else:
        print('Opção inválida. Tente novamente.')
