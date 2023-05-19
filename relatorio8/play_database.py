class PlayDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, name):
        query = "CREATE (:Match {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_result(self, points, player_name):
        query = "MATCH (p:Player {name: $player_name}) CREATE (:Result {points: $points})<-[:PONTUOU]-(p)"
        parameters = {"points": points, "player_name": player_name}
        self.db.execute_query(query, parameters)

    def insert_player_match(self, player_name, match_name):
        query = "MATCH (a:Player {name: $player_name}) MATCH (b:Match {name: $match_name}) CREATE (a)-[:PARTICIPOU]->(b)"
        parameters = {"player_name": player_name, "match_name": match_name}
        self.db.execute_query(query, parameters)

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_matches(self):
        query = "MATCH (a:Match) RETURN a.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_results(self):
        query = "MATCH (a:Result)<-[:PONTUOU]-(p:Player) RETURN a.points AS points, p.name AS player_name"
        results = self.db.execute_query(query)
        return [(result["points"], result["player_name"]) for result in results]