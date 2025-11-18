import math
import threesum as algo
import time


def measure_threesum(algorithm, start, size, increment, plot=True):
    sum_of_times = {}
    track = {}
    run1 = {}
    run2 = {}
    run3 = {}
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
            for key in track.keys():
                run1[key] = track[key]
            # ax = algo.create_graph(track.keys(), track.values(),
            #                        ax=ax, figure='bo', legend_label='Run 1')
        elif i == 1:
            for key in track.keys():
                run2[key] = track[key]
            # ax = algo.create_graph(track.keys(), track.values(),
            #                        ax=ax, figure='g*', legend_label='Run 2')
        elif i == 2:
            for key in track.keys():
                run3[key] = track[key]
            # ax = algo.create_graph(track.keys(), track.values(),
            #                        ax=ax, figure='r+', legend_label='Run 3')
        # Sum the time of runs in new dict
        for j in track:
            if j in sum_of_times:
                sum_of_times[j] += track[j]
            else:
                sum_of_times[j] = track[j]
    # Divide the sums by the number of runs (3) to get average
    averages = {}
    for value in sum_of_times.keys():
        averages[value] = sum_of_times[value] / 3
    # Calculate log v log graph
    logX = [math.log(x) for x in averages.keys()]
    logY = [math.log(y) for y in averages.values()]
    m, k = algo.lin_reg(logX, logY)
    lineY = [m + k * x for x in logX]
    print(f'Estimated time complexity: O(n^{round(k)})')
    if plot:
        # Create and show graph with runs
        ax = algo.create_graph(run1.keys(), run1.values(),
                               ax=ax, figure='bo', legend_label='Run 1')
        ax = algo.create_graph(run2.keys(), run2.values(),
                               ax=ax, figure='g*', legend_label='Run 2')
        ax = algo.create_graph(run3.keys(), run3.values(),
                               ax=ax, figure='r+', legend_label='Run 3')
        algo.show_graph(ax, '3 runs for 3-sum',
                        f'List sizes in range 100 to {size}',
                        'Run times with random lists', True)
        # Create and show averages graph
        line_graph = algo.create_graph(averages.keys(), averages.values(),
                                       None, None, '')
        algo.show_graph(line_graph, 'Average values for 3-sum',
                        f'List sizes in range 100 to {size}',
                        'Run times with random lists', False)
        # Create and show log graph
        log_graph = algo.create_graph(logX, lineY, None, None,
                                      'Straight line fit')
        log_graph = algo.create_graph(logX, logY, log_graph, 'r+', 'Log data')
        algo.show_graph(log_graph,
                        f'Log vs Log and a straight line fit with k = {k}\n'
                        f'Estimated time complexity: O(n^{round(k)})',
                        'Logarithm of list sizes',
                        'Logarithm of run times', True)
    return run1, run2, run3, logX, logY, lineY, k


n = 15  # List size
list1 = algo.random_list(n, 10)
print(f'list1: {list1}')
print(f'Using Brute: {algo.threesum_brute(list1)}')
print(f'Using Pointers: {algo.threesum_pointers(list1)}')
print(f'Using Caching: {algo.threesum_caching(list1)}')
list2 = algo.random_list(n, 10)
print(f'\nlist2: {list2}')
print(f'Using Brute: {algo.threesum_brute(list2)}')
print(f'Using Pointers: {algo.threesum_pointers(list2)}')
print(f'Using Caching: {algo.threesum_caching(list2)}')
list3 = algo.random_list(n, 10)
print(f'\nlist3: {list3}')
print(f'Using Brute: {algo.threesum_brute(list3)}')
print(f'Using Pointers: {algo.threesum_pointers(list3)}')
print(f'Using Caching: {algo.threesum_caching(list3)}')
print('\n1. Brute')
print('2. Pointers')
print('3. Caching')
print('4. Compare pointer and caching algorithms')
user_input = input('Please make a selection: ')
match user_input:
    case '1':
        measure_threesum('brute', 250, 951, 50)
    case '2':
        measure_threesum('pointers', 1500, 12501, 1000)
    case '3':
        measure_threesum('caching', 1500, 12501, 1000)
    case '4':
        run1_p, run2_p, run3_p, logX_p, logY_p, lineY_p, k_p = (
            measure_threesum('pointers', 1500, 12501, 1000, plot=False)
            )
        run1_c, run2_c, run3_c, logX_c, logY_c, lineY_c, k_c = (
            measure_threesum('caching', 1500, 12501, 1000, plot=False)
            )
        # Create and show comparison run graph
        ax = algo.create_graph(run1_p.keys(), run1_p.values(),
                               ax=None, figure=None, legend_label='Run 1(P)')
        ax = algo.create_graph(run2_p.keys(), run2_p.values(),
                               ax=ax, figure=None, legend_label='Run 2(P)')
        ax = algo.create_graph(run3_p.keys(), run3_p.values(),
                               ax=ax, figure=None, legend_label='Run 3(P)')
        ax = algo.create_graph(run1_c.keys(), run1_c.values(),
                               ax=ax, figure=None, legend_label='Run 1(C)')
        ax = algo.create_graph(run2_c.keys(), run2_c.values(),
                               ax=ax, figure=None, legend_label='Run 2(C)')
        ax = algo.create_graph(run3_c.keys(), run3_c.values(),
                               ax=ax, figure=None, legend_label='Run 3(C)')
        algo.show_graph(ax,
                        'Comparison graph between pointer and caching'
                        ' algorithms\n(P): Pointer\n(C): Caching',
                        f'List sizes in range 100 to {12501}',
                        'Run times with random lists', True)
        # Create and show comparison log graph with k values
        log_graph = algo.create_graph(logX_p, lineY_p, None, None,
                                      'Straight line fit (P)')
        log_graph = algo.create_graph(logX_p, logY_p, log_graph, 'r+',
                                      'Log data (P)')
        log_graph = algo.create_graph(logX_c, lineY_c, log_graph, None,
                                      'Straight line fit (C)')
        log_graph = algo.create_graph(logX_c, logY_c, log_graph, 'g*',
                                      'Log data (C)')
        algo.show_graph(log_graph,
                        'Log vs Log and a straight line fit comparison\n'
                        f'Pointer (P) K value: {k_p}\n'
                        f'Estimated time complexity: O(n^{round(k_p)})\n'
                        f'Cache (C) K value: {k_c}\n'
                        f'Estimated time complexity: O(n^{round(k_c)})',
                        'Logarithm of list sizes',
                        'Logarithm of run times', True)
