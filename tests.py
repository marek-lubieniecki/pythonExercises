from exercises import *


def test_bubble_sort():
    a = [99, 32, 5, 3, 6, 7, 54, 87]
    bubble_sort(a)
    assert a == [3, 5, 6, 7, 32, 54, 87, 99]


def test_star_triangle():
    a = 9
    star_triangle(a)
    assert 1 == 1


def test_fibonacci():
    a = fibonacci_series(5)
    b = fibonacci_series(2)
    c = fibonacci_series(1)
    assert a == [0, 1, 1, 2, 3]
    assert b == [0, 1]
    assert c == [0]


def test_triangle_check():
    assert triangle_check(1, 1, 1)
    assert triangle_check(1, 5, 5)
    assert not triangle_check(1, 1, 5)
    assert not triangle_check(5, 3, 1)