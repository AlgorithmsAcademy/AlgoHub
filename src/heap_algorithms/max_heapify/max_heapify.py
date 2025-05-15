"""Max-Heapify Algorithm."""


def max_heapify(array: list[int], i: int) -> None:
    """Ensure the subtree rooted at index i satisfies the max-heap property.

    Parameters
    ----------
    array : list[int]
        An array representing a heap where the left and right subtrees of index i are max heaps.
    i : int
        The index to heapify.

    """
    n = len(array)
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)
