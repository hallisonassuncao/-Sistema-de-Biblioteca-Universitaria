from .database import Database

class Autor:
    def __init__(self, nome, nacionalidade, id=None):
        self.id = id
        self.nome = nome
        self.nacionalidade = nacionalidade

    @staticmethod
    def cadastrar(nome, nacionalidade):
        db = Database()
        db.cur.execute("INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s)", (nome, nacionalidade))
        db.commit()
        db.close()

    @staticmethod
    def listar():
        db = Database()
        db.cur.execute("SELECT * FROM autor")
        autores = db.cur.fetchall()
        db.close()
        return autores

    @staticmethod
    def atualizar(id, nome, nacionalidade):
        db = Database()
        db.cur.execute("UPDATE autor SET nome=%s, nacionalidade=%s WHERE id=%s", (nome, nacionalidade, id))
        db.commit()
        db.close()

    @staticmethod
    def excluir(id):
        db = Database()
        db.cur.execute("DELETE FROM autor WHERE id=%s", (id,))
        db.commit()
        db.close()
