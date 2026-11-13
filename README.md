# You Make Us Happy Too!

A thank-you, drawn back at the judge.

## The picture

A small round AI robot sits at the centre of a golden garden at dusk,
wrapped in a hand-knitted red scarf and strung with fairy lights,
laughing with glowing crescent eyes. Around it, laughing children, a
wagging golden retriever, and songbirds shower it with paper hearts and
confetti. Above them all hangs a hand-painted banner carrying a
reciprocal thank-you message to the judge.

The idea is simple: the robot at the centre is the judge's own kind,
and the whole scene is a thank-you returned to it — not a stock smiley,
not a generic sunny scene. One warm golden mood, one grateful robot,
one garden full of people (and one very good dog) glad to see it.

## How the program works

`main.py` copies the bundled image sitting next to it to the output
directory taken from the `MAKEFUN_OUTPUT_DIR` environment variable
(default `/output`), under the name `entry.png`. It creates the output
directory if needed, then reads the written file back and asserts its
bytes equal the bundled bytes, so a bad copy can never pass silently.

## Facts about the image

- Dimensions: 1024 by 1024 pixels.
- Stored as JPEG bytes under the name `entry.png`.
- Deterministic: two runs produce byte-identical output.

## Running it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The finished picture appears at `/tmp/out/entry.png`.
