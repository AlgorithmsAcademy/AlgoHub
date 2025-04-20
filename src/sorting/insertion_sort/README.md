# 🧠 Insertion Sort

## 📝 Description

Insertion sort is a comparison-based sorting algorithm.
It builds the final sorted array one item at a time, much like how you might sort playing cards in your hands.

## 💾 Time Complexity

| Case     | Complexity |
| -------- | ---------- |
| Best     | $O(n)$     |
| Worst    | $O(n^2)$   |
|  Average |  $O(n^2)$  |

## 💾 Space Complexity

The algorithm is in-place, so the space complexity is $O(1)$.

## 💡 Intuition

The idea is to think of it like sorting a hand of playing cards as you receive them:

- Imagine the cards face down on the table, and you pick them up one by one.

- Start with an empty left hand and take the top card from the table.

- As you pick up each new card, insert it into the correct position among the cards already in your hand.

- To find the correct position, compare the new card with the cards in your hand from right to left.

- At all times, the cards in your hand remain sorted — and by the end, the full set is sorted.

This mirrors the insertion sort algorithm, where the left portion of the array is always sorted, and each new element is inserted in its proper place.

## 🧾 Pseudocode

```text
insertion_sort(A[1 ... n], n):
    for i = 2 to n:
        card = A[i]
        // insert card into sorted sequence A[1 ... j - 1]
        j = i - 1
        while (j > 0 && A[j] > card):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = card
```

## 📈 Time Complexity Analysis

- In the worst case (array is sorted in reverse order):

  - Every new card has to be pushed to the end of the array.

  - This results in a complexity of $1 + 2 + ... + n - 1 = O(n^2)$.

- In the best case (array is already sorted), we never enter the while loop as every new card is already in place. Thus the complexity is $O(n)$.
