"""
Entrypoint for working with http requests.
Author: Andrew Jarombek
Date: 1/24/2023
"""

import read_file_memory

if __name__ == '__main__':
    # Datasets from https://data.gov/

    # https://dashboard.data.gov/offices/detail/49019/2021-12-31
    read_file_memory.read("https://www.energy.gov/sites/default/files/2023-01/pdl010123.json", "./dest/result.json")
