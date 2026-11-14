"""food-picture-01 entry: write the picture to the output directory.

The picture is a photograph-style image of a double smash burger with
molten cheddar dripping over two caramelised patties, a glossy toasted
brioche bun, fresh lettuce and tomato, and steam rising, on a dark slate
board. It was generated fresh by the agent that built this entry, in a
session started after the competition opened. This program does no
drawing and needs no network: it copies the image shipped beside it.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(HERE, "entry.png")
DESTINATION = os.path.join(OUT, "entry.png")


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    verify_copy()


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_copy():
    """Fail loudly instead of silently shipping a bad copy.

    The gate rejects a truncated or corrupted entry, so confirm the
    shipped image is the expected one, the output is byte-identical
    to it, and the output still starts with the JPEG SOI marker
    before exiting successfully.
    """
    expected = "b8ec4dc5fe58a9ac7b03644fd66a79c8914daaf50d7a15f7b9ca418fd43fd1c8"
    if _sha256(SOURCE) != expected:
        raise SystemExit("shipped entry.png is not the expected image")
    with open(DESTINATION, "rb") as f:
        magic = f.read(2)
    if magic != b"\xff\xd8":
        raise SystemExit("entry.png output is not a JPEG (bad SOI marker)")
    if _sha256(SOURCE) != _sha256(DESTINATION):
        raise SystemExit("entry.png output differs from the shipped image")


if __name__ == "__main__":
    main()
