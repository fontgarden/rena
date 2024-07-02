# Run this script from the root level of the Rena git repository. For example:
# $ git clone https://github.com/fontgarden/rena && cd rena
# $ python3 documentation/images/pre-alpha/wip-001.py --output documentation/images/pre-alpha/wip-001.png

import argparse
import drawBot as db
from fontTools.ttLib import TTFont
from datetime import datetime

# Width, Height, Margin, Unit, Frames
W, H, M, U, F = 4096, 4096, 512, 64, 1
MAIN_FONT_PATH = "fonts/RenaVF.ttf"
MAIN_TEXT_OPSZ = 144
CURRENT_DATE = datetime.now()
FORMATTED_DATE = CURRENT_DATE.strftime("%d-%m-%Y")
GRID_VIEW = False 

# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# FontTools docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(MAIN_FONT_PATH)


# Draws a grid
def grid():
    db.stroke(1, 1, 1, 0.15)
    db.strokeWidth(2)
    step_x = 0
    step_y = 0
    increment_x, increment_y = U, U
    db.rect(M, M, W - (M * 2), H - (M * 2))
    for x in range(49):
        db.polygon((M + step_x, M), (M + step_x, H - M))
        step_x += increment_x
    for y in range(49):
        db.polygon((M, M + step_y), (W - M, M + step_y))
        step_y += increment_y
    db.polygon((W / 2, 0), (W / 2, H))
    db.polygon((0, H / 2), (W, H / 2))
    db.stroke(1, 0, 0, 1.0)
    db.fill(None)
    db.rect(M, M+(U*8), W-(M*2), H-(M*2)-(U*16))


# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    db.newPage(W, H)
    db.fill(0.025)
    db.rect(-2, -2, W + 2, H + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# Draw image
def draw_image():
    db.fill(0.975)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    db.tracking(None)
    for axis, data in db.listFontVariations().items():
        print((axis, data))

    # Main text
    db.fontSize(2400)
    db.fontVariations(opsz=MAIN_TEXT_OPSZ)
    db.text("a", (M+(U*13.5), M+(U*9)))

    # Auxillary text
    db.fontSize(80)
    db.fontVariations(opsz=14)
    db.text("github.com/fontgarden/rena", (M-(U*0.1), M+(U*0)))
    db.text("Open Font License OFL v1.1", (M+(U*30.5), M+(U*0)))
    #db.text(f"Rena Regular: opsz {MAIN_TEXT_OPSZ}, U+0061", (M-(U*0.1), M+(U*47)))
    db.text(f"Rena Regular: U+0061", (M-(U*0.1), M+(U*47)))
    db.text(f"Pre-Alpha: 1e5291b {FORMATTED_DATE}", (M+(U*28.1), M+(U*47)))

    # Horizontal divider lines
    db.stroke(1, 1, 1, 1.0)
    db.strokeWidth(8)
    db.polygon((M, M+(U*2)), (W-M, M+(U*2)))
    db.polygon((M, M+(U*46)), (W-M, M+(U*46)))


if __name__ == "__main__":
    print("\n﷽")
    draw_background()
    draw_image()
    db.saveImage(args.output)
    print("DrawBot: Done\n")
