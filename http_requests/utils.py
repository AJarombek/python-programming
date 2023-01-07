"""
Utility functions for making HTTP requests for files.
Author: Andrew Jarombek
Date: 1/7/2023
"""

import math


def format_file_sizes(size: int) -> str:
    if size == 0:
        return "0 B"

    size_name = ("B", "KB", "MB", "GB", 'TB')
    index = int(math.floor(math.log(size, 1000)))
    denominator = math.pow(1000, index)
    return f"{round(size / denominator, 2)} {size_name[index]}"
