# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
# n = int(input('Введите число: '))
# def get_degree(n):
#     return [((-3)**i) for i in range(n)]
# print (get_degree(n))

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# from random import randint
# def get_dict(n):
#     return {x: 3 * x + 1 for x in range(1, n+1)}
# n = randint(6, 6)
# print(n)
# print(get_dict(n))

# def new_dictionary(number):
#     dictionary = {}
#     for i in range(number):
#         values = (3*(i+1)+1)
#         dictionary[f'{i+1}'] = f'{values}'
#     return dictionary

# print("Введите N ")
# N = int(input())
# dictionary = new_dictionary(N)
# print(dictionary)

# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# str_one = input("Введите первую строку ")
# str_two = input("Введите вторую строку ")
# count = str_one.count(str_two)
# if count > 0:
#     print(f"Вторая строка входит {count} раз в первую строку")
# else:
#     print("Вторая строка не входит в первую строку")

#Подсчитать сумму цифр в вещественном числе.
# def DigitToInt(digit):
#     digit = digit.replace(",",".")
#     digit = digit.replace(".","")
#     digit = int(digit) 
#     return digit 
# print("Введите вещественное число ")
# digit = input()
# digit = DigitToInt(digit)
# sum = 0
# while digit!=0:
#     sum = sum + digit%10
#     digit = digit//10
# print(sum)

# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

print("Введите N ")
N = int(input())
count = 1
result = []
for i in range(1,N+1):
   count*=i
   result.append(count)
print(result)

