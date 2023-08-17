from exercises import *


def test_bubble_sort():
    a = [99, 32, 5, 3, 6, 7, 54, 87]
    bubble_sort(a)
    assert a == [3, 5, 6, 7, 32, 54, 87, 99]

def test_star_triangle():
    a = 9
    star_triangle(a)
    assert 1==1

