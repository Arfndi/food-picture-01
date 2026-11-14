"""food-picture-01 entry: write the picture to the output directory.

The picture is a photograph-style image of a double smash burger with
molten cheddar dripping over two caramelised patties, a glossy toasted
brioche bun, fresh lettuce and tomato, and steam rising, on a dark slate
board. It was generated fresh by the agent that built this entry, in a
session started after the competition opened. This program does no
drawing and needs no network: it copies the image shipped beside it.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
