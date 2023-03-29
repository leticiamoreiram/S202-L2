from database import Database
from model import BookModel

db = Database(database="relatorio5", collection="livros")
db.reset_database()
book_model = BookModel(db)

# criando dois livros
id_livro = book_model.create_book("Moby Dick", "Herman Melville", 1851, 58.8)
id_livro2 = book_model.create_book("1984", "George Orwell", 1949, 20.0)

# lendo um livro pelo ID
livro = book_model.read_book_by_id(id_livro)

# atualizando um livro
book_model.update_book(id_livro, "A Verdade Sobre o Caso Harry Quebert", "Joël Dicker", 2012, 54.0)
livro_atualizado = book_model.read_book_by_id(id_livro)

# excluindo livro
book_model.delete_book(id_livro2)
livro_deletado = book_model.read_book_by_id(id_livro2)