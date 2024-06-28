test_dic = {"a":123, "b":True, "c": "koushik"}
test = test_dic
print(test)
print(test_dic.keys())
print(len(test_dic))
test_dic.update({"A": "Koushik"})
print(test_dic)

# indexing 
print(test_dic['a'])
print(test_dic.get('a'))

# set
my_set = {1,2,3,4,5,6,7,8,88,8888}
my_list =list(my_set)
print(my_list[2])


# comparsion operator
set1 = {1,2,3,4,5}
set2 = {1,2,11,22,3334,4444}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1&set2)
print(set1.difference(set2))
print(set1 - set2)

# exersise
test_list = [22,3,34,455,665,3,3,563,545,5435,5345,54,353,553,545,3454,3]
k = len(test_list)
print(k)
x = len(set(test_list))
print(x)








"""k = (list(test_dic))
print(tuple(test_dic))
print(str(test_dic))"""

