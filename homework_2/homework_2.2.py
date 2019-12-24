# обмен значений соседних элементов списка

my_list = []
while True:
    a = input('Введите элемент списка, для выхода нажмите "q": ')
    if a == 'q': break
    my_list.append(a)

new_list = []
for i in range(len(my_list)):
    if i % 2 != 0:
        new_list.append(my_list[i])
        new_list.append(my_list[(i - 1)])
        
if len(my_list) // 2 != 0:
    new_list.append(my_list[-1])

print(my_list)
print(new_list)
