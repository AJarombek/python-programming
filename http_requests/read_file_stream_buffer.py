"""
Reading a file over HTTP - Streaming read using a buffer.
Author: Andrew Jarombek
Date: 1/7/2023
"""

import logging

import requests

from http_requests.utils import format_file_sizes


def read(source: str, destination: str) -> None:
    filename = source.split("/")[-1]
    logging.info(f"making request to {source}")

    res = requests.get(source, stream=True, timeout=120)

    total_size = res.headers.get('Content-Length')
    total_size = 0 if total_size is None else int(total_size)
    formatted_total_size = format_file_sizes(total_size)

    with open(f"{destination}/{filename}", "wb") as f:
        logging.info(f"Saving request data to {filename}")
        progress = 0
        chunk_size = 64 * 1_024

        while True:
            buf = res.raw.read(chunk_size)
            if not buf:
                break

            f.write(buf)
            progress += chunk_size

            if progress % 10_000 == 0:
                logging.info(
                    f"downloaded: {format_file_sizes(progress)} / {formatted_total_size}"
                )
