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
        The index of the target inside array.

    """
    for i, elem in enumerate(array):
        if elem == target:
            return i

    return -1
