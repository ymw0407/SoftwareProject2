dict = {"key1" : 1, "key2": 2, "key3": 3}
print(dict["key1"]) # 1

for k in dict.keys(): # ["key1", "key2", "key3"]
    print(k) 
for v in dict.values(): # [1, 2, 3]
    print(v)
for k, v in dict.items(): # [('key1', 1), ('key2', 2), ('key3', 3)]
    print(k, v)