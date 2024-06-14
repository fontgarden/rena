# Run this script from the root level of the Rena git repository. For example:
# $ git clone https://github.com/fontgarden/rena && cd rena
# $ python3 documentation/images/pre-alpha/wip-001.py --output documentation/images/pre-alpha/wip-001.png

import argparse
import drawBot as db
from fontTools.misc.fixedTools import floatToFixedToStr
from fontTools.ttLib import TTFont

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 4096, 4096, 512, 1
MAIN_FONT_PATH = "fonts/RenaVF.ttf"

# Toggle this for a grid overlay
GRID_VIEW = False  # Toggle this for a grid overlay

# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Load the font with the parts of fonttools that are imported with the line:
# from fontTools.ttLib import TTFont
# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(MAIN_FONT_PATH)


# Draws a grid
def grid():
    db.stroke(1, 0, 0, 0.75)
    db.strokeWidth(2)
    step_x = 0
    step_y = 0
    increment_x, increment_y = MARGIN / 4, MARGIN / 4
    db.rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(61):
        db.polygon((MARGIN + step_x, MARGIN), (MARGIN + step_x, HEIGHT - MARGIN))
        step_x += increment_x
    for y in range(29):
        db.polygon((MARGIN, MARGIN + step_y), (WIDTH - MARGIN, MARGIN + step_y))
        step_y += increment_y
    db.polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    db.polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


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
    db.newPage(WIDTH, HEIGHT)
    db.fill(0.025)
    db.rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# Draw image
def draw_image():
    #db.image("documentation/auxiliary-images/bg_001.png", (0, 0), alpha=1.0)
    db.fill(0.975)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    # list all axis from the current font
    for axis, data in db.listFontVariations().items():
        print((axis, data))
    db.tracking(None)

    db.fontSize(358.9)
    db.fontVariations(opsz=40)
    # db.text("Font.Garden", (MARGIN*1.995, MARGIN * 6.30))
    db.text("Font.Garden", (MARGIN*1.995, MARGIN * 6.1))
    db.fontSize(MARGIN*5)
    db.text("^", (MARGIN*2, MARGIN*1.5))


# Build and save the image
if __name__ == "__main__":
    print("\n﷽")
    draw_background()
    draw_image()
    db.saveImage(args.output)
    print("DrawBot: Done\n")
