import matplotlib.pyplot as plt
import random


def lin_reg(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = 0
    sum_xx = 0
    for i in range(n):
        sum_xy += x[i] * y[i]
        sum_xx += x[i] * x[i]
    # Calculate K and M with formula given from the assignment
    k = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    m = (sum_xx * sum_y - sum_x * sum_xy) / (n * sum_xx - sum_x * sum_x)
    return m, k


def show_graph(ax, title, xlabel, ylabel, legend):
    ax.set_title(title)  # Set title
    ax.set_xlabel(xlabel)  # Set x label
    ax.set_ylabel(ylabel)  # Set y label
    if legend:  # If legend is given, show legend
        ax.legend()
    plt.show()  # Show graph


def create_graph(labels, sizes, ax, figure, legend_label):
    if ax is None:  # If no axis is given, create a new one
        fig, ax = plt.subplots(figsize=(12, 8))
    labels = list(labels)
    sizes = list(sizes)
    if figure is None:  # If no figure is given, create line graph
        ax.plot(labels, sizes, label=legend_label)
    else:  # Else create graph with points
        ax.plot(labels, sizes, figure, label=legend_label)
    return ax


def random_list(sz, width):
    integers = []
    for i in range(sz):
        integers.append(random.randint(-1*width*sz, width*sz))
    return integers
