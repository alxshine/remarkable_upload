#!/bin/env python

import click
import requests
from joblib import Parallel, delayed
from typing import List

URL = "http://10.11.99.1/upload"


@click.command()
@click.argument("paths", nargs=-1, type=click.Path(readable=True))
def main(paths: List[str]):
    Parallel()(delayed(upload_path)(path) for path in paths)


def upload_path(path: str):
    files = {"file": open(path, "rb")}
    response = requests.post(URL, files=files)
    assert response.ok


if __name__ == "__main__":
    main()
