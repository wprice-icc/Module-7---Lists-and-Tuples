def test_last_three():
    assert last_three([5, 6, 7, 8, 9]) == [7, 8, 9]


def test_add_tuples():
    assert add_tuples((1, 2, 3), (4, 5, 6)) == (5, 7, 9)


def test_nth_elements():
    assert nth_elements([0, 1, 2, 3, 4, 5], 3) == [2, 5]


 def test_populate_and_pop():
    assert populate_and_pop(2, 6) == [2, 3, 4, 5]



def test_shallow_copy():
    lst1 = [1, 2, [3, 4]]
    lst2 = shallow_copy(lst1)
    lst2[2][0] = 9
    assert lst1[2][0] == 9



def test_filter_evens():
    assert filter_evens([1, 4, 5, 8, 11, 15, 18]) == [4, 8, 18]



def test_matrix_sum():
    assert matrix_sum([[1, 2], [3, 4], [5, 6]]) == 21



def test_to_tuple():
    assert to_tuple([1, 2, 3, 4]) == (1, 2, 3, 4)
