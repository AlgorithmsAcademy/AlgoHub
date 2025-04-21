# 👥 Contributing to AlgoHub

Thank you for your interest in contributing to AlgoHub! 🎉

We welcome all kinds of contributions—whether you're fixing bugs, improving docs, adding new algorithms, or refining tests.

## ✅ What you can contribute

- Add a new algorithm or data structure
- Improve or correct existing implementations
- Write or update documentation
- Add test cases or enhance test coverage
- Fix typos or bugs

## Guidelines

- **Coding Standards:**
  Follow clean and consistent coding practices. Use meaningful variable and function names.

- **Document Your Code:**
  Ensure all functions have clear and concise comments/description.

- **Test Your Changes:**
  While we understand that fully testing this library may be challenging, ensure your code works as intended before submitting. Focus on edge cases and confirm that your changes integrate smoothly with existing functionality.

- **Be Respectful**:
  Engage in discussions respectfully and constructively.

- **Follow The File Structure Templates**: Each Algorithm should have its own file in **scr** with: A README based on the template and the python file. Parallel to that you should create another file inside tests with a python file torun the tests and a YAML file to store the tests cases.

## Before Contributing

Before making the first commit of the session, you should set up the **pre-commit** framework and activate the **virtual environment**. This has to be done for each new session.

1. Start by activating the Python virtual environment:

   ```bash
   source .venv/bin/activate
   ```

2. Then, set up the pre-commit hooks:
   ```bash
   pre-commit install
   ```

## 📁 File Structure

When adding a new algorithm, follow this structure:

```
AlgoHub/
│
├── src/
│   ├── new_data_structure
|   |       └── new_data_structure/
│   |           ├── README.md        # Explanation and usage
│   |           ├── __init__.py
│   |           └── new_data_structure.py
│   └── algorithm_type
│       └── new_algorithm/
│           ├── README.md        # Explanation and usage
│           ├── __init__.py
│           └── new_algorithm.py
│
├── tests/
|   ├── new_data_structure
│   |       ├── test_new_data_structure.py
│   |       ├── __init__.py
│   |       └── test_cases.yaml
│   └── algorithm_type
│       └── your_algorithm/
│           ├── test_new_algorithm.py
│           ├── __init__.py
│           └── test_cases.yaml       # Test cases

```

### Algorithm README.md

The README.md inside the **New_Algorithm** folder should follow the following template.

```
# 🧠 Algorithm Name
## 📝 Description
 <!-- Brief explanation of what the algorithm does and its purpose. Keep it beginner-friendly. -->
## 💾 Time Complexity

| Case  | Complexity |
| ----- | ---------- |
| Best  | $\Omega()$ |   <!-- e.g., $\Omega(n)$ -->
| Worst | $O()$      |   <!-- e.g., $O(n^2)$ -->

## 💾 Space Complexity
<!-- Describe the space complexity. -->

## 💡 Intuition By Analogy
<!-- Describe the high-level idea behind how the algorithm works. Use metaphors, visual cues, or simple reasoning to make it intuitive. -->

## 🧾 Pseudocode
<!-- Pseudocode syntax, not code. Use loops, conditions, and indentation to mimic logic flow. -->

## 📈 Time Complexity Analysis
<!-- Give a step-by-step breakdown of how you derive the time complexity. Include summation formulas, case analysis, and any assumptions. -->

- **Worst case**:
<!-- Description + math if applicable -->

- **Best case**:
<!-- Description + math if applicable -->

- **Average case**:
<!-- Description + math -->
```

### Data structureREADME.md

The README.md inside the **New_Data_Structure** folder should follow the following template.

```
#🧠 Data Structure Name
## 📊 Visual Representation
<!-- Add a visual representation of the data structure and how it operates. For example, a diagram of a stack showing how elements are added and removed, or a flowchart of a function like `push` or `pop`. -->

## 📝 Description
  <!-- Brief explanation of what the data structure is, its use case, and purpose. Keep it beginner-friendly. For example: "A stack is a linear data structure that follows the Last In First Out (LIFO) principle, where the last element added is the first one to be removed." -->
## 💾 Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Insertion | $O()$      |
| Deletion  | $O()$      |
| Access    | $O()$      |
| Search    | $O()$      |

## 💾 Space Complexity
<!-- Describe the space complexity. Is it constant space or does it grow with the number of elements? For example: "The space complexity of a stack is $O(n)$, where $n$ is the number of elements stored in the stack." -->

## 💡 Intuition By Analogy
<!-- Describe the high-level idea behind how the data structure works. Use metaphors, visual cues, or simple reasoning to make it intuitive. For example, "Think of a stack as a stack of plates in a cafeteria. You can only add a plate on top or remove the top plate; you can't access the plates at the bottom until you remove the ones on top." -->

## 🧾 Pseudocode
<!-- Provide pseudocode for operations like insertion, deletion, or searching. Use loops, conditions, and indentation to mimic the logic flow. -->

## 📈 Time Complexity Analysis
 <!-- Break down the time complexity for the major operations. -->

- **Insertion**:

- **Deletion**:

- **Access**:

- **Search**:

```

## 🐛 Bug Report

To report a bug, create a new issue with the **bug** tag. The severity of the bug should be included using the following emojis:

- 🔥 Blocker (can’t proceed)
- 🛑 Major (big problem, workaround exists)
- ⚠️ Minor (cosmetic or rare)
- ❓ Not sure

The name of the issue should match the following template:

```
[severity_emojis Bug] name_of_the_algorithm
```

The description of the issue should match the following template:

```
# 🐛 Bug Report
## Bug Description
<!-- A clear and concise description of what the bug is. -->

## To Reproduce
Steps to reproduce the behavior:
<!-- Enumerate all the steps to reproduce the bug. -->

## Expected behavior
<!-- A clear and concise description of what you expected to happen. -->

## Environment (please complete the following information):
<!-- Fill the following -->
- Python version:
- Environment Version:

## Other
<!-- If the report needs any other detail add it in this section. -->

```
