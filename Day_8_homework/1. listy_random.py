import random
from collections import Counter

number = [random.randint(1,1000)]
list_1 = []

for i in range(0,1000):
    n = random.randint(1, 1000)
    list_1.append(n)
    print(list_1)

list_2 = []

for i in range(0,1000):
    n = random.randint(1, 1000)
    list_2.append(n)
    print(list_2)

for element in list_1:
    if any(element in list_1 for element in list_2):
        print(element)

list_3 = (set(list_1) - set(list_2))
print(list_3)

list_4 = (set(list_2) - set(list_1))
print(list_4)

list_1_counted = Counter(list_1).most_common(3)
print(list_1_counted)

list_2_counted = Counter(list_2).most_common(3)
print(list_2_counted)


list_1_sorted = sorted(list_1)
print(list_1_sorted)

list_2_sorted = sorted(list_2)
print(list_2_sorted)





