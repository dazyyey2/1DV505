import sys
sys.path.append("./Utils/")
import utils  # type: ignore # noqa: E402


# Test with random list of size 50 with width -50000 to 50000
def random_list_test(algorithm):
    unsorted_lst = utils.random_list(50, 1000)
    sorted_lst = algorithm(unsorted_lst)
    expected = sorted(unsorted_lst)
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'


# Test with different edge cases
def edge_case_test(algorithm):
    unsorted_lst = []
    sorted_lst = algorithm(unsorted_lst)
    expected = []
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'
    unsorted_lst = [10]
    sorted_lst = algorithm(unsorted_lst)
    expected = [10]
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'
    unsorted_lst = [10, -10]
    sorted_lst = algorithm(unsorted_lst)
    expected = [-10, 10]
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'
    unsorted_lst = [-10, -10]
    sorted_lst = algorithm(unsorted_lst)
    expected = [-10, -10]
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'
    unsorted_lst = [0]
    sorted_lst = algorithm(unsorted_lst)
    expected = [0]
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'
    unsorted_lst = [0, -1]
    sorted_lst = algorithm(unsorted_lst)
    expected = [-1, 0]
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'
    unsorted_lst = ['c', 'b', 'a']
    sorted_lst = algorithm(unsorted_lst)
    expected = ['a', 'b', 'c']
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'
