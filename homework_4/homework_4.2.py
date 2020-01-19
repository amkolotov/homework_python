# вывести элементы исходного списка, значения которых больше предыдущего элемента

my_list = [5, 2, 65, 34, 4, 78, 24, 86, 6, 45, 90]

res_list = [n for n in my_list if n > my_list[my_list.index(n) - 1]]

print(res_list)