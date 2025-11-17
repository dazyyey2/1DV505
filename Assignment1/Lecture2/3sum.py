import random
import matplotlib
import time


def threesum_brute(lst, sum=0):
    unique_pairs = set()
    for i in range(len(lst)-1):
        v1 = lst[i]
        for z in range(i+1, len(lst)):
            v2 = lst[z]
            for j in range(z+1, len(lst)):
                v3 = lst[j]
                if v1 + v2 + v3 == sum:
                    if v2 < v1:
                        v1, v2 = v2, v1
                    if v1 < v3:
                        v1, v3 = v3, v1
                    if v2 < v3:
                        v2, v3 = v3, v2
                    unique_pairs.add((v1, v2, v3))
    return list(unique_pairs)


def measure_threesum():
    for sz in range(1000, 20001, 1000):
        lst = random_list(15)
        before = time.time


def random_list(n):
    integers = []
    for i in range(0, n):
        integers.append(random.randint(-10*n, 10*n))
    return integers


n = input('List size (default 15): ')
if n == '':
    n = 15
n = int(n)
list1 = random_list(n)
print(f'list1: {list1}')
print(threesum_brute(list1))
list2 = random_list(n)
print(f'\nlist2: {list2}')
print(threesum_brute(list2))
list3 = random_list(n)
print(f'\nlist3: {list3}')
print(threesum_brute(list3))
