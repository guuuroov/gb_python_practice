#Задача 6: Вы пользуетесь общественным транспортом? 
#Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, где 
#сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.

n = int(input("Введите номер билета: "))

a = n // 100000
b = (n // 10000)%10
c = (n % 10000)//1000
sum1 = (a+b+c)
d = n % 10
e = (n//10)%10
f = (n % 1000)//100
sum2 = (d+e+f)
if sum1 == sum2:
    print('yes')
else:
    print('no')