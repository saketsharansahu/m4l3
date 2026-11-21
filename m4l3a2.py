test_dic = {
    "dog": 4,
    "cat": 4,
    "eagle":2,
    "lion":4,

    }

k = 4
counter = 0
for i in test_dic:
    if test_dic[i] == k:
        counter = counter + 1
print(counter)
