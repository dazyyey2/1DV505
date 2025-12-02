import random


# Test with list of size 1000 and width -5k to 5k
def random_list_test(algorithm):
    unsorted_lst = []
    for _ in range(1000):
        unsorted_lst.append(random.randint(-5000, 5000))
    expected = sorted(unsorted_lst)
    sorted_lst = algorithm(unsorted_lst)
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
    unsorted_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sorted_lst = algorithm(unsorted_lst)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'
    unsorted_lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_lst = algorithm(unsorted_lst)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'
    unsorted_lst = [0, 0, 0, 0, 0, 0]
    sorted_lst = algorithm(unsorted_lst)
    expected = [0, 0, 0, 0, 0, 0]
    assert sorted_lst == expected, f'Exp: {str(expected)}, Got: {
        f'{str(sorted_lst)} from {algorithm}'}'
