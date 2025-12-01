import test_sorting as test
import sys
sys.path.append("./Assignment1/Lecture3/")
import sort_algorithms as algo  # type: ignore # noqa: E402


def test_algorithms(algo_lst):
    success = True
    for alg in algo_lst:
        try:
            test.random_list_test(alg)
            test.edge_case_test(alg)
        except Exception as e:
            print(e)
            success = False
    return success


n2_algs = [algo.selection_sort, algo.bubble_sort, algo.insertion_sort]
n_log_n_algs = [algo.merge_sort, algo.quick_sort_slow]
quick_sort_variations = [algo.quick_sort_median, algo.quick_sort_slow]
all_algos = n2_algs + n_log_n_algs + quick_sort_variations

if test_algorithms(all_algos):
    print('All algorithms passed!')
