# 🧠 Max-Heapify

## 📝 Description

Given an index $i$ in an array representing a heap, where the binary trees rooted at the **left** and **right** children of $i$ already satisfy the **max-heap property**, `MAX-HEAPIFY` ensures that the tree rooted at $i$ also satisfies the max-heap property.

This operation is typically used as a subroutine in other heap operations like `build_heap`, and `heap_sort`.

## 💾 Time Complexity

$O(\log n)$

## 💾 Space Complexity

$\Theta(1)$ (in-place operation using recursion stack if not implemented iteratively)

## 💡 Intuition

The goal is to move the largest element among `i`, `left(i)`, and `right(i)` to the top of the subtree rooted at `i`:

- Since the left and right subtrees of `i` are already max-heaps, the only possible violation of the heap property is between `i` and its children.
- We compare `A[i]`, `A[left(i)]`, and `A[right(i)]`, and if `A[i]` is not the largest, we **swap it with the largest child**.
- We then recursively call `MAX-HEAPIFY` on the affected child position to fix the subtree.

This process continues until the max-heap property is restored — typically when we reach a leaf node or a local max.

## 🧾 Pseudocode

```text
MAX-HEAPIFY(A[1 ... n], i):
    l = left(i)
    r = right(i)
    largest = i
    if l ≤ n and A[l] > A[i]:
        largest = l
    if r ≤ n and A[r] > A[largest]:
        largest = r
    if largest ≠ i:
        swap A[i] and A[largest]
        MAX-HEAPIFY(A, largest)
```

## 📈 Time Complexity Analysis

As a heap is a binary tree, the time complexity is $\Theta($ height of $i) = O(\log(n))$.
