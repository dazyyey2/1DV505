import math
import threesum as algo
import time


def measure_threesum(algorithm, start, size, increment, compare=False):
    sum_of_times = {}
    track = {}
    ax = None
    for i in range(0, 3):  # Run 3 times
        track.clear()
        print(f'======= RUN {i+1} =======')
        for sz in range(start, size, increment):
            lst = algo.random_list(sz, 10)
            before = time.time()
            if algorithm == 'brute':
                algo.threesum_brute(lst)
            elif algorithm == 'pointers':
                algo.threesum_pointers(lst)
            elif algorithm == 'caching':
                algo.threesum_caching(lst)
            elapsed = time.time() - before
            track[sz] = elapsed
            print(f'{sz} : {round(track[sz], 3)}')
        if i == 0:
            ax = algo.create_graph(track.keys(), track.values(),
                                   ax=ax, figure='bo', legend_label='Run 1')
        elif i == 1:
            ax = algo.create_graph(track.keys(), track.values(),
                                   ax=ax, figure='g*', legend_label='Run 2')
        elif i == 2:
            ax = algo.create_graph(track.keys(), track.values(),
                                   ax=ax, figure='r+', legend_label='Run 3')
        for j in track:
            if j in sum_of_times:
                sum_of_times[j] += track[j]
            else:
                sum_of_times[j] = track[j]
    # Graph with runs
    algo.show_graph(ax, '3 runs for 3-sum',
                    f'List sizes in range 100 to {size}',
                    'Run times with random lists', True)
    averages = {}
    for value in sum_of_times.keys():
        averages[value] = sum_of_times[value] / 3
    # Averages graph
    line_graph = algo.create_graph(averages.keys(), averages.values(),
                                   None, None, '')
    algo.show_graph(line_graph, 'Average values for 3-sum',
                    f'List sizes in range 100 to {size}',
                    'Run times with random lists', False)
    # Log vs Log graph
    logX = [math.log(x) for x in averages.keys()]
    logY = [math.log(y) for y in averages.values()]
    m, k = algo.lin_reg(logX, logY)
    lineY = [m + k * x for x in logX]
    log_graph = algo.create_graph(logX, lineY, None, None, 'Straight line fit')
    log_graph = algo.create_graph(logX, logY, log_graph, 'r+', 'Log data')
    algo.show_graph(log_graph,
                    f'Log VS Log and a straight line fit with k = {k}',
                    'Logarithm of list sizes', 'Logarithm of run times', True)
    print(f'Estimated time complexity: O(n^{round(k)})')


def compare_algorithms(algorithms):
    sum_of_times = {}
    track = {}
    ax = None
    for i in range(len(algorithms)):
        if algorithms[i] == 'brute':
            start = 250
            size = 951
            increment = 50
        elif algorithms[i] == 'pointers' or algorithms[i] == 'caching':
            start = 1500
            size = 12501
            increment = 1000
        for z in range(0, 3):  # Run 3 times
            track.clear()
            print(f'======= RUN {z+1} =======')
            for sz in range(start, size, increment):
                lst = algo.random_list(sz, 10)
                before = time.time()
                if algorithms[i] == 'brute':
                    algo.threesum_brute(lst)
                elif algorithms[i] == 'pointers':
                    algo.threesum_pointers(lst)
                elif algorithms[i] == 'caching':
                    algo.threesum_caching(lst)
                elapsed = time.time() - before
                track[sz] = elapsed
                print(f'{sz} : {round(track[sz], 3)}')
            if z == 0:
                ax = algo.create_graph(track.keys(), track.values(),
                                       ax=ax, figure='bo',
                                       legend_label='Run 1')
            elif z == 1:
                ax = algo.create_graph(track.keys(), track.values(),
                                       ax=ax, figure='g*',
                                       legend_label='Run 2')
            elif z == 2:
                ax = algo.create_graph(track.keys(), track.values(),
                                       ax=ax, figure='r+',
                                       legend_label='Run 3')
            for j in track:
                if j in sum_of_times:
                    sum_of_times[j] += track[j]
                else:
                    sum_of_times[j] = track[j]
            # Graph with runs
    algo.show_graph(ax, '3 runs for 3-sum',
                    f'List sizes in range 100 to {size}',
                    'Run times with random lists', True)


n = input('List size (default: 15): ')
if n == '':
    n = 15
n = int(n)
list1 = algo.random_list(n, 10)
print(f'list1: {list1}')
print(f'Using Brute: {algo.threesum_brute(list1)}')
print(f'Using Pointers: {algo.threesum_pointers(list1)}')
list2 = algo.random_list(n, 10)
print(f'\nlist2: {list2}')
print(f'Using Brute: {algo.threesum_brute(list2)}')
print(f'Using Pointers: {algo.threesum_pointers(list2)}')
list3 = algo.random_list(n, 10)
print(f'\nlist3: {list3}')
print(f'Using Brute: {algo.threesum_brute(list3)}')
print(f'Using Pointers: {algo.threesum_pointers(list3)}\n')
print('\n1. Brute')
print('2. Pointers')
print('3. Caching')
print('4. Compare')
user_input = input('Please select algorithm: ')
match user_input:
    case '1':
        measure_threesum('brute', 250, 951, 50)
    case '2':
        measure_threesum('pointers', 1500, 12501, 1000)
    case '3':
        measure_threesum('caching', 1500, 12501, 1000)
    case '4':
        measure_threesum('pointers', 1500, 12501, 1000, compare=True)
        measure_threesum('caching', 1500, 12501, 1000, compare=True)
        # compare_algorithms(['brute', 'pointers', 'caching'])
