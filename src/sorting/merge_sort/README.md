# 🧠 Merge Sort

## 📝 Description

Merge Sort is a divide-and-conquer sorting algorithm that works by recursively splitting the list into halves until each sublist contains a single element (which is inherently sorted),
and then merging those sublists back together in a way that results in a sorted list.

## 💾 Time Complexity

$\Theta(n\log(n))$

## 💾 Space Complexity

The space complexity is $O(n)$ as for each merge step, we create two arrays with linear memory.

## 💡 Intuition

The core challenge of Merge Sort lies in the merge step.

That is, once we have two sorted subarrays A[p ... q] and A[q + 1 ... r], how do we efficiently combine them into a single sorted array?

We can achieve this in $O(n)$ time, where $n = r - p + 1$, using the following analogy:

> Think of the two subarrays as two face-up decks of cards, where the visible card is the smallest remaining in the deck.

- At each step, compare the top cards from both decks.

- Pick the smaller and place it into the output pile.

- Repeat until all cards are merged into the output.

- Since there are exactly $n$ cards total, the process stops after $n$ steps.

This ensures a linear-time merge while maintaining sorted order — a key to the efficiency of Merge Sort.

## 🧾 Pseudocode

```text
merge_sort(A[p ... r], p, r):
    if p < r:
        q = ⌊(p + r) / 2⌋       // divide
        merge_sort(A, p, q)     // conquer
        merge_sort(A, q + 1, r) // conquer
        merge(A, p, q, r)       // combine
```

```text
merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    Let L[1 ... n1 + 1] and R[1 ... n2 + 1] be new arrays

    for i = 1 to n1:
        L[i] = A[p + i - 1]

    for j = 1 to n2:
        R[j] = A[q + j]

    L[n1 + 1] = ∞
    L[n2 + 1] = ∞

    i = 1 // Pointer to first "deck of cards"
    j = 1 // Pointer to second "deck of cards"

    for k = p to r:
        if L[i] <= L[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
```

## 📈 Time Complexity Analysis

Given the above pseudocode, we can write the running time as:

$T(n) = 2T(\frac{n}{2}) + \Theta(n)$.

By the master theorem, $T(n) = n\log(n)$.
