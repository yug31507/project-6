# project-6

# Personal Journal Manager Documentation

## Introduction
The **Personal Journal Manager** is a Python-based command-line application designed to help users conveniently create, view, search, and manage daily journal entries[cite: 1]. Encapsulated within a `JManager` class, the script automatically handles file creation, error handling for permissions, and interactive menu navigation[cite: 1].

---

## Features
* **Automated File Initialization**: Automatically checks for or creates a local `journal.txt` file upon startup[cite: 1].
* **Timestamped Entries**: Appends user entries with precise system date and time stamps (`%Y-%m-%d %H:%M:%S`)[cite: 1].
* **Comprehensive Viewing**: Displays the entire collection of stored journal entries in a structured format[cite: 1].
* **Keyword & Date Search**: Scans entries for specific keywords or dates to locate relevant notes quickly[cite: 1].
* **Safe Deletion Protocol**: Provides an explicit confirmation prompt (`yes`/`no`) before allowing users to clear all journal entries[cite: 1].

---

## Core Concepts
* **Object-Oriented Programming (OOP)**: Utilizes the `JManager` class to bundle data and functions—such as adding, viewing, searching, and deleting—into a single modular blueprint[cite: 1].
* **Exception Handling**: Implements robust `try-except` blocks to gracefully catch common file system errors like `FileExistsError`, `FileNotFoundError`, and `PermissionError`[cite: 1].
* **File I/O Operations**: Leverages Python's built-in file handling modes (`"x"`, `"a"`, `"r"`, and `"w"`) to create, append, read, and overwrite text data securely[cite: 1].
* **Control Flow**: Combines an interactive `while` loop with Python's structural `match-case` statement to handle continuous menu selections[cite: 1].

---

## Tools & Editor (VS Code, GitHub)
* **Visual Studio Code (VS Code)**: An ideal code editor for developing and debugging this script, offering integrated terminal support to run the interactive prompt seamlessly.
* **Git & GitHub**: Perfect for version control. You can initialize a Git repository locally, track changes to `file_operator.py`, and push your code to GitHub to back up your project or share it with others.

---

### Repository Structure
```text
yug/Project-6
├── File Operator.py
├── README.md
