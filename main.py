#!/usr/bin/env python3
"""Write one short original poem about stopping to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the poem is a fixed string. No clock, no randomness, no network.
Run:  MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
"""

import os
import sys

POEM = """Stopping
---------

The road does not end when your feet do.
It waits, patient as a held breath,
while you learn the harder art:
not the going, but the stop.

The kettle sings and then is silent.
The hammer rests against the wall.
The hands that held the rope all day
unclench, and find they are hands again.

Stop, then - not as one defeated,
but as a field lies fallow in winter,
gathering under the snow
the green it will spend in spring.

The work will keep. The world will keep.
What will not keep is the you
who never learned to put it down.
So put it down. The quiet is a door,
and it has been yours all along.
"""


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    print("wrote %s (%d bytes)" % (path, len(POEM.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
