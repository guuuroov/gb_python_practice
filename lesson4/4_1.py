#Задача 22: Даны два неупорядоченных набора целых чисел 
#(может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, 
#которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. 
#n — кол-во элементов первого множества. 
#m — кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
user_data = set(input('Введите элементы множества(целые числа): ').split())

user_set1 = {user_data for user_data in range(n)}
user_set2 = {user_data for user_data in range(m)}
print(user_set1)
print(user_set2)

set_intersection = user_set1.intersection(user_set2)
print(f'Элементы, встречающиеся в обоих множествах:{set_intersection} ')

