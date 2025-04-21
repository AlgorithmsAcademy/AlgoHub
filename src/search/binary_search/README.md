# 🧠 Binary Search

## 📝 Description

Binary search is a divide and conquer algorithm that efficiently finds the position of a target element within a sorted array. By repeatedly halving the search space, binary search eliminates half of the remaining elements in each step. This makes it much faster than linear search, especially for large datasets.

## 💾 Time Complexity

| Case  | Complexity   |
| ----- | ------------ |
| Best  | $O(1)$       |
| Worst | $O(\log(n))$ |

## 💾 Space Complexity

The algorithm is in-place, so the space complexity is $O(1)$.

## 💡 Intuition By Analogy

The algorithm is pretty straightforward. Since the array is sorted, we can leverage the order of elements to significantly reduce the search space. Instead of scanning each element one by one like linear search, we compare the middle element with the target:

- If it's equal, we’re done.

- If the target is smaller, we know it must lie in the left half.

- If it's larger, we search the right half.

## 🧾 Pseudocode

```
binary_search(A[1 ... n], target):
    start = 1
    end = n
    while start <= end:
        mid = ⌊(start + end) / 2⌋

        if A[mid] == target:
            return mid

        else if element < A[mid]:
            end = mid - 1

        else:
            start = mid + 1
    return -1
```

## 📈 Time Complexity Analysis

- **Worst Case**:
  In the worst case, the algorithm continues halving the array until only one element remains. This results in a logarithmic number of comparisons, specifically $\log_2 n$, but asymptotically we denote it as $O(\log n)$.

- **Best case**:
  Best case is when the element is at the middle index of the array. It takes only one comparison to find the target element. So the best case complexity is O(1).
