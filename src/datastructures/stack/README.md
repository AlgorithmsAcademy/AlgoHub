# 🧠 Stack

## 📊 Visual Representation

```
┌─Stack────────┐
│              │
│ TOP → item3  │
│       item2  │
│       item1  │
│              │
└──────────────┘
```

## 📝 Description

A stack is a linear data structure that follows the Last In First Out (LIFO) principle, where the last element added is the first one to be removed. Think of it like a stack of plates - you can only add a plate to the top or remove the top plate.

This implementation provides the following core operations:

- **push**: Add an item to the top of the stack
- **pop**: Remove and return the top item from the stack
- **peek**: Return the top item without removing it
- **is_empty**: Check if the stack is empty
- **size**: Return the number of items in the stack

## 💾 Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |
| Peek      | O(1)       |
| Is Empty  | O(1)       |
| Size      | O(1)       |

## 💾 Space Complexity

The space complexity of a stack is O(n), where n is the number of elements stored in the stack.

## 💡 Intuition By Analogy

Think of a stack as a stack of books on a table. You can only add a new book on top of the pile or remove the top book. You cannot access or remove books in the middle or at the bottom without first removing all the books above it. This is why it's called "Last In, First Out" (LIFO) - the last book you placed is the first one you can take.

## 🧾 Pseudocode

**Push Operation:**

```
function push(item):
    add item to the end of the list
```

**Pop Operation:**

```
function pop():
    if stack is empty:
        raise error
    item = remove last element from list
    return item
```

**Peek Operation:**

```
function peek():
    if stack is empty:
        raise error
    return last element in list
```

**Is Empty Operation:**

```
function is_empty():
    return length of list equals 0
```

**Size Operation:**

```
function size():
    return length of list
```

## 📈 Time Complexity Analysis

- **Push**: O(1) - Adding an element to the end of a dynamic array (Python list) is a constant-time operation in the amortized case since we're just appending to the end of the array.

- **Pop**: O(1) - Removing the last element from a dynamic array is also a constant-time operation as we're simply decrementing the size and returning that element.

- **Peek**: O(1) - Accessing the last element in a list is a constant-time operation, as we're directly indexing into the array.

- **Is Empty**: O(1) - Checking the length of a list in Python is a constant-time operation.

- **Size**: O(1) - Similar to is_empty, getting the size of the internal list is a constant-time operation.
