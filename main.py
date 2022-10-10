import data_related
import menu_function

def menu():
    print(f'#######################################\n'
          f'### Menu de gerenciamento de Grupos ###\n'
          f'#######################################\n')
    Entrada = int(input(f'Consultar um grupo de trabalho (Escreva 1)\n'
                          f'Editar um grupo de trabalho (Escreva 2)\n'
                          f'Inserir um grupo de trabalho em uma lista (Escreva 3)\n'
                          f'Remover um grupo de trabalho em uma lista (Escreva 4)\n'
                          f'Salvar de uma lista para um JSON os grupos de trabalho (Escreva 5)\n'
                          f'Fechar o program (Escreva 6)\n'
                          f'Selecione uma das opções acima digitando apenas o numero: '))
    return Entrada


def consulta_grupo(opcao, qnt_grupos):
    if opcao == 1:
        acao = 'consulta'
    elif opcao == 2:
        acao = 'edição'

    print(f'Você escolheu a opção {opcao}, {acao} de grupos \n'
          f'Temos {qnt_grupos} disponíveis para {acao}.\n')
    grupo_consultado = int(input(f'digite um numero de 1 a {qnt_grupos} para escolher o grupo: '))
    print(f'Você escolheu o grupo {grupo_consultado} para {acao}. abaixo as informações do grupo escolhido:')
    return grupo_consultado


def manipulando_grupos_json():
    data = data_related.open_json()
    fechar = False
    while fechar != True:
        opcao = menu()
        if opcao == 1: #Consultar um grupo de trabalho (Escreva 1)
            while opcao == 1:
                qnt_grupos = len(data)
                grupo_consultado = int(consulta_grupo(opcao, qnt_grupos))
                print(f'{data[grupo_consultado - 1]}')
                Entrada = int(input(print(f'\nDeseja consultar outro grupo (1), ou voltar ao menu (2)?')))
                if Entrada != 1:
                    opcao = 7

        if opcao == 2:  # Editar um grupo de trabalho (Escreva 2)
            while opcao == 2:
                qnt_grupos = len(data)
                grupo_consultado = int(consulta_grupo(opcao, qnt_grupos))
                print(f'{data[grupo_consultado - 1]}')
                data, opcao = menu_function.edita_grupo(data, grupo_consultado, opcao)
                print(f'{data[grupo_consultado - 1]}')
                Entrada = int(input(f'\nDeseja editar outro grupo (1), ou voltar ao menu (2)?'))
                if Entrada != 1:
                    opcao = 7
        if opcao == 3:
            data = menu_function.add_grupo()

        if opcao == 4:
            data = menu_function.delete_grupo(data)

        if opcao == 5:
            data = data_related.save_json(data)

        if opcao == 6:
            print(f'Encerrando o menu e fechando o programa')
            fechar = True
        if opcao == 7:
            continue


if __name__ == '__main__':
    manipulando_grupos_json()
