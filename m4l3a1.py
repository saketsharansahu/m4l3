dic = {
    1:{"name":"saket", "age": 12 }, 
    2:{"name": "tanjim", "age": 12},
    3:{"name" : "saket", "age":12}
    }
print(dic[2])
print(dic.get(1))

print(len(dic))
li =[]
result = {}
for a,b in dic.items():
    unique_items = (b["name"], b["age"])
    if unique_items not in li:
        li.append(unique_items)
        result[a] = b
for a,b in result.items():
    print(a ," " , b)




