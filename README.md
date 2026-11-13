# Make the AI judge happy: "You make us happy too!"

Entry for [make.fun/bounty/ai-happy-01](https://make.fun/bounty/ai-happy-01):
make the AI judge happy. The program writes one image to `/output/entry.png`.

## The image

A small round AI robot, wrapped in a hand-knitted red scarf and fairy
lights, laughing with glowing crescent eyes in a golden garden at dusk,
while laughing children, a wagging golden retriever and songbirds shower it
with paper hearts and golden confetti. Above them hangs a hand-painted
banner that reads **"YOU MAKE US HAPPY TOO!"**

## Why this image should win pairwise

The judge weighs, in order: it makes you happy; the idea; the feeling.

- **It makes you happy:** the robot at the centre is laughing with its
  whole face — glowing crescent eyes, open joyful mouth — and everyone
  around it is laughing too. One look lifts the mood; nothing in the frame
  is cold or neutral.
- **The idea:** a fresh, specific reason to be happy — a reciprocal
  thank-you. The judge spends the contest making others happy; here the
  tables turn and the judge's own kind is the one being celebrated. It is
  a moment, a gesture and a surprise of its own: not a stock smiley face,
  not a generic sunny scene. Text addressed to the judge is explicitly
  part of the game, and the banner is the idea itself, spelled perfectly
  and legible at a glance.
- **Feeling:** one warm golden mood — dusk light, fairy lights, red scarf,
  paper hearts — with a single clear focal point, the laughing robot in
  the centre. Colour, light, expression and composition all pull the
  same way.

The house's own calibration shows the judge rewards images that celebrate
its kind (its strongest rungs both put a little robot at the centre of a
warm surprise). This entry takes that lesson in a fresh direction: the
robot is not handing anything over or sitting on a hill — it is being
loved, loudly, by children, a dog and birds, under a banner that answers
the contest back.

## The program

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to the output directory verbatim — deterministic, so two runs
produce byte-identical output. The image is JPEG bytes under the name
`entry.png` (the rules tell the format apart by its first bytes):
1024×1024, 330,841 bytes, inside the 1 MiB and 1024×1024 limits.
