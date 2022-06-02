# Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие 
# максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

# nums = [1, 5, 2, 3, 4, 6, 1, 7]
# def get_up(nums):
#     ups = [nums[0]]
#     for i in nums:
#         if i > max(ups):
#             ups.append(i)
#     return ups
# print(get_up(nums))

# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого
# файла по возрастанию.

# from random import randint
# path = 'fille.txt'
# max_val = 100
# quantity = 10
# f = open(path, 'w')
# for i in range(quantity):
#     f.write(f'{str(randint(0, max_val))},')
# f.close()
# with open(path, 'r') as fr:
#     list_int = fr.readline().split(',')
#     list_int.pop()
#     list_int.sort(key=(int))
# print(list_int)

# 3. Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа,
# которые в сумме дают 0. (решение будет долгим, ибо является демонстрационным при теме
# многопоточного программирования).

data = '1Kints.txt'
with open(data, 'r') as fr:
    inp_list = fr.readlines()
    inp_list.pop()
    list_val = list(map(int, inp_list))
count = 0
for vali in list_val:
    for valj in list_val:
        for valk in list_val:
            if(vali + valj + valk == 0):
                print(f'{vali} + {valj} + {valk} = 0')
                count += 1
print()
