# 🧠 Binary Search

## 📝 Description

Binary search is a divide and conquer algorithm that efficiently finds the position of a target element within a sorted array. By repeatedly halving the search space, binary search eliminates half of the remaining elements in each step. This makes it much faster than linear search, especially for large datasets.

## 💾 Time Complexity

| Case  | Complexity         |
| ----- | ------------------ |
| Best  | $O(1)$             |
| Worst | $O(\text{log}(n))$ |

## 💾 Space Complexity

The **space complexity** of binary search is **O(1)**, since there are no new space alocations.

## 💡 Intuition

To be filled.

## 🧾 Pseudocode

```
BinarySearch(array, element):
    Set start to 0
    Set end to length of array - 1

    While start <= end
        Set mid to (start + end) div 2

        If array[mid] == element
            Return mid

        Else If array[mid] > element
            Set end to mid - 1

        Else
            Set start to mid + 1
        End if
    End loop

    Return -1
```

## 📈 Time Complexity Analysis

- **Worst case**:
  The worst case will be when the element is present in the first position. As seen in the average case, the comparison required to reach the first element is **log(N)**. So the time complexity for the worst case is **O(logN)**.

- **Best case**:
  Best case is when the element is at the middle index of the array. It takes only one comparison to find the target element. So the best case complexity is O(1).
