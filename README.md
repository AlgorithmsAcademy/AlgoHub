# AlgoHub

<p align="center">
  <img src="docs/source_images/AlgoHub_Logo_1.png" width="250">
  <br>
</p>

<!-- Will work once the repo is public -->

![GitHub stars](https://img.shields.io/github/stars/AlgorithmsAcademy/AlgoHub?style=flat)
![GitHub License](https://img.shields.io/github/license/AlgorithmsAcademy/AlgoHub)
![GitHub top language](https://img.shields.io/github/languages/top/AlgorithmsAcademy/AlgoHub)
![GitHub last commit](https://img.shields.io/github/last-commit/AlgorithmsAcademy/AlgoHub)

This repo collects common algorithms & data structures that are useful for interviews — each with

1. a **written and/or visual explanation**
2. a **python implementation**
3. **test cases**

## Installation

1. Install [uv](https://github.com/astral-sh/uv) - a fast Python package installer and resolver. See the [official documentation](https://github.com/astral-sh/uv#installation) for installation instructions.

2. Clone the repository and setup the environment:

   ```bash
   git clone https://github.com/AlgorithmsAcademy/AlgoHub.git
   ```

3. From the **git** repository synchronizes your Python environment by executing the following command:
   ```bash
   uv sync --all-extras
   ```

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

## Contribution

### Guidelines

- **Coding Standards:**
  Follow clean and consistent coding practices. Use meaningful variable and function names.

- **Document Your Code:**
  Ensure all functions have clear and concise comments/description.

- **Test Your Changes:**
  While we understand that fully testing this library may be challenging, ensure your code works as intended before submitting. Focus on edge cases and confirm that your changes integrate smoothly with existing functionality.

- **Be Respectful**:
  Engage in discussions respectfully and constructively.

- **Follow The File Structure Templates**: Each Algorithm should have its own file in **scr** with: A README based on the template and the python file. Parallel to that you should create another file inside tests with a python file torun the tests and a YAML file to store the tests cases.

### Bug Report

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
