import random
import matplotlib.pyplot as plt


def threesum_brute(lst, sum=0):
    unique_triples = set()
    for i in range(len(lst)-1):
        v1 = lst[i]
        for z in range(i+1, len(lst)):
            v2 = lst[z]
            for j in range(z+1, len(lst)):
                v3 = lst[j]
                if v1 + v2 + v3 == sum:
                    # Sort tuple before adding to set
                    triple = tuple(sorted((v1, v2, v3)))
                    unique_triples.add(triple)
    return list(unique_triples)


def threesum_pointers(lst, target=0):
    lst = sorted(lst)  # Sort list in ascending order
    unique_triples = set()
    n = len(lst)
    for i in range(n - 2):
        # Skip if i is the same as last i
        if i > 0 and lst[i] == lst[i - 1]:
            continue
        # Front pointer start at i + 1
        # Back pointer start at end of list
        fp, bp = i + 1, n - 1
        while fp < bp:
            # lst[i] is fixed until the whole list has been compared
            current_sum = lst[i] + lst[fp] + lst[bp]
            if current_sum == target:  # If match
                unique_triples.add((lst[i], lst[fp], lst[bp]))
                fp += 1  # Increment front pointer
                bp -= 1  # Decrement back pointer
                while fp < bp and lst[fp] == lst[fp - 1]:
                    fp += 1  # Skip duplicates for fp
                while fp < bp and lst[bp] == lst[bp + 1]:
                    bp -= 1  # # Skip duplicates for bp
            elif current_sum < target:
                fp += 1  # If sum too small => move fp
            else:
                bp -= 1  # If sum too big => move bp
    return list(unique_triples)  # Convert set to list


def threesum_caching(lst, target=0):
    lst = sorted(lst)  # Sort list in ascending order
    unique_triplets = set()
    # First value start at first value in lst
    for i in range(len(lst)):
        v1 = lst[i]
        cach = set()
        # Second value start at i+1 to avoid v1
        for j in range(i + 1, len(lst)):
            v2 = lst[j]
            # Calculate what the 3rd number needs to be
            v3 = target - v1 - v2
            if v3 in cach:  # If v3 has been seen
                # Sort tuple before adding to set
                triplet = tuple(sorted((v1, v2, v3)))
                unique_triplets.add(triplet)
            cach.add(v2)  # Add v2 to cach and increment
    return list(unique_triplets)  # Covert set to list


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
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if legend:
        ax.legend()
    plt.show()


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
