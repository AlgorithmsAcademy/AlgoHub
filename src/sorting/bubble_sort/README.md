# 🧠 Bubble Sort

## 📝 Description

Bubble Sort is simple comparison-based sorting algorithm, but not the most efficient option.

## 💾 Time Complexity

| Case  | Complexity  |
| ----- | ----------- |
| Best  | $\Omega(n)$ |
| Worst | $O(n^2)$    |

## 💾 Space Complexity

The algorithm is in-place, so the space complexity is $O(1)$.

## 💡 Intuition By Analogy

The idea is that during each iteration, the largest unsorted element is moved to its correct position at the right hand side of the array. After the first pass, the largest element is in place; after the second, the second largest, and so on. This continues until the array is sorted.

## 🧾 Pseudocode

```text
bubble_sort(A, n):
    for i = 1 to n:
        changed = false
        for j = 1 to n - i:
            if A[j] > A[j + 1]:
                swap A[j] and A[j + 1]
                changed = true
        if not changed:
            break
```

## 📈 Time Complexity Analysis

- In the wost case (list is in sorted in reverse order), Bubble Sort performs:

  - First pass: $n - 1$ comparisons and swaps.
  - Second pass: $n - 2$ comparisons and swaps.
  - ...
  - Last pass: $1$ comparison and swap.

  So the total number of operations is

  $$
  \sum_{i=1}^{n-1} i = \frac{(n - 1) \cdot n}{2} = O(n^2)
  $$

- In the best case (list is already sorted), Bubble Sort only performs one pass and then exits.
  Thus the complexty is $O(n)$.
