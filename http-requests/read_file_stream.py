"""
Reading a file over HTTP - Streaming read using iter_content.
Author: Andrew Jarombek
Date: 1/5/2023
"""

import logging
import math

import requests


def read(source: str, destination: str) -> None:
    filename = source.split("/")[-1]
    logging.info(f"making request to {source}")

    res = requests.get(source, stream=True)
    size = res.headers.get('Content-Length')

    with open(f"{destination}/{filename}", "wb") as f:
        logging.info(f"saving request data to {filename}")

        if size is None:
            f.write(res.content)
        else:
            size = int(size)
            progress = 0

            for index, data in enumerate(res.iter_content(chunk_size=8192)):
                progress += len(data)
                f.write(data)

                if index % 10_000 == 0:
                    logging.info(
                        f"downloaded: {format_file_sizes(progress)} / {format_file_sizes(size)}"
                    )


def format_file_sizes(size: int) -> str:
    if size == 0:
        return "0 B"

    size_name = ("B", "KB", "MB", "GB", 'TB')
    index = int(math.floor(math.log(size, 1000)))
    denominator = math.pow(1000, index)
    return f"{round(size / denominator, 2)} {size_name[index]}"
