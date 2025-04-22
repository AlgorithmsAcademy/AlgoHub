import pytest

from src.datastructures.stack.stack import Stack


def test_init() -> None:
    """Test that a new stack is empty."""
    stack = Stack()
    assert stack.is_empty()
    assert stack.size() == 0


@pytest.mark.parametrize(
    "items", [[], [1], [1, 2, 3], ["a", "b", "c"], [1, "two", 3.0, [4], {"five": 5}]]
)
def test_push_and_size(items: list) -> None:
    """Test pushing items onto the stack and checking size."""
    stack = Stack()

    for i, item in enumerate(items, 1):
        stack.push(item)
        assert stack.size() == i

    assert stack.size() == len(items)


@pytest.mark.parametrize(
    "items", [[1], [1, 2, 3], ["a", "b", "c"], [1, "two", 3.0, [4], {"five": 5}]]
)
def test_pop(items: list) -> None:
    """Test popping items from the stack."""
    stack = Stack()

    # Push all items
    for item in items:
        stack.push(item)

    # Pop items and verify LIFO order
    for i in range(len(items) - 1, -1, -1):
        assert stack.pop() == items[i]

    # Stack should be empty after popping all items
    assert stack.is_empty()
    assert stack.size() == 0


def test_pop_empty_stack() -> None:
    """Test that popping from an empty stack raises IndexError."""
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


@pytest.mark.parametrize(
    "items", [[1], [1, 2, 3], ["a", "b", "c"], [1, "two", 3.0, [4], {"five": 5}]]
)
def test_peek(items: list) -> None:
    """Test peeking at the top item without removing it."""
    stack = Stack()

    # Push all items
    for item in items:
        stack.push(item)
        # Peek should return the item just added
        assert stack.peek() == item

    # Final peek should be the last item
    assert stack.peek() == items[-1]

    # Size should not change
    assert stack.size() == len(items)


def test_peek_empty_stack() -> None:
    """Test that peeking at an empty stack raises IndexError."""
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()


@pytest.mark.parametrize(
    ("items", "expected_empty"), [([], True), ([1], False), ([1, 2, 3], False)]
)
def test_is_empty(items: list, *, expected_empty: bool) -> None:
    """Test the is_empty method."""
    stack = Stack()

    for item in items:
        stack.push(item)

    assert stack.is_empty() == expected_empty


@pytest.mark.parametrize("items", [[1, 2, 3], ["a", "b", "c"], [1, "two", 3.0]])
def test_lifo_order(items: list) -> None:
    """Test that stack maintains LIFO (Last In First Out) order."""
    stack = Stack()

    for item in items:
        stack.push(item)

    # Pop items and verify they come out in reverse order
    reversed_items = list(reversed(items))
    for _i, expected in enumerate(reversed_items):
        assert stack.pop() == expected


def test_string_representation() -> None:
    """Test the string representation of the stack."""
    stack = Stack()

    # Empty stack representation
    rep = str(stack)
    assert "empty" in rep.lower() or "[]" in rep

    # Stack with items
    stack.push(1)
    stack.push(2)
    stack.push(3)

    rep = str(stack)
    assert "Stack" in rep
    assert "3" in rep
    assert "2" in rep
    assert "1" in rep
