import os

dados_cliente = []

setores = {
    '1': 'Abertura de Conta',
    '2': 'Caixa',
    '3': 'Gerente Pessoa Física',
    '4': 'Gerente Pessoa Jurídica',
}

saldo = 1945.00

def exibir_nome_do_programa():
    print('''
    ░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░██████╗░░█████╗░███╗░░██╗██╗░░██╗
    ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗████╗░██║██║░██╔╝
    ██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║██████╦╝███████║██╔██╗██║█████═╝░
    ██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║██╔══██╗██╔══██║██║╚████║██╔═██╗░
    ╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝██████╦╝██║░░██║██║░╚███║██║░╚██╗
    ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
    ''')

def sacar_depositar_dinheiro():
    escolha_dinheiro = input('Digite 1 se deseja sacar ou digite 2 se deseja depositar o dinheiro: ')
    print()
    if escolha_dinheiro == '1':
        while True:
            sacar = float(input('digite o valor que deseja sacar: '))
            if sacar > saldo:
                print('Erro: Saldo insuficiente')
            else:
                saldo_saque = (saldo - sacar)
                print(f'O saque de R${sacar} foi feito com sucesso, seu novo saldo é de R$:{saldo_saque}')
                break
    elif escolha_dinheiro == '2':
        depositar = float(input('digite o valor que deseja depositar: '))
        saldo_deposito = (saldo + depositar)
        print(f'O deposito de R${depositar} foi feito com sucesso, seu novo saldo é de R$:{saldo_deposito}')
    else:
        escolha_invalida()

def formatar_cpf(cpf):
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
   
    return f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"

def solicitar_atendimento():

    while True:
        nome = input("Digite seu primeiro nome (apenas letras): ")
        if nome.isalpha():
            break
        else:
            print("Erro: Digite apenas letras, sem números ou símbolos.")

    while True:
        cpf_usuario = input("Digite seu CPF (somente números): ")
        if len(cpf_usuario) == 11:
            break
        else:
            print('Erro: CPF inválido')
    cpf_formatado = formatar_cpf(cpf_usuario)

    print()
    print(f'Nome: {nome}')
    print(f'CPF: {cpf_formatado}')
    print()
    print("Escolha o numero da opcao de atendimento desejada:")
    print("1 - Abertura de Conta")
    print("2 - Caixa")
    print("3 - Gerente Pessoa Fisica")
    print("4 - Gerente Pessoa Juridica")
    print("5 - Voltar")
    print()

    escolha_setor = input('Escolha o setor desejado: ')
    setor_nome = setores.get(escolha_setor, "Setor Desconhecido")

    cliente = {
    'nome': nome,
    'cpf': cpf_formatado,
    'setor': (setor_nome),
    }

    dados_cliente.append(cliente)

    try:
        if escolha_setor == '1':
            print(f'Parabens {cliente['nome']}, a sua conta no CPF:{cliente['cpf']} foi aberta.')
            voltar_ao_menu()
        elif escolha_setor == '2':
            print(f'Olá {cliente['nome']} bem vindo ao caixa, seu saldo é de: {saldo}')
            sacar_depositar_dinheiro()
            voltar_ao_menu()
        elif escolha_setor == '3':
            print('Por favor aguarde um pouco, o gerente já irá te atender.')
            voltar_ao_menu()
        elif escolha_setor == '4':
            input('Digite o CNPJ da empresa: ')
            print('Por favor aguarde um pouco, o gerente já irá te atender.')
            voltar_ao_menu()
        elif escolha_setor == '5':
            main()
        else: 
            print('Setor não encontrado')
            solicitar_atendimento()
    except ValueError:
        print('Setor não encontrado')
        solicitar_atendimento()

def listar_atendimentos():
    for i, cliente in enumerate(dados_cliente, start=1):
        print(f"--- Cliente {i} ---")
        print(f"Nome : {cliente['nome']}")
        print(f"CPF  : {cliente['cpf']}")
        print(f"Setor: {cliente['setor']}")
    
    if dados_cliente == []:
        print('Nenhum atendimento registrado.')

def voltar_ao_menu():
    voltar_menu = input('Aperte qualquer tecla para voltar ao menu principal.')
    if voltar_menu == '':
        main()

def escolha_invalida():
    print('Escolha invalida, por favor escolha uma oção valida')
    main()

def sair():
    quit()

def exibir_opcoes():
    print("Bem-vindo ao sistema de atendimento")
    print()
    print("Escolha uma das opcoes abaixo: ")
    print("1 - Solicitar atendimento")
    print("2 - Listar atendimentos registrados")
    print("3 - Sair")
    print()

def escolha_menu():
    escolha = input('Escolha a opção desejada: ')

    try:
        if escolha == '1':
            solicitar_atendimento()
        elif escolha == '2':
            listar_atendimentos()
            voltar_ao_menu()
        elif escolha == '3':
            sair()
        else:
            escolha_invalida()
    except ValueError:
        escolha_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolha_menu() 

if __name__ == '__main__':
    main()
