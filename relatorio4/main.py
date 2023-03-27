from save_json import writeAJson
from database import Database

db = Database(database="loja_de_roupas", collection="vendas")
#data = db.collection.find()
db.reset_database()

result = db.collection.aggregate([
    {"$match": {"cliente_id": "B"}},
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": "$produtos.preco"}}},
])

writeAJson(result, "total_gasto")

result2 = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.nome", "total_vendido": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total_vendido": 1}},
    {"$limit": 1}
])

writeAJson(result2, "total_vendido")

result3 = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "menor_gasto": {"$min": "$produtos.preco"}}},
    {"$sort": {"menor_gasto": 1}},
    {"$limit": 1}
])

writeAJson(result3, "menor_gasto")

result3 = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.nome", "quantidade": {"$sum": "$produtos.quantidade"}}},
    {"$match": {"quantidade": {"$gt": 2}}},
    {"$sort": {"quantidade": -1}},
])

writeAJson(result3, "quantidade")