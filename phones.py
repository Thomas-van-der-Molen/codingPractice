num = int(input())
phones = {}
for x in range(num):
    name = input()
    name, phone = name.split(" ")[0], name.split(" ")[1]
    phones[name] = phone

query = input()
queries = []
while query:
    queries.append(query)
    query = input()

for query in queries:
    if query in phones: print(f'{query}={phones[query]}')
    else: print("Not found")