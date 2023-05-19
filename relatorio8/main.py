from database import Database
from play_database import PlayDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://52.91.64.0:7687", "neo4j", "significance-operand-incline")
db.drop_all()

# Criando uma instância da classe PlayDatabase para interagir com o banco de dados
play_db = PlayDatabase(db)

# Criando alguns jogadores
play_db.create_player("João")
play_db.create_player("Guilherme")
play_db.create_player("José")

# Criando algumas partidas
play_db.create_match("Match 1")
play_db.create_match("Match 2")
play_db.create_match("Match 3")

# Inserindo pontuação para os jogadores
play_db.create_result("1", "João")
play_db.create_result("3", "Guilherme")
play_db.create_result("2", "José")

# Inserindo jogadores nas partidas
play_db.insert_player_match("João", "Match 1")
play_db.insert_player_match("Guilherme", "Match 1")
play_db.insert_player_match("José", "Match 1")
play_db.insert_player_match("João", "Match 2")
play_db.insert_player_match("Guilherme", "Match 2")
play_db.insert_player_match("José", "Match 2")
play_db.insert_player_match("João", "Match 3")
play_db.insert_player_match("Guilherme", "Match 3")
play_db.insert_player_match("José", "Match 3")

# Atualizando jogador
#play_db.update_player("João", "Pedro")

# Deletando jogador
#play_db.delete_player("José")

# Print de todas as informações do banco de dados
print("Players:")
print(play_db.get_players())
print("Matches:")
print(play_db.get_matches())
print("Results:")
print(play_db.get_results())





