"""Stack implementation module."""

from typing import Generic, TypeVar

from rich.console import Console
from rich.panel import Panel

T = TypeVar("T")


class Stack(Generic[T]):
    """A stack implementation using lists.

    It follows the LIFO principle (last in, first out).
    It only has a few basic operations :
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the top item.
        peek(): Return the top item without removing it.
        is_empty(): Check if the stack is empty.
        size(): Return the size of the stack.
    """

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items = []

    def push(self, item: T) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            err_msg = "Cannot pop from an empty stack"
            raise IndexError(err_msg)
        return self._items.pop()

    def peek(self) -> T:
        """Return the top element of the stack without removing it."""
        if self.is_empty():
            err_msg = "Cannot peek from an empty stack"
            raise IndexError(err_msg)
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the size of the stack."""
        return len(self._items)

    def __str__(self) -> str:
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack: [empty]"

        console = Console(record=True)

        items_reversed = self._items.copy()
        items_reversed.reverse()
        lines = []
        for i, item in enumerate(items_reversed):
            prefix = "TOP → " if i == 0 else "      "
            lines.append(f"{prefix}{item}")
        panel = Panel(
            "\n".join(lines),
            title="[bold blue]Stack[/bold blue]",
            border_style="blue",
            expand=False,
        )
        console.print(panel)
        return console.export_text()
