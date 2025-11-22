import math
import sort_algorithms as algo
import time
import sys
sys.path.append("./Utils/")
# Comments on below line are to remove error from linters
import utils  # type: ignore # noqa: E402


def measure_algorithm(algorithm, runs, start, size, increment):
    sum_of_times = {}
    track = {}
    run_data = {}
    log_data = {}

    for i in range(runs):
        track.clear()  # Clear time tracking data
        print(f'======= RUN {i + 1} =======')
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

    averages = {}
    for value in sum_of_times.keys():
        averages[value] = sum_of_times[value] / runs

    run_data[i] = averages.copy()

    # Calculate log-log graph
    log_x = [math.log(x) for x in averages.keys()]
    log_y = [math.log(y) for y in averages.values()]
    m, k = utils.lin_reg(log_x, log_y)
    line_y = [m + k * x for x in log_x]

    log_data['logX'] = log_x
    log_data['logY'] = log_y
    log_data['lineY'] = line_y
    log_data['k'] = k
    print(f'Estimated time complexity: O(n^{round(k)})')

    return run_data, log_data


def runs_graph(run_data=None, log_data=None, algo_name=None,
               ax=None, fig_counter=0):
    figures = ['bo', 'g*', 'r+', 'ro', 'b*', 'g+']
    if fig_counter == len(figures):
        fig_counter = 0
    figure = figures[fig_counter]
    for run_data in run_data.values():
        fig_counter += 1
        ax = utils.create_graph(
            run_data.keys(),
            run_data.values(),
            ax=ax,
            figure=figure,
            legend_label=f'Averages for {algo_name}'
        )
    return ax, fig_counter


def log_graph(log_data, algo_name=None, ax=None, fig_counter=0):
    log_x = log_data["logX"]
    line_y = log_data["lineY"]
    figures = ['bo', 'g*', 'r+', 'ro', 'b*', 'g+']
    if fig_counter == len(figures):
        fig_counter = 0
    figure = figures[fig_counter]
    fig_counter += 1

    ax = utils.create_graph(
        log_x,
        line_y,
        ax=ax,
        figure=figure,
        legend_label=f'Log data for {algo_name}'
    )
    return ax, fig_counter


n2_algs = [algo.selection_sort, algo.bubble_sort, algo.insertion_sort]
ax = None
log_ax = None
fig_counter = 0

for i in range(2):  # 0 for run_data graph, 1 for log_data graph
    for alg in n2_algs:
        algo_name = alg.__name__
        run_data, log_data = measure_algorithm(alg, 2, 2000, 6001, 1000)
        if i == 0:
            ax, fig_counter = runs_graph(run_data=run_data, algo_name=algo_name,
                                         ax=ax, fig_counter=fig_counter)
        if i == 1:
            log_ax, fig_counter = log_graph(log_data, algo_name=algo_name,
                                            ax=log_ax, fig_counter=fig_counter)
    if i == 0:
        utils.show_graph(ax, 'Comparison of O(n^2) Sorting Algorithms',
                         'List Size', 'Time (s)', True)
    if i == 1:
        utils.show_graph(log_ax, 'Comparison of O(n^2) Sorting Algorithms',
                         'List Size', 'Time (s)', True)
