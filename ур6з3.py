A = int(input('Введите число A:'))
B = int(input('Введите число B (B>=A):'))
print('Все чётные числа между числами A и B:')
for i in range (A, B+1):
    if i % 2 == 0:
       print(i, end=' ')