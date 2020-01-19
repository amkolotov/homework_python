# определить элементы списка, не имеющие повторений

int_list = [4, 2, 5, 4, 3, 9, 5, 8]

res_list = [n for n in int_list if int_list.count(n) == 1]

print(res_list)