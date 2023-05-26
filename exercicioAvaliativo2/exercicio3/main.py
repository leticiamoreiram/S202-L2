from database import Database
from teacherCRUD import TeacherCRUD

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://18.215.64.141:7687", "neo4j", "speed-carbons-reviews")
db.drop_all()

# Criando uma instância da classe TeacherCRUD para interagir com o banco de dados
teacher_db = TeacherCRUD(db)

# Criando um professor
teacher_db.create_teacher("Chris Lima", 1956, "189.052.396-66")

# Retornando um professor
teacher_db.read_teacher("Chris Lima")

# Atualizando professor
teacher_db.update_teacher("Chris Lima", "123.456.789.11")

# Deletando professor
teacher_db.delete_teacher("Chris Lima")

