#print("**********Menu**********")
#print("Criar Usuário")
#print("Depositar")
#print("Sacar")

#Importação de biblioteca
from datetime import datetime

saldo = 0
limite = 500
numero_saques = 0
limites_saques = 3
usuarios =[]#criei uma lista vazia , pois serão adicionados valores posteriormente
contas = []
agencia='0001'

#Menu com as opções que o usuário vai escolher
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
    return input('Qual opção deseja')
#Função depósito
def deposito(valor,saldo):
    #  vou receber o valor do depósito e somar ao saldo
    if valor > 0 :
        saldo += valor
        #print mostrando o valor depositado
        print(f'Você depositou R${valor}')      
    else:
        print('Valor do deposito Ínválido.Verifique a quantia digitada.')
    
    return saldo
#Função saque
def saque(saque,saldo):


   global  numero_saques,limites,limites_saques
    #De acordo com a documentação Python , váriaveis globais não ficam presas ao limite do escopo da função.
   if numero_saques >= limites_saques:
    print('Você atingiu o limite de saques de sua conta.Tente novamente no proximo dia útil')
   else:
        if saque <= 0:
            print('Saque Inválido.Verifique o valor e tente novamente.')
        elif saque > limite :
            print('Valor limite excedido.Verifique o valor e tente novamente.')
        elif saque > saldo :
            print('Saldo insuficiênte.Verifique o valor e tente novamente.')
        else:
            saldo -= saque
            numero_saques += 1
            
        return saldo   
#Função extrato
def extrato (saldo):  
    hora = datetime.now() #Obtem a hora atual 
    horaatual = hora.strftime('%d/%m/%Y/ %H:%M')
    print('=============Extrato=============')
    print(f'{horaatual} \nSaldo disponível:{saldo}' )
    print('\n=============Extrato=============')
#Função sair
def sair():
    print('***************Encerrando o Sistema***************')
#Função criar usuários
def novo_usuario(usuario):
    cpf = int(input('Digite seu cpf (Somente números);'))
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('Usuário já cadastrado na base de dados!')
        return

    nome = str('Escreva seu nome completo : ')
    data_nascimento = input('Informe a data de nascimento (dd--mm--aa) :')
    endereço = input('Informe seu endereço (Rua , numero,cep,bairro e cidade)')
    #o append adiciona usuário ao meu banco
    usuarios.append(f'nome:{nome},data de nascimento:{data_nascimento},endereço:{endereço}')
    print('Cadastro realizado com sucesso!')
#Função filtrar usuários
def filtrar_usuario (cpf,usuarios):
    # Filtra um usuário em uma lista de usuários com base no CPF fornecido.
    #O CPF do usuário que se deseja buscar.
    #usuarios (list): Uma lista de dicionários, onde cada dicionário representa um usuário e contém uma chave 'cpf' com o CPF do usuário.
    #None: Retorna o dicionário do usuário correspondente ao CPF, 
    #None se nenhum usuário for encontrado.
    
    usuarios_filtrados = [usuario for usuario in usuarios if usuarios['cpf'] ==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

while True:
    op = menu()

    if op =='d':
        valor = float(input('Digite o vaor do Depósito: '))
        saldo = deposito(valor,saldo)
    if op =='s':
        valor = float(input('Digite o valor de Saque : '))
        saldo = saque(valor,saldo)

    break