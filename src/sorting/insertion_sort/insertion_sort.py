"""Insertion Sort Algorithm."""

from typing import Any


def insertion_sort(array: list[Any]) -> list[Any]:
    """In-place implementation of insertion sort.

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
    for i in range(1, n):
        key = array[i]
        # Insert key into the sorted sequence array[0 ... i-1]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array
