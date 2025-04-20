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
        A new list, sorted in ascending order.

    """
    n = len(array)
    if n <= 1:
        return array
    q = n // 2
    return merge(merge_sort(array[:q]), merge_sort(array[q:]))


def merge(left: list[Any], right: list[Any]) -> list[Any]:
    """Merge two sorted lists into a single sorted list.

    Parameters
    ----------
    left : list[Any]
        The first sorted list.
    right: list[Any]
        The second sorted list.

    Returns
    -------
    list[Any]
        A new list that has merged left and right.

    """
    n1 = len(left)
    n2 = len(right)
    res = []
    i = j = 0
    while i < n1 and j < n2:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
