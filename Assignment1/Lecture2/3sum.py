import random
import matplotlib.pyplot as plt
import time
import math


def threesum_brute(lst, target=0):
    unique_triples = set()
    for i in range(len(lst)-1):
        v1 = lst[i]
        for z in range(i+1, len(lst)):
            v2 = lst[z]
            for j in range(z+1, len(lst)):
                v3 = lst[j]
                if v1 + v2 + v3 == target:
                    triple = tuple(sorted((v1, v2, v3)))  # Sort before
                    unique_triples.add(triple)
    return list(unique_triples)


def measure_threesum():
    sum_of_times = {}
    track = {}
    ax = None
    for i in range(0, 3):  # Run 3 times
        track.clear()
        print(f'======= RUN {i+1} =======')
        for sz in range(100, 801, 50):
            lst = random_list(sz, 10)
            before = time.time()
            threesum_brute(lst)
            elapsed = time.time() - before
            track[sz] = round(elapsed, 3)
            print(f'{sz} : {track[sz]}')
        if i == 0:
            ax = create_graph(track.keys(), track.values(),
                              ax=ax, figure='bo', legend_label='Run 1')
        elif i == 1:
            ax = create_graph(track.keys(), track.values(),
                              ax=ax, figure='g*', legend_label='Run 2')
        elif i == 2:
            ax = create_graph(track.keys(), track.values(),
                              ax=ax, figure='r+', legend_label='Run 3')
        for j in track:
            if j in sum_of_times:
                sum_of_times[j] += track[j]
            else:
                sum_of_times[j] = track[j]
    # Graph with runs
    show_graph(ax, '3 runs for 3-sum', 'List sizes in range 100 to 800',
               'Run times with random lists', True)
    averages = {}
    for value in sum_of_times.keys():
        averages[value] = sum_of_times[value] / 3
    # Averages graph
    line_graph = create_graph(averages.keys(), averages.values(),
                              None, None, '')
    show_graph(line_graph, 'Average values for 3-sum',
               'List sizes in range 100 to 800',
               'Run times with random lists', False)
    # Log vs Log graph
    logX = [math.log(x) for x in averages.keys()]
    logY = [math.log(y) for y in averages.values()]
    m, k = lin_reg(logX, logY)
    lineY = [m + k * x for x in logX]
    log_graph = create_graph(logX, lineY, None, None, 'Straight line fit')
    log_graph = create_graph(logX, logY, log_graph, 'r+', 'Log data')
    show_graph(log_graph, f'Log VS Log and a straight line fit with k = {k}',
               'Logarithm of list sizes', 'Logarithm of run times', True)
    print(f'Estimated time complexity: O(n^{round(k)})')


def lin_reg(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = 0
    sum_xx = 0
    for i in range(n):
        sum_xy += x[i] * y[i]
        sum_xx += x[i] * x[i]
    k = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    m = (sum_xx * sum_y - sum_x * sum_xy) / (n * sum_xx - sum_x * sum_x)
    return m, k


def show_graph(ax, title, xlabel, ylabel, legend):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if legend:
        ax.legend()
    plt.show()


def create_graph(labels, sizes, ax, figure, legend_label):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    labels = list(labels)
    sizes = list(sizes)
    if figure is None:
        ax.plot(labels, sizes, label=legend_label)
    else:
        ax.plot(labels, sizes, figure, label=legend_label)
    return ax


def random_list(sz, width):
    integers = []
    for i in range(sz):
        integers.append(random.randint(-1*width*sz, width*sz))
    return integers


n = input('List size (default: 15): ')
if n == '':
    n = 15
n = int(n)
list1 = random_list(n, 10)
print(f'list1: {list1}')
print(threesum_brute(list1))
list2 = random_list(n, 10)
print(f'\nlist2: {list2}')
print(threesum_brute(list2))
list3 = random_list(n, 10)
print(f'\nlist3: {list3}')
print(threesum_brute(list3))

measure_threesum()
