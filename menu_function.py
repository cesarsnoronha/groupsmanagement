
def edita_grupo(data, grupo_consultado, opcao): #(opcao, qnt_grupos, data, grupo_consultado):
    editar1 = int(input(f'Você deseja editar o tema (1), os alunos (2), se o grupo está fechado (3) ou voltar (4)? \n'))
    if editar1 == 1:
        novotema = input(f'Qual o novo tema do grupo? \n')
        data[grupo_consultado - 1]['tema'] = novotema #editar tema
        # opcao = 7
    elif editar1 == 2:
        for item in data[grupo_consultado - 1]['alunos']:
            aluno = data[grupo_consultado - 1]['alunos'].index(item)
            data[grupo_consultado - 1]['alunos'][aluno] = input(f'Quem irá substituir o aluno {item}?\n')

    elif editar1 == 3:
        if data[grupo_consultado - 1]['fechado'] == True:
            data[grupo_consultado - 1]['fechado'] = False
        elif data[grupo_consultado - 1]['fechado'] == False:
            data[grupo_consultado - 1]['fechado'] = True
        # opcao = 7
    elif editar1 == 4:
        opcao = 7
    else:
        print("Opção inválida")
        # pedir a opção novamente
    return data, opcao

def add_grupo(data):
    print(f'Você escolheu a opção de adicionar grupos \n')
    tema = input(f'Qual o novo tema do grupo? \n')
    aluno = ['a', 'b', 'c']
    for i in range(0, 3):
        aluno[i] = input(f'Qual o nome do aluno {i}? \n')
    fechado = int(input(f'O grupo está aberto (0) ou fechado (1)? \n'))
    if fechado == 1:
        fecha = True
    elif fechado == 0:
        fecha = False
    data.append({
        'tema': tema,
        'alunos': [aluno[0], aluno[1], aluno[2]],
        'fechado': fecha
    })

    return data

def delete_grupo(data):
    tamanho = len(data)
    print(f'Você escolheu a opção de deletar grupos \n')
    for idx, obj in enumerate(data):
        print(idx, obj)
    grupo_deletado = int(input(f'Qual o grupo você deseja deletar (digite 1 - {tamanho-1})? \n'))
    data.pop(grupo_deletado)
    return data