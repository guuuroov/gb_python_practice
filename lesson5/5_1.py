# Задача 26:  Напишите программу, которая на вход принимает два числа 
# A и B, 
# и возводит число А в целую степень B с помощью рекурсии.


def recurse(a,b):
    if b == 1:
        return a
    elif b % 2==0:
        res = recurse(a,b // 2)
        return res*res
    else:
        res = recurse(a, b // 2)
        return res * res * a

a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
print(f"Число {a} в степени {b} будет: {recurse(a,b)}")