users = [
    { "id": 0, "name": "Jeandra"},
    { "id": 1, "name": "Alex"},
    { "id": 2, "name": "Hugo"},
    { "id": 3, "name": "Jadna"},
    { "id": 4, "name": "Karina"},
    { "id": 5, "name": "Ysa"},
    { "id": 6, "name": "Everton"},
    { "id": 7, "name": "Raquel"},
    { "id": 8, "name": "Vanja"},
    { "id": 9, "name": "Veronica"}
]

# Recebendo dados de amizades 
friendship_pairs = [(0, 1), (0,2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Inicializando (criando) o dict com uma lista vazia para cada id de usuário:
friendships = {user["id"]: [] for user in users} 

# Agora execute um loop pelos pares de amigos para preenchê-las:
for i, j in friendship_pairs:
    friendships[i].append(j) # Adiciona j como amigo do usuário i
    friendships[j].append(i) # Adiciona i como amigo do usuário j
    
#teste    
#teste