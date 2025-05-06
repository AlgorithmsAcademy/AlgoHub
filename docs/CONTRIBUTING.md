# 👥 Contributing to AlgoHub

Thank you for your interest in contributing to AlgoHub! 🎉

We welcome all kinds of contributions—whether you're fixing bugs, improving docs, adding new algorithms, or refining tests.

## ✅ What you can contribute

- Report bug
- Add a new algorithm or data structure
- Improve or correct existing implementations
- Write or update documentation
- Add test cases or enhance test coverage
- Fix typos

## How to contribut

Every change in the repository should be merged through [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests). All commit execute [Ruff](https://docs.astral.sh/ruff/) to insure some level of coding standard.

### Before Contributing

Before making the first commit of the session, you should set up the **pre-commit** framework and activate the **virtual environment**. This has to be done for each new session.

1. Start by activating the Python virtual environment:

   ```bash
   source .venv/bin/activate
   ```

2. Then, set up the pre-commit hooks:
   ```bash
   pre-commit install
   ```

### Implementing a new algorithm

Before implementing a new algorithm. The Python virtual environment should include [rich](https://pypi.org/project/rich/) and [pytest](https://pypi.org/project/pytest/). From the cloned repository run the command below for a quick installation.

```bash
pip install -r requirements.txt
```

Every algorithm implementation should have a dedicated **issue**. This issue should be built with the **Implement Algorithm** issue form. If no issue exists for the specific algorithm to be implemented create one. Every file inside the new repository and the **test file** should follow the file structure inside [File Structure](#📁-file-structure) section.

All algorithm should be accompanied with a **README.md** file. This file should follow the template in the [Algorithm README.md](#algorithm-readme) section.

Every algorithm should be tested using [pytest](https://docs.pytest.org/en/stable/).

## 🐛 Bug Report

To report a bug, simply create a new issue using the **Bug Report** form and fill out all sections.
The form is straightforward, but if you’d like a bit more guidance, follow the steps below. 👇

### 📝 Steps to Report a Bug

1. **Enter a clear, short title**
   Use a short, clear title that describes the issue.

   > Example: `Crash when clicking the login button`

2. **What type of issue is this? (Bug Type)**

- 🧮 Algorithm Implementation - The logic or output of an algorithm is incorrect.
- 🛠 CI/Tooling Issue - Problems with continuous integration or scripts.
- 📘 Algorithm Documentation - Missing or incorrect explanations/comments for an algorithm.
- 🖋 General Documentation - Typos, formatting, or missing information inside documentation that is not related to an algorithm.
- 🧪 Test Failure or Adding Testcase - Broken tests or missing edge case coverage.
- ❓ Other / Not Sure - You’re unsure how bad it is or some other kind of issue.

3. **In the Steps to Reproduce & What Happens section:**

- List step-by-step instructions to trigger the bug
- Describe what actually happens

4. **Describe what you expected to happen(Expected Behavior):**
   In the Expected Behavior section, explain what you thought would happen instead.

5. **Create the issue:**
   Once you create the issue, our system will automatically format the title.
   This formatting takes about 4 seconds.

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
│           └── __init__.py

```

### Algorithm README

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
