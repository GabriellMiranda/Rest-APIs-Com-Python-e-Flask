from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Gabriel', idade=23)
    pessoa.save()


def consulta():
    # pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    print(pessoa.nome)
    print(pessoa.idade)
    '''
        for p in pessoa:
        print(p.nome)
        print(p.idade)
    '''


def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.idade = 21
    pessoa.save()


def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuario():
    usuario = Usuarios.query.all()
    print(usuario)

if __name__ == '__main__':
    insere_usuario("rafael", '123')
    insere_usuario("gabriel", '321')
    consulta_todos_usuario()
    #insere_pessoas()
    #alterar_pessoa()
    #consulta()
    #excluir_pessoa()
