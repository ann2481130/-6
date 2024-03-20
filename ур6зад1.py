N = int(input('Введите число:'))
cnt = 1
a = 0
while cnt <= N:
    cnt += 1
    x = int(input('Введите целое число:'))
    if x == 0:
     a += 1
print('Количество нулей:', a)


