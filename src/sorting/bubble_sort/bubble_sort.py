"""Bubble Sort Algorithm."""

from typing import Any


def bubble_sort(array: list[Any]) -> list[Any]:
    """In-place implementation of bubble sort.

    Parameters
    ----------
    array : list[Any]
        The list of comparable elements to sort.

    Returns
    -------
    list[Any]
        The same list, sorted in ascending order.

    """
    n = len(array)
    for i in range(n):
        changed = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                changed = True
        if not changed:
            break

    return array