#111111
from functools import reduce
from random import randint
def first_task():
    Nums = [int(input()) for _ in range(3)]
    return sum(Nums), reduce(lambda x, y: x*y, Nums), sum(Nums)//3
#222222
def second_task():
    lessons = {1: '9:15', 2: '10:10', 3: '11:05', 4: '12:00', 5: '12:55', 6: '13:50', 7: '14:45'}
    print(lessons.get(int(input())))
#333333
def third_task():
    nums = [randint(1, 6) for _ in range(3)]
    print(nums)
    print(sum(nums)/3)
#444444
def fourth_task():
    num = randint(100, 999)
    print('Получено число:', num)
    num = str(num)
    print('сотни:', num[0])
    print('десятки:', num[1])
    print('единицы:', num[2])
#555555
def fifth_task_1():
    a, b, c, d = map(int, input().split())
    if a > b and a > c and a > d:
        print("наибольшее число", a)
    elif b > a and b > c and c > d:
        print("наибольшее число", b)
    elif c > a and c > b and c > d:
        print("наибольшее число", c)
    else:
        if d > a and d > b and d > c:
            print("наибольшее число", d)

def fifth_task_2():
    nums = [int(input()) for _ in range(4)]
    print(max(nums), min(nums))
#66666
def sixth_task():
    data = input()
    if data[data.rfind('.') + 1:] in ('htm', 'html', 'php'):
        print('Это веб-страница!')
    else:
        print('Что-то другое.')
#77777
def seventh_task():
    nums = [randint(10, 100) for _ in range(10)]
    print(nums)
    print(max(nums))
