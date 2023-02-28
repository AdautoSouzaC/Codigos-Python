import sqlite3

banco = sqlite3.connect("banco")
cursor = banco.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text,idade integer,email text)")
#cursor.execute("CREATE TABLE pessoas (id interger autoincrement, nome text,idade integer,email text)")
cont = 0
while cont != 1 :
    opt = input (' 1-inserir usuario \n 2-visualizar \n 3-deletar \n 4-sair \n -- >')
    # \n quebra de linha
    if opt =='1':
        nome = input('digite seu nome: ')
        idade = input('digite a idade: ')
        email = input('digite se e-mail :')
        dados = [nome, idade, email]
        sql = "INSERT INTO pessoas (nome, idade, email) values(?, ?, ?)"
        cursor.execute(sql, dados)
        banco.commit()
    elif opt == '2':
        sql_visualizar = 'select * from pessoas'
        informacoes = cursor.execute (sql_visualizar)
        for informacao in informacoes:
            print(informacao)
    elif opt == '3':
        nome =  input('qual nome deseja exluir : ')
        excluir = [nome]
        sql_excluir = 'delete from pessoas where nome = ? ' 
        cursor.execute (sql_excluir, excluir)
        banco.commit()
        print("usuario excluido com sucesso")
    else: 
        print("saindo do programa . . .")
        cont += 1 
banco.commit()
banco.close
