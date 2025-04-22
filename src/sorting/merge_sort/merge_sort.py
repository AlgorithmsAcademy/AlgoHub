"""Merge Sort Algorithm."""

from typing import Any


def merge_sort(array: list[Any]) -> list[Any]:
    """Sorts the input array using the merge sort algorithm.

    Parameters
    ----------
    array : list[Any]
        The list of comparable elements to sort.

    Returns
    -------
    list[Any]
        The same list but sorted in increasing order.

    """
    _merge_sort(array, 0, len(array) - 1)
    return array


def _merge_sort(array: list[Any], p: int, r: int) -> None:
    """Sorts the input array (from p to r) using the merge sort algorithm.

    Parameters
    ----------
    array : list[Any]
        The list of comparable elements to sort.
    p : int
        Start index.
    r : int
        End index.

    """
    if p < r:
        q = (p + r) // 2
        _merge_sort(array, p, q)
        _merge_sort(array, q + 1, r)
        merge(array, p, q, r)


def merge(array: list[Any], p: int, q: int, r: int) -> None:
    """Merge the two sorted subarrays array[p..q] and array[q+1..r] into a single sorted subarray.

    Parameters
    ----------
    array : list[Any]
        The list where merging will occur.
    p : int
        Start index.
    q : int
        Middle index.
    r : int
        End index.

    """
    left = array[p : q + 1]
    right = array[q + 1 : r + 1]

    n1 = len(left)
    n2 = len(right)

    i = j = 0
    k = p

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right[j]
        j += 1
        k += 1
