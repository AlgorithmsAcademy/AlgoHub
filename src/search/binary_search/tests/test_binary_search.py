import pytest

from src.search.binary_search.binary_search import binary_search


@pytest.mark.parametrize(
    ("array", "target", "expected_index"),
    [
        ([], 1, -1),  # Empty list
        ([1], 1, 0),  # Single element match
        ([1], 2, -1),  # Single element no match
        ([1, 2, 3], 2, 1),  # Middle
        ([1, 2, 3], 1, 0),  # First
        ([1, 2, 3], 3, 2),  # Last
        ([1, 2, 3, 3, 3, 4], 3, 2),  # First match for repeated
    ],
)
def test_search_basic_cases(array: list[int], target: int, expected_index: int) -> None:
    """Test searching for values in different lists."""
    result = binary_search(array, target)
    if expected_index == -1:
        assert result == -1
    else:
        assert array[result] == target
