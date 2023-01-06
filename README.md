# python-programming

### Overview

Python programming code, tested and run on Docker containers.

### Commands

**Local Coding Environment Setup**

```bash
# One time Poetry install
pip3 install poetry

# Start the virtual environment and install the dependencies
poetry shell
poetry install
```

**Format Code**

```bash
black .
```

### Directories

| Directory Name   | Description                                                                    |
|------------------|--------------------------------------------------------------------------------|
| `.run`           | Run configurations to use in the PyCharm IDE.                                  |
| `coroutines`     | Python code using coroutines.                                                  |
| `http-requests`  | Python code making HTTP requests.                                              |
| `poetry.lock`    | Lock file containing Python dependencies installed by Poetry.                  |
| `pyproject.toml` | [Poetry](https://python-poetry.org/) dependency management configuration file. |

### Version History

**[v1.0.0](https://github.com/AJarombek/python-programming/tree/v1.0.0) - Initial Version**

> Release Date: Sep 9th, 2022

* First Python programming example related to coroutines.  All misc Python programs will be placed in this 
repository going forward.
