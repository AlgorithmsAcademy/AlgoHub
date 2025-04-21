"""Binary Search Algorithm."""


def binary_search(array: list[int], target: int) -> int:
    """In-place implementation of binary_search.

    Parameters
    ----------
    array : list[int]
        The list of comparable elements sorted in increasing order.
    target : int
        The element to be searched.

    Returns
    -------
    int
        Returns the index of the element to be searched, or -1 if not found.

    """
    return binary_search_recursive(array, target, 0, len(array) - 1)


def binary_search_recursive(array: list[int], target: int, start: int, end: int) -> int:
    """Perform a recursive binary search.

    Parameters
    ----------
    array : list[int]
        The list of comparable elements sorted in increasing order.
    target : int
        The element to be searched.
    start : int
        The index where the function starts the search.
    end : int
        The index where the function ends the search.

    Returns
    -------
    int
        Returns the index of the element to be searched, or -1 if not found.

    """
    if start > end:
        return -1  # Element not found

    mid = (start + end) // 2

    if array[mid] == target:
        return mid  # Element found
    if array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    return binary_search_recursive(array, target, mid + 1, end)
