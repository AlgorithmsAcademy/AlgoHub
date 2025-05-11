import pytest

from src.sorting.bubble_sort.bubble_sort import bubble_sort


@pytest.mark.parametrize(
    ("array", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([5, 3, 8, 1], [1, 3, 5, 8]),
        ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([3, 3, 3], [3, 3, 3]),
        ([9, -1, 5, 3, 3, 7], [-1, 3, 3, 5, 7, 9]),
        (["b", "a", "d", "c"], ["a", "b", "c", "d"]),
    ],
)
def test_sort_basic_cases(array: list, expected: list) -> None:
    """Test sorting on various basic input arrays."""
    result = bubble_sort(array)
    assert array == expected
    assert result == expected
