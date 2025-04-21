# 🧠 Linear Search

## 📝 Description

Linear search look for a specific element inside an unsorted array. The output of this algorithm is the index of this element. If the element isnt inside the array then the output is **-1**.

## 💾 Time Complexity

| Case  | Complexity |
| ----- | ---------- |
| Best  | $O(1)$     |
| Worst | $O(n)$     |

## 💾 Space Complexity

The algorithm is in-place, so the space complexity is $(1)$.

## 💡 Intuition By Analogy

Imagine you're looking for a specific word in a dictionary. Instead of flipping directly to the word, you start from the first page and check if the word appears on that page. If the word isn't there, you move to the next page, and so on, until you find the word. Once you find the word, you note the page number and stop searching.

## 🧾 Pseudocode

Let `array` be an unsorted array of element with any type and `target` be the element we are looking for, then:

```
linear_search(array, target):
    assine the number of element in array to N
    for i=0 to N - 1
        if array[i] == target
            return i
    return -1
```

## 📈 Time Complexity Analysis

Give a step-by-step breakdown of how you derive the time complexity. Include summation formulas, case analysis, and any assumptions.

- **Worst Case**:
  Let the size of the array be $n$.

  - In the worst case, the algorithm performs $n$ comparisons (because it checks all elements in the array once).
  - Each comparison is a constant time operation, so the total number of operations is directly proportional to $n$.
  - Then the complexity in the **worst case** is $O(n)$.

- **Best Case**:

  - $n$ the best case, the algorithm performs exactly **1** comparison (since the target is found at the first position).
  - Therefore, the total number of operations is constant, regardless of the size of the array.
  - Then the complexity in the **best case** is $O(1)$.

- **Average Case**:
  - If the target is found in the array, we expect it to be found after checking approximately half of the elements (since we are assuming random distribution). On average, we would expect to perform $\frac{n}{2}$ comparisons.
  - If the target is absent, the algorithm will go through all $n$ elements and return **-1** after checking all of them. Thus, on average, the algorithm will check about $\frac{n}{2}$ elements before it either finds the target or completes the search.
  - Then the complexity in the **average case** is $O(n)$.
