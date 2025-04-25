"""Counting Sort Algorithm."""


def counting_sort(array: list[int], max_value: int) -> list[int]:
    """Sort a list of integers from 1 to max_value using counting sort.

    Parameters
    ----------
    array : list[Any]
        The list of integers from 1 to max_value.

    max_value : int
        The maximum value inside the array.

    Returns
    -------
    list[Any]
        The same list, sorted in ascending order.

    """
    count = [0] * max_value
    output = [-1] * len(array)

    # counting elements in array
    for i in array:
        count[i - 1] += 1

    # weighting of counting
    for i in range(len(count) - 1):
        count[i + 1] = count[i + 1] + count[i]

    # sorting using count
    for i in range(len(array)):
        element = array[i] - 1
        count[element] -= 1
        output[count[element]] = array[i]

    return output
