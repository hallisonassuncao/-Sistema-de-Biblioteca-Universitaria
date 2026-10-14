from .database import Database

class Livro:
    def __init__(self, titulo, ano_publicacao, autor_id, id=None):
        self.id = id
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.autor_id = autor_id

    @staticmethod
    def cadastrar(titulo, ano_publicacao, autor_id):
        db = Database()
        db.cur.execute("INSERT INTO livro (titulo, ano_publicacao, autor_id) VALUES (%s, %s, %s)", 
                       (titulo, ano_publicacao, autor_id))
        db.commit()
        db.close()

    @staticmethod
    def listar():
        db = Database()
        db.cur.execute("""SELECT livro.id, livro.titulo, livro.ano_publicacao, autor.nome 
                          FROM livro JOIN autor ON livro.autor_id = autor.id""")
        livros = db.cur.fetchall()
        db.close()
        return livros

    @staticmethod
    def atualizar(id, titulo, ano_publicacao, autor_id):
        db = Database()
        db.cur.execute("UPDATE livro SET titulo=%s, ano_publicacao=%s, autor_id=%s WHERE id=%s", 
                       (titulo, ano_publicacao, autor_id, id))
        db.commit()
        db.close()

    @staticmethod
    def excluir(id):
        db = Database()
        db.cur.execute("DELETE FROM livro WHERE id=%s", (id,))
        db.commit()
        db.close()
