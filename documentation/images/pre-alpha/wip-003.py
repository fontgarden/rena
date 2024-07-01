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
    FS = 262.5
    db.fontSize(FS)
    db.fontVariations(opsz=MAIN_TEXT_OPSZ)
    db.text("يا باب الباب", (M+(U*0), M+(U*42.5)-(U*2)))
    db.text("Ya báb al-báb", (M+(U*24.1), M+(U*42.5)-(U*2)))
    db.text("أشهد يا إلهي", (M+(U*0), M+(U*35.5)-(U*2)))
    db.text("Ashadu ya ilahi", (M+(U*21.4), M+(U*35.5)-(U*2)))
    db.text("يا باب الباب", (M+(U*0), M+(U*28.5)-(U*2)))
    db.text("Ya báb al-báb", (M+(U*24.1), M+(U*28.5)-(U*2)))
    db.text("أشهد يا إلهي", (M+(U*0), M+(U*21.5)-(U*2)))
    db.text("Ashadu ya ilahi", (M+(U*21.4), M+(U*21.5)-(U*2)))
    db.text("يا باب الباب", (M+(U*0), M+(U*14.5)-(U*2)))
    db.text("Ya báb al-báb", (M+(U*24.1), M+(U*14.5)-(U*2)))
    db.text("أشهد يا إلهي", (M+(U*0), M+(U*7.5)-(U*2)))
    db.text("Ashadu ya ilahi", (M+(U*21.4), M+(U*7.5)-(U*2)))
    db.lineHeight(None)
    db.lineHeight(FS*1.0)
    # db.textBox("I deleted my sunscreen post because I didn't like my tone and thought the post could have been better. But I haven't forgotten sunscreen. I will be back with an even better anti-sunscreen post. Soon.", (M, M-(U*7), W-(M*1.75), W-(M*2)), align="left")

    # Auxillary text
    db.fontSize(80)
    db.fontVariations(opsz=14)
    db.text("github.com/fontgarden/rena", (M-(U*0.1), M+(U*0)))
    db.text("Open Font License OFL v1.1", (M+(U*30.5), M+(U*0)))
    db.text(f"Rena Regular: opsz {MAIN_TEXT_OPSZ}", (M-(U*0.1), M+(U*47)))
    db.text(f"Pre-Alpha: 1b93ba1 {FORMATTED_DATE}", (M+(U*28.2), M+(U*47)))

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
