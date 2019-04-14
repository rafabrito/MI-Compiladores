import string

# Lista com Palavras reservadas
reservada = ['programa', 'constantes', 'variaveis', 'metodo', 'resultado', 'principal', 'se', 'entao',
             'senao', 'enquanto', 'leia','escreva', 'vazio', 'inteiro', 'real', 'boleano', 'texto',
             'verdadeiro', 'falso']

# Lista com letras de [a..z] e [A...Z]
letra = string.ascii_letters


# Lista com os delimitadores
delimitador = ';,()[]{}+-.*/'

#lista de digitos
digito = '0123456789'

reader = open("teste.txt", 'r')

def lerarquivo():
    texto = reader.readlines()
    for a in range(len(texto)):
        texto[a] = texto[a] + '^'
    return texto

def aritmetico():
    texto = lerarquivo()
    linha = 0
    coluna = 0

    while linha in range(len(texto)):


        while coluna in range(len(texto[linha])):
            if(texto[linha][coluna] == '+' ):
                if(texto[linha][coluna+1]=='+'):
                    print('++')
                    coluna+=1
                else:
                    print('+')

            if (texto[linha][coluna] == '-'):
                if(texto[linha][coluna+1]=='-'):
                    print('--')
                    coluna+=1
                else:
                    print('-')

            if (texto[linha][coluna] == '*'):
                print('*')

            if(texto[linha][coluna]=='/'):
                print('/')
            coluna +=1
        coluna = 0
        linha+=1


def identificador():
    texto = lerarquivo()
    linha = 0
    coluna = 0

    while linha in range(len(texto)):

        while coluna in range(len(texto[linha])):
            if (texto[linha][coluna] in letra):
                char_temp = ''
                erro = 0

                while coluna in range(len(texto[linha])):
                    if (texto[linha][coluna] in letra or texto[linha][coluna] in digito or texto[linha][coluna] == '_'):
                        char_temp += texto[linha][coluna]
                    elif (texto[linha][coluna] == ' ' or texto[linha][coluna] in delimitador or texto[linha][
                        coluna] == '\r' or texto[linha][coluna] == '\t'):
                        break
                    elif (texto[linha][coluna] != '^' and texto[linha][coluna] != '\n'):
                        char = texto[linha][coluna]
                        print('Erro Léxico, Identificador Inválido: {} na linha {} e na coluna {}'.format(
                        texto[linha][coluna], linha, coluna))
                        erro += 1
                    coluna += 1
                if (erro >= 1):
                    while coluna in range(len(texto[linha + 1])):
                        if (texto[linha][coluna] == ' ' or texto[linha][coluna] in delimitador or texto[linha][
                        coluna] == '\r' or texto[linha][coluna] == '\t'):
                            coluna -= 1  # Retorna para o caracter anterior para definir o identificar
                            break
                        coluna += 1
                else:
                    if (char_temp in reservada):
                        print('Aqui classifico o token como Palavra Reservada')
                    else:
                        print('Aqui classifico o token como Identificador')
            coluna += 1
        coluna = 0
        linha += 1


def comentario():
    texto = lerarquivo()
    linha = 0
    coluna = 0

    while linha in range(len(texto)):

        while coluna in range(len(texto[linha])):
            #Esse é o automato do simbolo '/' barra
            if (texto[linha][coluna] == '/'):
                # Sub-automato de comentário de linha
                if (texto[linha][coluna] == '/' and texto[linha][coluna + 1] == '/'):
                    coluna = len(texto[linha])
                    break
                # Sub-automato de comentário de bloco
                elif (texto[linha][coluna] == '/' and texto[linha][coluna + 1] == '*'):
                    begin_linha = linha
                    begin_coluna = coluna
                    cont = True
                    char = texto[linha][coluna]
                    while cont and not (texto[linha][coluna] == '*' and texto[linha][coluna + 1] == '/'):
                        if ((coluna + 2) < len(texto[linha])):
                            coluna += 1
                            char += texto[linha][coluna]
                        else:
                            coluna = 0
                            linha += 1
                            if (linha == len(texto)):
                                print("Erro Lexico - Comentario de bloco nao foi fechado - linha {} e coluna {} \n".format(
                                    begin_linha, begin_coluna))
                                cont = False
                    coluna += 1
                # Sub-automato de simbolo  algébrico de divisão
                else:
                    print('/')
            coluna +=1
        coluna = 0
        linha+=1


aritmetico()
reader.close()