lst = list(input('Введите числовой ряд через пробел: ').split())
print(lst)
maximum = int(lst[0])
for i in lst:
    i = float(i)
    if maximum < i:
        maximum = i
print(f'максимальное число - {round(maximum)}')
 
