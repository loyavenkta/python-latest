#### string into list and tuple
test_string = "How are you"
test_list = [1,2,3,4]


'''print(test_string.split())
print(list(test_string))
print(tuple(test_string))

print(str(test_list))
print(' '.join(['ome','two','three']))


### indexing string
print(test_string[0:5])'''




k = str(test_list).strip('[').strip(']').replace(",",'').replace(" ","")
print(k)


