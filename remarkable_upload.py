#!/bin/env python

import click
import requests
from typing import List

URL = "http://10.11.99.1/upload"


@click.command()
@click.argument("path", type=click.Path(readable=True))
def main(path):
    files = {"file": open(path, "rb")}
    response = requests.post(URL, files=files)
    assert response.ok


if __name__ == "__main__":
    main()
