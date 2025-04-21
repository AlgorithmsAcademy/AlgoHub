"""Linear Search Algorithm."""


def linear_search(array: list[int], target: int) -> int:
    """In-place implementation of linear search.

    Parameters
    ----------
    array : list[Any]
        The list of variable.
    target : Any
        The element to be searched

    Returns
    -------
    int :
        The same list, sorted in ascending order.

    """
    for i in range(array):
        if array[i] == target:
            return i

    return -1
