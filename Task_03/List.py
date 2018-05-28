# List practice
print("List practice")
list_1 = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
list_2 = [list_1[0], list_1[2], list_1[4]]
list_3 = ['1a', '2a', '3a', '4a']
print(list_3.pop(1))
print(list_3)

list_4 = list_3[::]
list_4.insert(1, '2a')
print(list_4)
