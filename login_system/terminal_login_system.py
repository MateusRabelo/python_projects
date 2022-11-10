cliente = []
endereco = []

def cadastro():
    
    while True:
        print("Forneça as informações do usuário!")

        dados = {} # dicionário que será passado com todos os dados para a lista 'clientes'
        dados['nomeComp'] = input('Nome: ')
        dados['senha'] = input('Senha: ')

        # 1° endereço de e-mail
        dados['email'] = input('Email: ')
        lista = {i['email']: i for i in clientes} # variável usada cim índice e laço 'for': verifica repetições por meio das chaves.
        
        while dados['email'] in lista: # caso o dado já esteja em uso, o programa solicita uim dado diferente
            dados['email'] = input('Email em uso, tente novamente! Email: ')

        # 2° Login de usuário
        dados['login'] = input('Login: ')
        lista = {i['login']: i for i in clientes}

        while dados['login'] in lista:
            dados['login'] = input('Login em uso, tente novamente! Login: ')

        # 3° telefone do usuário
        dados['telefone'] = input('telefone: ')
        lista = {i['telefone']: i for i in clientes}

        while dados['telefone'] in lista:
            dados['telefone'] = input('Telefone em uso, tente novamente! Telefone: ')


        clientes.append(dados) # método 'append' irá adicionar os dados na lista

        print("Ok! Cadastro concluído")

        opcao = input("Deseja cadastrar mais alguém? [s/n]: ").strip().lower()
        if(opcao == 'n'): # caso o administrador não queira novos usuários o laço 'while True' se encerra
            menu()
            break


def cadEndereco():
    
    while True:
        print("Forneça um login de usuário!")

        lista = {i['login']: i for i in clientes}
        pesq = input('Login: ')

        # endereço só será cadastrado a um usuário válido

        if pesq in lista:
            print("Forneça o endereço do cliente: ")

            destino = {} # dicionário contendo apenas informações de endereço do cliente
            destino['id'] == pesq
            destino['estado'] = input('Estado: ')
            destino['cidade'] = input('Cidade: ')
            destino['rua'] = input('Rua e número:')
            destino['cep'] = input('Cep: ')

            endereco.append(destino) # será armazenado em outra lista

        else:
            print('\nUsuário não encontrado!\n')

        opcao = input("Deseja cadastrar mais algum endereço? [s/n]: ").strip().lower()
        if(opcao == 'n'): # caso o administrador não queira novos usuários o laço 'while True' se encerra
            menu()
            break 
        

def mostrarDados():
    
    while True:
        print('Forneça o login para consultar os dados de um usuário!')

        lista = {i['login']: i for i in clientes}
        lista2 = {i['id']: i for i in endereco}

        # agora, teremos dois casos onde o cliente pode oui não estar, com o endereço cadastrado (obs:
        # o mesmo login deverá estar contido em ambas as listas: clientes e endereços).

        pesq = input("Login: ")

        if pesq in lista and pesq not in lista2:

            print(f'Dados do cliente [{pesq.upper()}]: {lista[pesq]}') # eventualmente o input 'pesq' estará na lista
            # e casoi seja 'True', através do operador 'in'm irá retornar os dados do usuário

            print('\nEndereço não encontrado!\n')
        
        elif pesq in lista and pesq in lista2:

            print(f'\nDados do cliente [{pesq.upper()}]: {lista[pesq]}')
            print(f'\nEndereço do cliente [{pesq.upper()}]: ')
            print('')
            
            resultado = list(filter(lambda item : item['id'] == pesq, endereco)) # filter com a função lambda irá
            # filtrar os resultados a partir de uma chave específica dentroi de uma lista com dicionários

            for i in resultado:
                print(i)
            print('')

        else:
            print('\nUsuário não encontrado!\n')

        opcao = input("Deseja consultar outro cliente? [s/n]: ").strip().lower()
        if(opcao == 'n'): # caso o administrador não queira novos usuários o laço 'while True' se encerra
            menu()
            break 


def mostrarClientes():
    
    while True:
        print('\nUsuários Cadastrados: \n')

        for i in clientes: # variável 'i' passa na lista 'clientes' buscando apenas as informações com índice 'login' e 'nomeComp', logo após retornando o output dos dados.
            print('Nome:', i['nomeComp'], 'Login:', i['login'])

        print('')

        opcao = input("Deseja conferir novamente? [s/n]: ").strip().lower()
        if(opcao == 'n'): # caso o administrador não queira novos usuários o laço 'while True' se encerra
            menu()
            break

def menu():
    print('***************************************')
    print(' [1] Cadastrar Cliente')
    print(' [2] Cadastrar Endereços do Cliente')
    print(' [3] Consultar Cliente')
    print(' [4] Consultar Banco de Dados')
    print(' [0] Sair')
    print('***************************************')

menu()

while True:

    x = int(input('Escolha > [1] [2] [3] [4] [0]: '))

    while x > 4 or x < 0:
        x = int(input('Erro, tente novamente! Escolha uma opção: ')) # caso os numeros não estejam presentes no menui, o programa irá repetí-lo

    if x == 1:
        cadastro()
    elif x == 2:
        cadEndereço()
    elif x == 3:
        mostrarDados()
    elif x == 4:
        mostrarClientes()
    else:
        print('\nPrograma encerrado!\n')
        break