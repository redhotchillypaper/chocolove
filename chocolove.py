#The first module from Chaka and HighLove
def delnull(A:list,num=0):
    """
    Функция удаляет нули из массива нули
    """
    A = [int(i) for i in A if i != num]
    return A
def soe(a,b):
    """
    Простой алгоритм Решета Эратосфена
    Возвращение диапазона простых чисел от a до b
    """
    list1 = list(range(b + 1))
    list1[1] = 0
    for i in range(2, b + 1):
        if list1[i] != 0:
            for j in range(i * i, b + 1, i):
                list1[j] = 0
        if i < a:
            list1[i] = 0
    return delnull(list1)
def sum_nums(num):
    """
    Возвращает сумму цифр числа
    """
    num = str(num)
    A = [int(i) for i in num]
    sum = 0
    for i in A:
        sum += i
    return sum
def nod(a,b):
    """
    Возвращает НОД числа
    """
    while b != 0:
        a, b = b, a % b
    return a
def nok(a,b):
    """
    Возвращает НОД числа
    """
    x,y=a,b
    while b != 0:
        a, b = b, a % b
    return x*y/a
