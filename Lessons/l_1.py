
a=int(input("Введите число"))
b = int(input("Введите число"))
if a>b:
    print(a)
elif a==b:
    print(r" {a} = \n {b}")
else:
    print(b)

# №1 За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

n = int(input("Введите кол-во км пройденных за день: "))
m = int(input("Введите длину маршрута в км: "))
print((m+n-1)//n)

# №3 В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

n = int(input("Введите количество парт для класса А: "))
m = int(input("Введите количество парт для класса В: "))
c = int(input("Введите количество парт для класса С: "))
print((n+1)//2 + (m+1)//2 + (c+1)//2)



# №5 Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
#                       нумеруются от «головы» поезда, а иногда – с
#                       «хвоста»
#                       это зависит от того, в какую сторону едет
#                       электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

i = int(input())
j = int(input())
if(i == j ):
    print("Мало условий =( ")
else:
    print(i+j-1," - количество вагонов в электричке")


# №7 Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

y = int(input("Find year"))
if y%4 == 0 and y%100!=0 or y%400==0:
    print("yes")
else:
    print("no")

# Дополнительная задача: 
# напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
print(round(((x2-x1)**2+(y2-y1)**2)**0.5, 2))

# Дополнительная 2:
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

a = float(input("Введите число: "))
print(int(n * 10)%10)

