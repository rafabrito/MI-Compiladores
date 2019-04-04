import os.path

nome_arquivo = input('Digite o nome do arquivo e extenção: ')

if(os.path.exists(nome_arquivo)):
    arq = open('teste.txt', 'r')

    linha = arq.readline()
    num_linha = 1

    while linha:
        cont = 0

        size_linha = len(linha)

        while cont < size_linha:
            char_atual = linha[cont]
            char_proximo = None
            print('Primeiro while caracter atual {}'.format(char_atual))

            if (cont + 1 < size_linha):
                char_proximo = linha[cont + 1]
                print('If próximo caracter {}'.format(char_proximo))

            if (char_atual.isalpha()):
                temp = char_atual
                cont += 1
                while (cont < size_linha):
                    char_atual = linha[cont]
                    char_proximo = None
                    print('Caracter atual {}'.format(char_atual))

                    if (cont + 1 < size_linha):
                        char_proximo = linha[cont + 1]
                        print('Próximo caracter {}'.format(char_proximo))

                    if (char_atual.isalpha() or char_atual.isdigit() or char_atual == '_'):
                        temp += char_atual
                        print('Consumindo os caracteres... {}'.format(temp))
                    else:
                        print('Entrou no else')

                    cont += 1
            linha = arq.readline()
            num_linha += 1

    arq.close()
else:
    print('\nArquivo não existe!!')

    print('\nO arquivo será criado agora!!')
    novo_arquivo = input('\nDigite o arquivo e extenção: ')

    arq = open(novo_arquivo, 'w')

    codigo = input('Digite o Conteudo do arquivo: ')
    arq.write(codigo)

    arq.close()
