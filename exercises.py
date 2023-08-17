def bubble_sort(a):
    # a = name of list
    b = len(a) - 1;
    # minus 1 because we always compare 2 adjacent values
    for x in range(b):
        for y in range(b - x):
            if a[y] > a[y + 1]:
                a[y], a[y + 1] = a[y + 1], a[y]


def star_triangle(number_of_rows):
    for x in range(number_of_rows):
        print(' '*(number_of_rows-x-1)+'*'*(2*x+1))


def fibonacci_series(number):
    if number == 1:
        return [0]
    list = [0, 1]
    for i in range(number-2):
        next = list[i] + list[i+1]
        list.append(next)
    return list




def triangle_check(a, b, c):
    return a + b >= c and a + c >= b and c + b >= a
