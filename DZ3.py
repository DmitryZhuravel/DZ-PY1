# Найти НОК двух чисел
# print('Введите число a = ', end='')
# a = int (input ())
# print ('Введите число b = ', end = '')
# b = int (input ())
# p = a * b
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# print ('НОК=', p // (a+b))

# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.142. 
# k = 1
# c = 0
# for k in range(1, 10000):
#     c = c+4*((-1)**(k+1))/(2*k-1)
# print(f'{c:.3f}')

# Составить список простых множителей натурального числа N
# n = int(input("Введите число N: "))
# i = 1
# while(i <= n):
#     c=0
#     if(n % i == 0):
#         j=1
#         while(j <= i):
#             if(i % j == 0):
#                 c+=1
#             j+=1
#         if (c==2):
#             print(i)
#     i+=1
      
# Дана последовательность чисел. Получить список неповторяющихся 
# элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
# def find_index_num(elem, nums):
#     for i in range(len(nums)):
#         if nums[i] == elem:
#             return i
#     return -1

# def get_unique_lst(nums):
#     unique_lst = []
#     for num in nums:
#         if find_index_num(num, unique_lst) == -1:
#             unique_lst.append(num)
#     return unique_lst

# nums = [int(num) for num in input("Дана последовательность чисел через пробел: ").split()]
# print('Cписок неповторяющихся элементов исходной последовательности: ', get_unique_lst(nums))

#5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

from random import randint
quantity, maxVal = 5, 20 
path = 'file.txt' 
data = open(path, 'w')
for i in range(quantity):
    data.write(f'{str(randint(0, maxVal))}\n')
data.close()
readList = []
with open('file.txt', 'r') as data:
    for i in data:
        if(int(i) % 2 != 0):
            readList.append(int(i))
print('Список нечётных чисел')
print(readList)
