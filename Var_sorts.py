import random

# В данном задании рассмотрим разные варианты сортировок используя псевдокод для сортировок

#1 Сортировка "bubble"

#Исходный список для сортировки
A = [random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
     random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]
print("Исходный список имеет следующий вид:", A)
#создаем новый список (В), который будет отсортированным вариантом первого (А) списка
B = A.copy()
for i in range(0, len(B)):
    for j in range(0, len(B)-1-i):
        if B[j] > B[j+1]:
            a = B[j]
            B[j] = B[j+1]
            B[j+1] = a
print("Используя сортировку 'bubble', получаем следующий список: ", B)

#2 Сортировка "insert"

#создаем новый список (С), который будет отсортированным вариантом первого (А) списка
C = A.copy()
for i in range(0, len(C)):
    b = C[i]
    j = i-1
    while j >= 0 and b < C[j]:
        C[j+1] = C[j]
        j -= 1
    C[j+1] = b
print("Используя сортировку 'insert', получаем следующий список: ", C)

#3 Сортировка "shaker"

#создаем новый список (D), который будет отсортированным вариантом первого (А) списка
D = A.copy()
k = 0             #крайнее левое значение
m = len(D) - 1    #крайнее правое значение
while k <= m:
    for i in range(k, m, 1):              #проход в прямом направлении
        if D[i] > D[i+1]:
            D[i], D[i+1] = D[i+1], D[i]
    m -= 1

    for i in range(m, k, -1):             #проход в обратном направлении
        if D[i-1] > D[i]:
            D[i], D[i-1] = D[i-1], D[i]
print("Используя сортировку 'shaker', получаем следующий список: ", D)

#4 Сортировка "select"

#создаем новый список (E), который будет отсортированным вариантом первого (А) списка
E = A.copy()
i = 0
while i < len(E)-1:
    l = i
    j = i + 1
    while j < len(E):
        if E[j] < E[l]:
            l = j
        j += 1
    E[i], E[l] = E[l], E[i]
    i += 1
print("Используя сортировку 'select', получаем следующий список: ", E)