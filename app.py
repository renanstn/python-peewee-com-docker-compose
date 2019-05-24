import peewee

db = peewee.MySQLDatabase('teste', 
    user='root',
    password='admin',
    host='database_peewee',
    port=3306
)

class Autores(peewee.Model):
    nome = peewee.CharField()

    class Meta:
        database = db

class Livros(peewee.Model):
    titulo = peewee.CharField()
    paginas = peewee.IntegerField()
    autor = peewee.ForeignKeyField(Autores)

    class Meta:
        database = db


if __name__ == '__main__':
    #db.connect()
    Autores.create_table()
    Livros.create_table()

    # Inserir um autor na tabela:
    autor_1 = Autores.create(nome="José de Abreu")

    # Inserindo um livro na tabela:
    livro_1 = {
        'titulo' : 'A treta de Konoha',
        'paginas' : 400,
        'autor' : autor_1
    }
    livro_2 = {
        'titulo' : 'Guerra dos mundos',
        'paginas' : 350,
        'autor' : autor_1
    }

    livros = [livro_1, livro_2]

    # Inserindo os livros todos juntos:
    Livros.insert_many(livros).execute()

    # Realizando buscas:
    livro = Livros.get(Livros.titulo=='A treta de Konoha').get()
    print(livro.titulo)

    livros = Livros.select().join(Autores).where(Autores.nome=='José de Abreu')
    for livro in livros:
        print(livro.titulo)