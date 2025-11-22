import math
import sort_algorithms as algo
import time
import sys
sys.path.append("./Utils/")
# Comments on below line are to remove error from linters
import utils  # type: ignore # noqa: E402

# Change recursion limit to prevent crash when measuring
# slow quick sort algorithm
sys.setrecursionlimit(20000)


def measure_algorithm(algorithm, runs, start, size, increment,
                      sorted_lists=False, reverse=False):
    sum_of_times = {}
    track = {}
    for i in range(runs):
        if sorted_lists is False:  # If we use random list
            track.clear()  # Clear time tracking data
            print(f'======= Run {i + 1} {algorithm.__name__} =======')
            for sz in range(start, size, increment):
                # Generate list of random values of size sz
                lst = utils.random_list(sz, 10)
                before = time.time()  # Save time before operation
                # Choose algorithm to use in operation
                algorithm(lst)
                # Calculate time elapsed since before operation
                elapsed = time.time() - before
                track[sz] = elapsed  # Save time and size of list
                print(f'{sz} : {round(track[sz], 3)}')
            # Save sum of times to later calculate averages
            for j in track:
                if j in sum_of_times:
                    sum_of_times[j] += track[j]
                else:
                    sum_of_times[j] = track[j]
        else:  # If we use sorted list
            track.clear()  # Clear time tracking data
            print(f'======= Run {i + 1} {algorithm.__name__} =======')
            for sz in range(start, size, increment):
                lst = list(range(sz))
                if reverse:
                    lst = lst[::-1]
                before = time.time()  # Save time before operation
                # Choose algorithm to use in operation
                algorithm(lst)
                # Calculate time elapsed since before operation
                elapsed = time.time() - before
                track[sz] = elapsed  # Save time and size of list
                print(f'{sz} : {round(track[sz], 3)}')
            # Save sum of times to later calculate averages
            for j in track:
                if j in sum_of_times:
                    sum_of_times[j] += track[j]
                else:
                    sum_of_times[j] = track[j]
    # Calculate averages for run graph
    averages = {}
    for value in sum_of_times.keys():
        averages[value] = sum_of_times[value] / runs
    # Calculate log-log graph
    log_x = [math.log(x) for x in averages.keys()]
    log_y = [math.log(y) for y in averages.values()]
    m, k = utils.lin_reg(log_x, log_y)
    line_y = [m + k * x for x in log_x]
    log_data = {}
    log_data['logX'] = log_x
    log_data['lineY'] = line_y
    if sorted_lists:
        log_data['k'] = k
    return averages, log_data


def runs_graph(run_data=None, log_data=None, algo_name=None,
               ax=None, fig_counter=0):
    figures = ['bo', 'g*', 'r+', 'ro', 'b*', 'g+']
    # If we have used all figures, go to beginning
    if fig_counter == len(figures):
        fig_counter = 0
    figure = figures[fig_counter]
    fig_counter += 1  # Increment to use different figure next time
    ax = utils.create_graph(
        run_data.keys(),
        run_data.values(),
        ax=ax,
        figure=figure,
        legend_label=f'Averages for {algo_name}'
    )
    return ax, fig_counter


def log_graph(log_data, algo_name=None, ax=None, fig_counter=0, large=False):
    log_x = log_data["logX"]
    line_y = log_data["lineY"]
    figures = ['bo', 'g*', 'r+', 'ro', 'b*', 'g+']
    # If we have used all figures, go to beginning
    if fig_counter == len(figures):
        fig_counter = 0
    figure = figures[fig_counter]
    fig_counter += 1  # Increment to use different figure next time
    ax = utils.create_graph(
        log_x,
        line_y,
        ax=ax,
        figure=figure,
        legend_label=f'Log data for {algo_name}',
        large=large
    )
    return ax, fig_counter


