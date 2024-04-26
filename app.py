import os

tarefas = []

# Função para exibir o menu


def interface():
    print('\n          Opções disponíveis\n\n'
          '          [1] Criar uma tarefa\n'
          '          [2] Mostrar as tarefas\n'
          '          [3] Atualizar tarefa\n'
          '          [4] Finalizar tarefa\n'
          '          [5] Excluir tarefa\n'
          '          [6] Encerrar o programa\n')

# função para listar as tarefas


def listar():
    for tarefa in tarefas:
        concluida = tarefa['concluida']
        if concluida == False:
            concluida = ''
        else:
            concluida = '✓'
        print(f"[{tarefa['id']}] [ {concluida} ] {tarefa['nome']}")


def atualizar():
    escolha = int(input('Informe o numero da tarefa que deseja editar: '))
    nome = input('Informe o novo nome da tarefa: ')
    if escolha and nome:
        for tarefa in tarefas:
            if escolha == tarefa['id']:
                tarefa['nome'] = nome
                os.system('cls')
                print(f'\033[92mTarefa atualizada com sucesso\033[0m')
    else:
        print('Ambos os campos precisam ser preenchidos corretamente')

def excluir():
    try:
        listar()
        escolha = int(input('Informe o numero da tarefa desejada: '))
        if escolha:
            for tarefa in tarefas:
                if tarefa['id'] == escolha:
                    tarefas.remove(tarefa)
                    os.system('cls')
                    print(f'\033[92mTarefa removida com sucesso\033[0m')
        else:
            print('Escolha uma tarefa para excluir')
    except:
        print('Ocorreu um erro, tente novamente!')

def finalizar():
    try:
        listar()
        escolha = int(input('Informe o numero da tarefa desejada: '))
        if escolha:
            for tarefa in tarefas:
                if tarefa['id'] == escolha:
                    tarefa['concluida'] = True
        else:
            print('Escolha uma opção para finalizar')
    except:
        print('Ocorreu um erro, tente novamente!')


# Função para verificar se a tarefa existe
def conferirTarefaExistente(nome):
    for tarefa in tarefas:
        if tarefa['nome'] == nome:
            return True
    return False


os.system('cls')
print('\n          Seja bem vindo')

while True:
    try:
        interface()

        escolha = input('Informe a opção desejada: ')

        if escolha == '1':
            nome = input('Informe o nome da tarefa: ')
            if nome:
                if not conferirTarefaExistente(nome):
                    tarefa = {'id': len(tarefas) + 1, 'nome': nome, 'concluida': False}
                    tarefas.append(tarefa)
                    os.system('cls')
                    print(f'\033[92mTarefa {nome} registrada com sucesso\033[0m')
                else:
                    os.system('cls')
                    print(f'\033[91mA tarefa {nome} já existe\033[0m')
            else:
                os.system('cls')
                print('\033[91mNome da tarefa não pode ser vazio\033[0m')

        elif escolha == '6':
            os.system('cls')
            print('\033[94mPrograma encerrado com sucesso!\033[0m')
            break

        elif escolha == '2':
            os.system('cls')
            listar()
        elif escolha == '3':
            os.system('cls')
            listar()
            atualizar()

        elif escolha == '4':
            os.system('cls')
            finalizar()
            listar()
            

        elif escolha == '5':
            os.system('cls')
            excluir()
            
        else:
            os.system('cls')
            print(
                '\033[91mInformou um valor inválido! favor informar o numero da opção desejada...\033[0m')
    except:
        print('ocorreu um erro!')