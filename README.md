# LinkedList Implementation

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![Build Status](https://img.shields.io/github/workflow/status/atabekdemurtaza/LinkedList_implementation/CI)
![License](https://img.shields.io/github/license/atabekdemurtaza/LinkedList_implementation)
![Code Style](https://img.shields.io/badge/code%20style-pep8-green)
![Test Coverage](https://img.shields.io/badge/test%20coverage-100%25-success)

This repository contains an implementation of a singly linked list in Python, complete with robust unit tests using `pytest`, logging with `loguru`, and visualization using `graphviz`. The implementation supports operations like adding nodes to the beginning, end, before, or after certain nodes, as well as removing nodes.

## Features

- **Add Nodes:** Insert nodes at the beginning, end, before, or after specified nodes.
- **Remove Nodes:** Safely remove nodes from the list.
- **Visualization:** Visualize the linked list structure using `graphviz`.
- **Logging:** Track operations and errors using `loguru`.
- **Testing:** Ensure code correctness with `pytest`.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/atabekdemurtaza/LinkedList_implementation.git
   cd LinkedList_implementation

## Code Quality

This project uses `flake8`, `black`, and `isort` for code quality checks.

- **flake8**: Checks code against PEP 8 style guide.
- **black**: Formats code according to PEP 8.
- **isort**: Sorts imports alphabetically and by type.

### Linting and Formatting

To check code quality and format your code, run:

```bash
flake8
black .
isort .