# Save fuctions in lists
n2_algs = [algo.selection_sort, algo.bubble_sort, algo.insertion_sort]
n_log_n_algs = [algo.merge_sort, algo.quick_sort_slow]
quick_sort_variations = [algo.quick_sort_median, algo.quick_sort_slow]
algo_run_data = {}  # Save run data from tests
algo_log_data = {}  # Save log data
fig_counter = 0  # Used to cycle between markers for points in graphs
ax = None
log_ax = None
runs = 3  # Number of runs per test
# Print menu
print('1. Evaluate O(n²) algorithms')
print('2. Evaluate O(n*log(n)) algorithms')
print('3. Compare quick sort algorithms\n')
user_input = input('Please enter choice: ')
print()
# Match against user choice
match user_input:
    case '1':  # O(n²) evaluation
        list_size_from = 2000  # Starting list size
        list_size_to = 10001  # Ending list size
        # O(n²) algorithms testing
        for alg in n2_algs:
            # Get rid of the underscores in function names
            algo_name = alg.__name__.replace('_', ' ')
            # Get data from tests
            run_data, log_data = measure_algorithm(alg, runs, list_size_from,
                                                   list_size_to, 500)
            # Save data
            algo_run_data[algo_name] = run_data
            algo_log_data[algo_name] = log_data
        # Create and show graph with data from measurements
        for name, run_data in algo_run_data.items():
            ax, fig_counter = runs_graph(run_data=run_data, algo_name=name,
                                         ax=ax, fig_counter=fig_counter)
        utils.show_graph(ax, 'Comparison of O(n^2) sorting algorithms',
                         f'List sizes in range {list_size_from}'
                         f' to {list_size_to}',
                         f'Average time of {runs} runs with random lists',
                         True)
        # Create and show log graph with data from measurements
        for name, log_data in algo_log_data.items():
            log_ax, fig_counter = log_graph(log_data, algo_name=name,
                                            ax=log_ax, fig_counter=fig_counter)
        utils.show_graph(log_ax, 'Log-log data for O(n^2) sorting algorithms',
                         'Log2 of sorting times',
                         'Log2 of list sizes',
                         True)
    case '2':  # O(nlog(n)) evaluation
        list_size_from = 10000  # Starting list size
        list_size_to = 150000  # Ending list size
        # O(nlog(n)) algorithms testing
        for alg in n_log_n_algs:
            # Get rid of the underscores in function names
            algo_name = alg.__name__.replace('_', ' ')
            # Get data from tests
            run_data, log_data = measure_algorithm(alg, runs, list_size_from,
                                                   list_size_to, 10000)
            # Save data
            algo_run_data[algo_name] = run_data
            algo_log_data[algo_name] = log_data
        # Create and show graph with data from measurement
        for name, run_data in algo_run_data.items():
            ax, fig_counter = runs_graph(run_data=run_data, algo_name=name,
                                         ax=ax, fig_counter=fig_counter)
        utils.show_graph(ax, 'Comparison of O(n*log(n)) sorting algorithms',
                         f'List sizes in range {list_size_from}'
                         f' to {list_size_to}',
                         f'Average time of {runs} runs with random lists',
                         True)
        # Create and show log graph with data from measurements
        for name, log_data in algo_log_data.items():
            log_ax, fig_counter = log_graph(log_data, algo_name=name,
                                            ax=log_ax, fig_counter=fig_counter)
        utils.show_graph(log_ax, 'Log-log data for O(n*log(n))'
                         'sorting algorithms',
                         'Log2 of sorting times',
                         'Log2 of list sizes',
                         True)
    case '3':
        list_size_from = 10000  # Starting list size
        list_size_to = 150000  # Ending list size
        # Quick sort testing
        for alg in quick_sort_variations:
            # Get rid of the underscores in function names
            algo_name = alg.__name__.replace('_', ' ')
            # Get data from tests
            run_data, log_data = measure_algorithm(alg, runs, list_size_from,
                                                   list_size_to, 10000)
            # Save data
            algo_run_data[algo_name] = run_data
            algo_log_data[algo_name] = log_data
        # Create and show graph with data from measurement
        for name, run_data in algo_run_data.items():
            ax, fig_counter = runs_graph(run_data=run_data, algo_name=name,
                                         ax=ax, fig_counter=fig_counter)
        utils.show_graph(ax, 'Comparison of quick sort algorithms'
                         '\n[Using random lists]',
                         f'List sizes in range {list_size_from}'
                         f' to {list_size_to}',
                         f'Average time of {runs} runs with random lists',
                         True)
        # Create and show log graph with data from measurement
        for name, log_data in algo_log_data.items():
            log_ax, fig_counter = log_graph(log_data, algo_name=name,
                                            ax=log_ax, fig_counter=fig_counter)
        utils.show_graph(log_ax, 'Log-log data for quick sort algorithms\n'
                         '[Using random lists]',
                         'Log2 of sorting times',
                         'Log2 of list sizes',
                         True)
        print('===== Using sorted list from 1000 to 10000 =====')
        ax = None  # Reset axes
        log_ax = None  # Reset log axes
        fig_counter = 0  # Reset figure counter
        sorted_log_data = {}  # Dict for saving log graph data
        sorted_run_data = {}  # Dict for saving run graph data
        reverse_run_data = {}  # Dict for saving run data from reversed list
        reverse_log_data = {}  # Dict for saving log data from reversed list
        # Quick sort testing with sorted lists
        for alg in quick_sort_variations:
            # Get rid of the underscores in function names
            algo_name = alg.__name__.replace('_', ' ')
            # Get data from tests with sorted list
            run_data, log_data = measure_algorithm(alg, runs, 1000,
                                                   10001, 1000,
                                                   sorted_lists=True)
            # Save data
            sorted_run_data[algo_name] = run_data
            sorted_log_data[algo_name] = log_data
        # Create graph with data from measurement (don't show it yet)
        for name, run_data in sorted_run_data.items():
            ax, fig_counter = runs_graph(run_data=run_data, algo_name=name,
                                         ax=ax, fig_counter=fig_counter)
        print('===== Using reverse sorted list from 1000 to 10000 =====')
        # Quick sort testing with reverse sorted lists
        for alg in quick_sort_variations:
            # Get rid of the underscores in function names
            algo_name = alg.__name__.replace('_', ' ')
            # Get data from tests with reverse sorted list
            run_data, log_data = measure_algorithm(alg, runs, 1000,
                                                   10001, 1000,
                                                   sorted_lists=True,
                                                   reverse=True)
            # Save data
            reverse_run_data[algo_name] = run_data
            reverse_log_data[algo_name] = log_data
        # Add data to graph that was previously created and show the graph
        for name, run_data in reverse_run_data.items():
            ax, fig_counter = runs_graph(run_data=run_data,
                                         algo_name=name+' [Reverse sorting]',
                                         ax=ax, fig_counter=fig_counter)
        utils.show_graph(ax, 'Comparison of quick sort algorithms'
                         '\n[Using sorted lists]',
                         f'List sizes in range {1000}'
                         f' to {10000}',
                         f'Average time of {runs} runs with sorted lists',
                         True)
        ax = None  # Reset axis
        # Variables for saving k-value from tests
        qs_slow_sorted_k = 0
        qs_slow_r_sorted_k = 0
        sorted_k = 0
        r_sorted_k = 0
        # Create log graph without showing it yet
        for name, log_data in sorted_log_data.items():
            log_ax, fig_counter = log_graph(log_data, algo_name=name,
                                            ax=log_ax, fig_counter=fig_counter,
                                            large=True)
            # Save k-value in variable
            if name == 'quick sort slow':
                qs_slow_sorted_k = log_data['k']
            elif name == 'quick sort median':
                sorted_k = log_data['k']
        # Add data to previously created log graph and show it
        for name, log_data in reverse_log_data.items():
            log_ax, fig_counter = log_graph(log_data,
                                            algo_name=name+'[Reverse sorting]',
                                            ax=log_ax, fig_counter=fig_counter,
                                            large=True)
            # Save the k-values
            if name == 'quick sort slow':
                qs_slow_r_sorted_k = log_data['k']
            elif name == 'quick sort median':
                r_sorted_k = log_data['k']
        utils.show_graph(log_ax, 'Log-log data for quick sort algorithms\n'
                         '[Using sorted lists]\n'
                         f'QS slow k-value: {qs_slow_sorted_k}\n'
                         f'QS slow [Reversed] k-value: {qs_slow_r_sorted_k}\n'
                         f'QS median k-value: {sorted_k} \n'
                         f'QS median [Reversed] k-value: {r_sorted_k}\n',
                         'Log2 of reverse sorting times',
                         'Log2 of list sizes',
                         True)
