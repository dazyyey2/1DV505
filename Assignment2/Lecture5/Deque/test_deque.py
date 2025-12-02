import pytest
from Deque import Deque as dq


def test_adding():
    ll = dq()
    # Test add_first
    for i in range(1, 11):
        ll.add_first(i)
    expected = '{ 10 9 8 7 6 5 4 3 2 1 }'
    assert str(ll) == str(expected), f'Exp: {str(expected)}, Got: {
        f'{str(ll)}'}'
    # Size check
    size = ll.size
    expected = 10
    assert size == expected, f'Exp: {str(expected)}, Got: {
        f'{str(size)}'}'
    # Test add_last on same list
    for i in range(1, 11):
        ll.add_last(i)
    expected = '{ 10 9 8 7 6 5 4 3 2 1 1 2 3 4 5 6 7 8 9 10 }'
    assert str(ll) == str(expected), f'Exp: {str(expected)}, Got: {
        f'{str(ll)}'}'
    # Size check
    size = ll.size
    expected = 20
    assert size == expected, f'Exp: {str(expected)}, Got: {
        f'{str(size)}'}'


@pytest.fixture
def populated_list():
    ll = dq()
    ll.add_last('Jonas')
    ll.add_last('Erik')
    ll.add_last('Herbert')
    ll.add_last('Johanna')
    return ll


def test_get(populated_list):
    ll = populated_list
    # Test get_first()
    expected = 'Jonas'
    assert ll.get_first() == expected, f'Exp: {str(expected)}, Got: {
        f'{str(ll.get_first())}'}'
    # Test get_last()
    expected = 'Johanna'
    assert ll.get_last() == expected, f'Exp: {str(expected)}, Got: {
        f'{str(ll.get_last())}'}'


def test_removing(populated_list):
    ll = populated_list
    # Test remove_first() return
    first = ll.remove_first()
    expected = 'Jonas'
    assert first == expected, f'Exp: {str(expected)}, Got: {
        f'{str(first)}'}'
    # Test remove_first() actually removed the first element
    ll_str = str(ll)
    expected = '{ Erik Herbert Johanna }'
    assert ll_str == expected, f'Exp: {str(expected)}, Got: {
        f'{str(ll_str)}'}'
    # Test remove_last() return
    last = ll.remove_last()
    expected = 'Johanna'
    assert last == expected, f'Exp: {str(expected)}, Got: {
        f'{str(last)}'}'
    # Test remove_last() actually removed the last element
    ll_str = str(ll)
    expected = '{ Erik Herbert }'
    assert ll_str == expected, f'Exp: {str(expected)}, Got: {
        f'{str(ll_str)}'}'
    # Size check
    size = ll.size
    expected = 2
    assert size == expected, f'Exp: {str(expected)}, Got: {
        f'{str(size)}'}'
    # is_empty() check
    result = ll.is_empty()
    expected = False
    assert result == expected, f'Exp: {str(expected)}, Got: {
        f'{str(result)}'}'
    #  Remove all remaining nodes
    for _ in ll:
        ll.remove_first()
    # is_empty() check again
    result = ll.is_empty()
    expected = True
    assert result == expected, f'Exp: {str(expected)}, Got: {
        f'{str(result)}'}'
    # Size check
    size = ll.size
    expected = 0
    assert size == expected, f'Exp: {str(expected)}, Got: {
        f'{str(size)}'}'


def test_iteration(populated_list):
    ll = populated_list
    result = []
    # Test iteration
    for data in ll:
        result.append(data)
    expected = ['Jonas', 'Erik', 'Herbert', 'Johanna']
    assert result == expected, f'Exp: {str(expected)}, Got: {
        f'{str(result)}'}'
